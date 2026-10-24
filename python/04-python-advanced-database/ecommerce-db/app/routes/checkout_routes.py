from decimal import Decimal

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
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
            with SessionLocal() as db, db.begin():
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
            if quantity < 1 or quantity > product.quantity:
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