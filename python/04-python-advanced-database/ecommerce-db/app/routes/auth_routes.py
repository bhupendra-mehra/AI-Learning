from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from sqlalchemy.exc import IntegrityError
from werkzeug.security import (
    check_password_hash,
    generate_password_hash,
)

from app.database import SessionLocal
from app.repositories.customer_repository import CustomerRepository

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not name or not email or not password:
            flash("All fields are required.", "error")
            return render_template("auth/register.html")

        if len(password) < 8:
            flash("Password must be at least 8 characters.", "error")
            return render_template("auth/register.html")

        with SessionLocal() as db:
            repository = CustomerRepository(db)

            if repository.get_by_email(email):
                flash("An account with this email already exists.", "error")
                return render_template("auth/register.html")

            try:
                customer = repository.create(
                    name=name,
                    email=email,
                    password_hash=generate_password_hash(password),
                )
                db.commit()

                # Start an authenticated session after successful registration.
                session.clear()
                session["customer_id"] = customer.id

                flash("Registration successful. Welcome!", "success")
                return redirect(url_for("storefront.home"))

            except IntegrityError:
                db.rollback()
                flash("Unable to register with this email.", "error")

    return render_template("auth/register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        with SessionLocal() as db:
            repository = CustomerRepository(db)
            customer = repository.get_by_email(email)

            if (
                customer is None
                or not customer.password_hash
                or not check_password_hash(customer.password_hash, password)
            ):
                flash("Invalid email or password.", "error")
                return render_template("auth/login.html")

            session.clear()
            session["customer_id"] = customer.id

            flash("Login successful.", "success")
            return redirect(url_for("storefront.home"))

    return render_template("auth/login.html")


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("storefront.home"))