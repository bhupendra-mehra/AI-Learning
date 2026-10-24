
from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from sqlalchemy.exc import IntegrityError

from app.database import SessionLocal
from app.repositories.customer_repository import CustomerRepository
from app.utils.admin_auth import admin_required

customer_bp = Blueprint("admin_customers", __name__, url_prefix="/admin/customers")

customer_bp.before_request(admin_required)


# READ: List all customers
@customer_bp.route("/")
def list_customers():
    session = SessionLocal()

    try:
        customer_repository = CustomerRepository(session)
        page = request.args.get("page", 1, type=int)

        pagination = customer_repository.get_all(page=page, per_page=5)

        return render_template(
            "admin/customers/list.html",
            pagination=pagination,
        )

    finally:
        session.close()


# CREATE: Add a new customer
@customer_bp.route("/create", methods=["GET", "POST"])
def create_customer():
    if request.method == "GET":
        return render_template("admin/customers/customer_form.html", customer=None)

    session = SessionLocal()

    try:
        return _save_customer(session)

    finally:
        session.close()


# UPDATE: Edit an existing customer
@customer_bp.route("/<int:customer_id>/edit", methods=["GET", "POST"])
def edit_customer(customer_id):
    session = SessionLocal()

    try:
        repository = CustomerRepository(session)
        customer = repository.get_by_id(customer_id)

        if customer is None:
            abort(404)

        if request.method == "GET":
            return render_template(
                "admin/customers/customer_form.html", customer=customer
            )

        return _save_customer(session=session, customer=customer)

    finally:
        session.close()


# DELETE: Remove an existing customer
@customer_bp.route("/<int:customer_id>/delete", methods=["POST"])
def delete_customer(customer_id):
    session = SessionLocal()

    try:
        repository = CustomerRepository(session)
        customer = repository.get_by_id(customer_id)

        if customer is None:
            abort(404)

        customer_name = customer.name

        repository.delete(customer)
        session.commit()

        flash(f"Customer {customer_name} deleted successfully.", "success")

        return redirect(url_for("admin_customers.list_customers"))

    except IntegrityError:
        session.rollback()

        flash(
            "Cannot delete this customer because related records "
            "exist, such as orders.",
            "error",
        )

        return redirect(url_for("admin_customers.list_customers"))

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


def _save_customer(session, customer=None):
    repository = CustomerRepository(session)

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()

    is_edit = customer is not None

    # Validate required fields
    if not name or not email:
        flash("Name and email are required.", "error")
        return (
            render_template("admin/customers/customer_form.html", customer=customer),
            400,
        )

    # Check for duplicate email
    existing_customer = repository.get_by_email(email)

    if existing_customer is not None and (
        not is_edit or existing_customer.id != customer.id
    ):
        flash("A customer with this email already exists.", "error")
        return (
            render_template("admin/customers/customer_form.html", customer=customer),
            409,
        )

    try:
        if is_edit:
            repository.update(customer=customer, name=name, email=email)
            action = "updated"
        else:
            customer = repository.create(name=name, email=email)
            action = "created"

        customer_name = customer.name
        session.commit()

        flash(f"Customer {customer_name} {action} successfully.", "success")

        return redirect(url_for("admin_customers.list_customers"))

    except IntegrityError:
        session.rollback()
        flash("This email is already registered.", "error")
        return (
            render_template("admin/customers/customer_form.html", customer=customer),
            409,
        )

    except Exception:
        session.rollback()
        raise
