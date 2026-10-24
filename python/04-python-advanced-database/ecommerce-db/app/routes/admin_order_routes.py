from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from sqlalchemy import func, select
from sqlalchemy.orm import selectinload

from app.database import SessionLocal
from app.models.order import Order
from app.utils.admin_auth import admin_required
from app.utils.pagination import Pagination

admin_order_bp = Blueprint(
    "admin_orders",
    __name__,
    url_prefix="/admin/orders",
)

admin_order_bp.before_request(admin_required)

ALLOWED_STATUSES = {
    "pending",
    "processing",
    "shipped",
    "completed",
    "cancelled",
}


@admin_order_bp.route("/")
def list_orders():
    with SessionLocal() as db:
        # statement = (
        #     select(Order)
        #     .order_by(Order.id.desc())
        # )
        # orders = db.scalars(statement).all()

        # return render_template(
        #     "admin/orders/index.html",
        #     orders=orders,
        # )

        page = request.args.get("page", 1, type=int)
        per_page = 5
        offset = (page - 1) * per_page

        statement = (
            select(Order).order_by(Order.id.desc()).offset(offset).limit(per_page)
        )

        orders = list(db.scalars(statement).all())

        count_statement = select(func.count()).select_from(Order)

        total = db.scalar(count_statement) or 0

        pagination = Pagination(
            items=orders,
            page=page,
            per_page=per_page,
            total=total,
        )

        return render_template(
            "admin/orders/index.html",
            pagination=pagination,
        )


@admin_order_bp.route("/<int:order_id>")
def view_order(order_id):
    with SessionLocal() as db:
        statement = (
            select(Order).options(selectinload(Order.items)).where(Order.id == order_id)
        )
        order = db.scalar(statement)

        if order is None:
            abort(404)

        return render_template(
            "admin/orders/detail.html",
            order=order,
            allowed_statuses=sorted(ALLOWED_STATUSES),
        )


@admin_order_bp.route(
    "/<int:order_id>/status",
    methods=["POST"],
)
def update_order_status(order_id):
    status = request.form.get("status", "").strip().lower()

    if status not in ALLOWED_STATUSES:
        flash("Invalid order status.", "error")
        return redirect(
            url_for(
                "admin_orders.view_order",
                order_id=order_id,
            )
        )

    with SessionLocal() as db, db.begin():
        order = db.get(Order, order_id)

        if order is None:
            abort(404)

        order.status = status

    flash("Order status updated.", "success")
    return redirect(
        url_for(
            "admin_orders.view_order",
            order_id=order_id,
        )
    )
