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

        if new_quantity > product.quantity:
            flash(
                f"Only {product.quantity} units are currently available.",
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

        if quantity > product.quantity:
            flash(
                f"Only {product.quantity} units are currently available.",
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