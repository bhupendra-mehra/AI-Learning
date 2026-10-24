from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    session,
    url_for,
)
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.database import SessionLocal
from app.models.order import Order
from app.repositories.category_repository import CategoryRepository

order_bp = Blueprint(
    "orders",
    __name__,
    url_prefix="/my-orders",
)


@order_bp.route("/")
def order_history():
    customer_id = session.get("customer_id")

    if not customer_id:
        flash("Please log in to view your orders.", "error")
        return redirect(url_for("auth.login"))

    with SessionLocal() as db:
        category_repository = CategoryRepository(db)
        categories = category_repository.get_categories()
        statement = (
            select(Order)
            .where(Order.customer_id == customer_id)
            .order_by(Order.id.desc())
        )

        orders = db.scalars(statement).all()

        # Render while the session is open.
        return render_template(
            "orders/history.html",
            orders=orders,categories=categories
        )


@order_bp.route("/<int:order_id>")
def order_detail(order_id):
    customer_id = session.get("customer_id")

    if not customer_id:
        flash("Please log in to view your order.", "error")
        return redirect(url_for("auth.login"))

    with SessionLocal() as db:
        category_repository = CategoryRepository(db)
        categories = category_repository.get_categories()
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
            return redirect(url_for("orders.order_history"))

        return render_template(
            "orders/detail.html",
            order=order,categories=categories
        )