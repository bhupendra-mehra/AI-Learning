# Lesson 07 — Part 8: Storefront, Customer Registration, Login and Shopping Cart

Step 4: Build the Shopping Cart

Now that the storefront and customer authentication are working, let's implement a session-based shopping cart. Customers will be able to add products, change quantities, remove items and view their cart before checkout.

We'll keep the cart in Flask's session for now, so we don't need a separate cart database table. Orders and checkout will be handled in Part 9.

## 1. Create the cart routes

Create `app/routes/cart_routes.py`.


Python

Run

```
from decimal import Decimal

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    session,
    flash,
)

from app.database import SessionLocal
from app.repositories.product_repository import ProductRepository


cart_bp = Blueprint("cart", __name__, url_prefix="/cart")


@cart_bp.route("/")
def view_cart():
    cart = session.get("cart", {})
    cart_items = []
    total = Decimal("0.00")

    with SessionLocal() as db:
        repository = ProductRepository(db)

        for product_id, quantity in cart.items():
            product = repository.get_by_id(int(product_id))

            if product is None:
                continue

            quantity = int(quantity)
            subtotal = Decimal(str(product.price)) * quantity
            total += subtotal

            cart_items.append({
                "product": product,
                "quantity": quantity,
                "subtotal": subtotal,
            })

    return render_template(
        "cart/cart.html",
        cart_items=cart_items,
        total=total,
    )


@cart_bp.route("/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    try:
        quantity = int(request.form.get("quantity", 1))
    except (TypeError, ValueError):
        flash("Please enter a valid quantity.", "error")
        return redirect(url_for(
            "storefront.product_detail",
            product_id=product_id,
        ))

    if quantity < 1:
        flash("Quantity must be at least 1.", "error")
        return redirect(url_for(
            "storefront.product_detail",
            product_id=product_id,
        ))

    with SessionLocal() as db:
        repository = ProductRepository(db)
        product = repository.get_by_id(product_id)

        if product is None:
            flash("Product not found.", "error")
            return redirect(url_for("storefront.home"))

        cart = session.get("cart", {})
        current_quantity = int(cart.get(str(product_id), 0))
        new_quantity = current_quantity + quantity

        if new_quantity > product.stock:
            flash(
                f"Only {product.stock} units are currently available.",
                "error",
            )
            return redirect(url_for(
                "storefront.product_detail",
                product_id=product_id,
            ))

        cart[str(product_id)] = new_quantity
        session["cart"] = cart
        session.modified = True

    flash(f"{product.name} added to your cart.", "success")
    return redirect(url_for("cart.view_cart"))


@cart_bp.route("/update/<int:product_id>", methods=["POST"])
def update_cart(product_id):
    try:
        quantity = int(request.form.get("quantity", 1))
    except (TypeError, ValueError):
        flash("Please enter a valid quantity.", "error")
        return redirect(url_for("cart.view_cart"))

    cart = session.get("cart", {})
    product_key = str(product_id)

    if product_key not in cart:
        flash("That product is not in your cart.", "error")
        return redirect(url_for("cart.view_cart"))

    if quantity < 1:
        flash("Quantity must be at least 1.", "error")
        return redirect(url_for("cart.view_cart"))

    with SessionLocal() as db:
        repository = ProductRepository(db)
        product = repository.get_by_id(product_id)

        if product is None:
            cart.pop(product_key, None)
            session["cart"] = cart
            session.modified = True
            flash("The product is no longer available.", "error")
            return redirect(url_for("cart.view_cart"))

        if quantity > product.stock:
            flash(
                f"Only {product.stock} units are currently available.",
                "error",
            )
            return redirect(url_for("cart.view_cart"))

        cart[product_key] = quantity
        session["cart"] = cart
        session.modified = True

    flash("Cart updated.", "success")
    return redirect(url_for("cart.view_cart"))


@cart_bp.route("/remove/<int:product_id>", methods=["POST"])
def remove_from_cart(product_id):
    cart = session.get("cart", {})
    cart.pop(str(product_id), None)

    session["cart"] = cart
    session.modified = True

    flash("Product removed from your cart.", "success")
    return redirect(url_for("cart.view_cart"))
```

This implementation assumes your `ProductRepository.get_by_id()` method returns a product with its category relationship loaded, as in the previous step.

## 2. Register the cart blueprint

In `app/web.py`, import the blueprint:

Python

Run

```
from app.routes.cart_routes import cart_bp
```

Inside `create_app()`, register it:

Python

Run

```
app.register_blueprint(cart_bp)
```

Your existing storefront base template can now safely use:

jinja2

```
<a href="{{ url_for('cart.view_cart') }}">Cart</a>
```

## 3. Add the Add to Cart form to the product page

Update `app/templates/storefront/product_detail.html`. Add this form where you want the purchase controls to appear:

HTML

```
<form method="POST"
      action="{{ url_for('cart.add_to_cart', product_id=product.id) }}">

    <label for="quantity">Quantity</label>

    <input
        type="number"
        id="quantity"
        name="quantity"
        value="1"
        min="1"
        max="{{ product.stock }}"
        required
    >

    <button type="submit"
            {% if product.stock < 1 %}disabled{% endif %}>
        {% if product.stock > 0 %}
            Add to Cart
        {% else %}
            Out of Stock
        {% endif %}
    </button>
</form>
```

The form sends a POST request to the cart route, including the product ID and requested quantity.


## 4. Create the shopping cart template

Create the directory `app/templates/cart/`, then add `cart.html`:

HTML

```
{% extends "storefront/base_store.html" %}

{% block content %}
<div class="cart-container">
    <h1>Shopping Cart</h1>

    {% if cart_items %}
        <table class="cart-table">
            <thead>
                <tr>
                    <th>Product</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Subtotal</th>
                    <th>Action</th>
                </tr>
            </thead>

            <tbody>
                {% for item in cart_items %}
                    <tr>
                        <td>
                            <a href="{{ url_for(
                                'storefront.product_detail',
                                product_id=item.product.id
                            ) }}">
                                {{ item.product.name }}
                            </a>
                        </td>

                        <td>
                            ₹{{ "%.2f"|format(item.product.price) }}
                        </td>

                        <td>
                            <form method="POST"
                                  action="{{ url_for(
                                      'cart.update_cart',
                                      product_id=item.product.id
                                  ) }}">
                                <input
                                    type="number"
                                    name="quantity"
                                    value="{{ item.quantity }}"
                                    min="1"
                                    max="{{ item.product.stock }}"
                                    required
                                >
                                <button type="submit">Update</button>
                            </form>
                        </td>

                        <td>
                            ₹{{ "%.2f"|format(item.subtotal) }}
                        </td>

                        <td>
                            <form method="POST"
                                  action="{{ url_for(
                                      'cart.remove_from_cart',
                                      product_id=item.product.id
                                  ) }}">
                                <button type="submit">
                                    Remove
                                </button>
                            </form>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>

        <div class="cart-total">
            <h2>
                Cart Total: ₹{{ "%.2f"|format(total) }}
            </h2>

            <a href="{{ url_for('storefront.home') }}">
                Continue Shopping
            </a>

            <a href="{{ url_for('storefront.home') }}"
               class="checkout-button">
                Checkout (Coming in Part 9)
            </a>
        </div>
    {% else %}
        <p>Your shopping cart is empty.</p>
        <a href="{{ url_for('storefront.home') }}">
            Browse Products
        </a>
    {% endif %}
</div>
{% endblock %}
```

The checkout link is temporarily directed to the storefront. We'll replace it with the actual checkout route in Part 9.

## 5. Add basic cart styling

Add this CSS to your storefront stylesheet:

CSS

```
.cart-container {
    max-width: 1100px;
    margin: 30px auto;
    padding: 20px;
}

.cart-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

.cart-table th,
.cart-table td {
    padding: 12px;
    border-bottom: 1px solid #ddd;
    text-align: left;
}

.cart-table input[type="number"] {
    width: 65px;
    padding: 7px;
}

.cart-table button,
.checkout-button {
    padding: 8px 12px;
    border: none;
    border-radius: 4px;
    background: #2563eb;
    color: white;
    cursor: pointer;
    text-decoration: none;
}

.cart-total {
    margin-top: 25px;
    text-align: right;
}

.cart-total a {
    display: inline-block;
    margin: 10px;
}
```

## 6. Test the shopping cart

## Testing checklist

0 of 8 completed

Open a product detail page and add one item to the cart.

Add the same product again and verify its quantity increases.

Add a different product and verify both appear in the cart.

Update a product quantity and confirm the subtotal and total change.

Try a quantity exceeding available stock and verify it is rejected.

Remove a product and confirm it disappears from the cart.

Remove all products and verify the empty-cart message appears.

Refresh the page and verify the cart remains available in the session.

Important implementation notes

* This is a learning-stage, session-based cart. Flask's default session is stored in a signed cookie, so keep the cart small and never store passwords, payment details or other secrets in it.

* Stock is checked when adding or updating items, but it must be checked again during checkout because inventory can change.

* The cart total is for display only. Part 9 must recalculate prices and totals from the database when creating an order.

* Add CSRF protection to all POST forms before production.

* If your product prices are stored as `Decimal`, the route uses `Decimal` for subtotal and total calculations.

## Next: Part 9 — Simple Checkout and Order Creation

We'll implement customer-only checkout, validate cart items and inventory, create an `Order` with its `OrderItem` records using your existing SQLAlchemy models and repositories, and clear the cart only after a successful transaction.
