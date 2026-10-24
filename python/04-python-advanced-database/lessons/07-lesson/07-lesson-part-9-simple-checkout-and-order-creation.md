# Lesson 07 — Part 9: Simple Checkout and Order Creation

Step 1: Checkout and Order Processing

In Part 8, we built the storefront, customer authentication and session-based shopping cart. Now we'll connect the cart to your existing SQLAlchemy `Order` and `OrderItem` models.

The checkout will be deliberately simple: logged-in customers confirm their order, inventory is validated, and an order is saved to MySQL. No shipping or payment integration yet.

Checkout workflow

1. Customer adds products to the cart.

2. Customer logs in and proceeds to checkout.

3. System reloads products and validates stock and prices.

4. Customer confirms the order.

5. System creates the order and its line items in one database transaction.

6. Cart is cleared only after the transaction succeeds.

## 1. Review your existing models

We'll use the following expected fields. Compare these with your actual models before proceeding.

|
Model

|

Expected fields

|
| --- | --- |
|

`Order`

|

`id`, `customer_id`, `status`, `total_amount`

|
|

`OrderItem`

|

`id`, `order_id`, `product_id`, `quantity`, `unit_price`, `subtotal`

|
|

`Product`

|

`id`, `name`, `price`, `stock`

|
|

`Customer`

|

`id`, `name`, `email`

|

The examples below assume your order status is stored as a string and that the order-item model stores the unit price and subtotal. If your field names differ, adapt the code accordingly.

## 2. Create the checkout service

Create or update `app/services/order_service.py`.

The service handles business logic independently of Flask routes. It validates the cart, checks stock, creates the order and decrements inventory in a transaction.


Python

Run

```
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product


class OrderService:
    def __init__(self, session: Session):
        self.session = session

    def create_order(self, customer_id: int, cart: dict) -> Order:
        if not cart:
            raise ValueError("Your shopping cart is empty.")

        order_items = []
        total_amount = Decimal("0.00")

        # Lock product rows while validating and creating the order.
        # This helps prevent concurrent checkouts overselling stock.
        for product_id, quantity in cart.items():
            try:
                product_id = int(product_id)
                quantity = int(quantity)
            except (TypeError, ValueError):
                raise ValueError("Your cart contains invalid items.")

            if quantity < 1:
                raise ValueError("Product quantities must be at least 1.")

            statement = (
                select(Product)
                .where(Product.id == product_id)
                .with_for_update()
            )
            product = self.session.scalar(statement)

            if product is None:
                raise ValueError(
                    f"Product #{product_id} is no longer available."
                )

            if quantity > product.stock:
                raise ValueError(
                    f"Insufficient stock for {product.name}. "
                    f"Available: {product.stock}."
                )

            unit_price = Decimal(str(product.price))
            subtotal = unit_price * quantity
            total_amount += subtotal

            order_items.append({
                "product": product,
                "quantity": quantity,
                "unit_price": unit_price,
                "subtotal": subtotal,
            })

        order = Order(
            customer_id=customer_id,
            status="pending",
            total_amount=total_amount,
        )

        self.session.add(order)
        self.session.flush()

        for item in order_items:
            product = item["product"]

            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=item["quantity"],
                unit_price=item["unit_price"],
                subtotal=item["subtotal"],
            )

            self.session.add(order_item)
            product.stock -= item["quantity"]

        self.session.flush()
        return order
```

The service expects to run inside a database transaction. The caller controls commit and rollback. `with_for_update()` is supported by MySQL's transactional storage engines, such as InnoDB.

## 3. Add the checkout route

Create `app/routes/checkout_routes.py`.

This route requires an authenticated customer. It displays a confirmation page on GET and creates the order only on POST.

Python

Run

```
from decimal import Decimal

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    session,
    flash,
)

from app.database import SessionLocal
from app.repositories.product_repository import ProductRepository
from app.services.order_service import OrderService


checkout_bp = Blueprint(
    "checkout",
    __name__,
    url_prefix="/checkout",
)


def get_checkout_customer_id():
    return session.get("customer_id")


@checkout_bp.route("/", methods=["GET", "POST"])
def checkout():
    customer_id = get_checkout_customer_id()

    if not customer_id:
        flash("Please log in to continue checkout.", "error")
        return redirect(url_for(
            "auth.login",
            next=url_for("checkout.checkout"),
        ))

    cart = session.get("cart", {})

    if not cart:
        flash("Your shopping cart is empty.", "error")
        return redirect(url_for("cart.view_cart"))

    if request.method == "POST":
        try:
            with SessionLocal() as db:
                with db.begin():
                    order_service = OrderService(db)
                    order = order_service.create_order(
                        customer_id=customer_id,
                        cart=cart,
                    )
                    order_id = order.id

            # Clear cart only after the transaction commits successfully.
            session.pop("cart", None)

            flash("Your order has been placed successfully.", "success")
            return redirect(
                url_for("checkout.order_confirmation",
                        order_id=order_id)
            )

        except ValueError as error:
            flash(str(error), "error")
            return redirect(url_for("cart.view_cart"))

    cart_items = []
    total = Decimal("0.00")

    with SessionLocal() as db:
        repository = ProductRepository(db)

        for product_id, quantity in cart.items():
            product = repository.get_by_id(int(product_id))

            if product is None:
                flash(
                    "A product in your cart is no longer available.",
                    "error",
                )
                return redirect(url_for("cart.view_cart"))

            quantity = int(quantity)
            if quantity < 1 or quantity > product.stock:
                flash(
                    f"Please update the quantity for {product.name}.",
                    "error",
                )
                return redirect(url_for("cart.view_cart"))

            subtotal = Decimal(str(product.price)) * quantity
            total += subtotal

            cart_items.append({
                "product": product,
                "quantity": quantity,
                "subtotal": subtotal,
            })

    return render_template(
        "checkout/checkout.html",
        cart_items=cart_items,
        total=total,
    )


@checkout_bp.route("/confirmation/<int:order_id>")
def order_confirmation(order_id):
    customer_id = get_checkout_customer_id()

    if not customer_id:
        flash("Please log in to view your order.", "error")
        return redirect(url_for("auth.login"))

    with SessionLocal() as db:
        from sqlalchemy import select
        from sqlalchemy.orm import selectinload

        from app.models.order import Order

        statement = (
            select(Order)
            .options(selectinload(Order.items))
            .where(
                Order.id == order_id,
                Order.customer_id == customer_id,
            )
        )
        order = db.scalar(statement)

        if order is None:
            flash("Order not found.", "error")
            return redirect(url_for("storefront.home"))

        return render_template(
            "checkout/confirmation.html",
            order=order,
        )
```

Add the missing `request` import to the Flask imports at the top:

Python

Run

```
from flask import request
```

The customer ID is taken from the authenticated session, not from the submitted form. The confirmation route also verifies order ownership, so customers cannot view another customer's order by changing the URL.

## 4. Register the checkout blueprint

In `app/web.py`, import:

Python

Run

```
from app.routes.checkout_routes import checkout_bp
```

Then register it inside `create_app()`:

Python

Run

```
app.register_blueprint(checkout_bp)
```


## 5. Create the checkout template

Create `app/templates/checkout/checkout.html`:

HTML

```
{% extends "storefront/base_store.html" %}

{% block content %}
<div class="checkout-container">
    <h1>Review Your Order</h1>

    <table class="cart-table">
        <thead>
            <tr>
                <th>Product</th>
                <th>Price</th>
                <th>Quantity</th>
                <th>Subtotal</th>
            </tr>
        </thead>
        <tbody>
            {% for item in cart_items %}
            <tr>
                <td>{{ item.product.name }}</td>
                <td>₹{{ "%.2f"|format(item.product.price) }}</td>
                <td>{{ item.quantity }}</td>
                <td>₹{{ "%.2f"|format(item.subtotal) }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <div class="checkout-summary">
        <h2>Total: ₹{{ "%.2f"|format(total) }}</h2>
        <p>Payment and shipping are not included in this learning exercise.</p>

        <form method="POST" action="{{ url_for('checkout.checkout') }}">
            <button type="submit">Confirm Order</button>
        </form>

        <a href="{{ url_for('cart.view_cart') }}">Back to Cart</a>
    </div>
</div>
{% endblock %}
```

## 6. Create the order confirmation template

Create `app/templates/checkout/confirmation.html`:

HTML

```
{% extends "storefront/base_store.html" %}

{% block content %}
<div class="checkout-container">
    <h1>Order Placed Successfully!</h1>

    <p>Thank you for your purchase.</p>

    <h2>Order #{{ order.id }}</h2>
    <p>Status: {{ order.status }}</p>
    <p>Total: ₹{{ "%.2f"|format(order.total_amount) }}</p>

    <h3>Order Items</h3>

    <table class="cart-table">
        <thead>
            <tr>
                <th>Product ID</th>
                <th>Quantity</th>
                <th>Unit Price</th>
                <th>Subtotal</th>
            </tr>
        </thead>
        <tbody>
            {% for item in order.items %}
            <tr>
                <td>{{ item.product_id }}</td>
                <td>{{ item.quantity }}</td>
                <td>₹{{ "%.2f"|format(item.unit_price) }}</td>
                <td>₹{{ "%.2f"|format(item.subtotal) }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <a href="{{ url_for('storefront.home') }}">
        Continue Shopping
    </a>
</div>
{% endblock %}
```

## 7. Connect the cart to checkout

In `app/templates/cart/cart.html`, replace the placeholder checkout link with:

HTML

```
<a href="{{ url_for('checkout.checkout') }}"
   class="checkout-button">
    Proceed to Checkout
</a>
```

## 8. Test the checkout workflow

## Part 9 testing checklist

0 of 9 completed

Log in as a customer and add products to the cart.

Open checkout and verify product names, quantities, prices and total.

Submit checkout and verify an order and its order items are saved.

Verify product stock decreases by the purchased quantities.

Verify the cart is cleared after successful order creation.

Try checking out while logged out; confirm login is required.

Try ordering more than the available stock; confirm the order is rejected and the cart remains.

Try refreshing the confirmation page; confirm it does not create a second order.

Try accessing another customer's order confirmation URL; confirm access is denied.

Important adjustments before running

* Ensure your `Order` and `OrderItem` field names match the examples. Your existing models may use different names or have additional required fields.

* The code assumes `Order.items` is the relationship to `OrderItem`, and `OrderItem` has `unit_price` and `subtotal`.

* If your customer login route does not support the `next` parameter, remove `next=url_for("checkout.checkout")` from the login redirect or implement safe post-login redirection. After logging in, the customer can return to checkout.

* The checkout form needs CSRF protection before production.

* For robust inventory handling, use InnoDB transactions and ensure your database uses the expected transactional isolation and locking behavior. Consider idempotency protection against duplicate order submissions in a production system.

* The sample catches validation errors; unexpected database errors should be logged and handled with a user-friendly error page, while the transaction rolls back.

Part 9 outcome: customers can review their cart, confirm a simple order, and receive an order confirmation, with stock decremented and order records committed together.

Next: Part 10 — Customer Order History, Admin Order Management, Integration Testing and Documentation.
