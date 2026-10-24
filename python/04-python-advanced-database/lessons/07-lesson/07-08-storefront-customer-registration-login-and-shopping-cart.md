Yes, that is a sensible approach for completing your e-commerce project. Since your goal is to build a practical e-commerce application with Flask, SQLAlchemy, MySQL and a simple frontend, we don't need to introduce shipping, payment gateways or unnecessary complexity.

I'd recommend keeping Part 8 focused on the storefront, customer authentication and cart, then splitting the order workflow into two manageable parts.

## Updated project roadmap

## E-commerce project — final development stages

Part 8 — Current

Storefront, customer registration, login and shopping cart

* Browse categories and products

* Register, log in and log out

* Add, update and remove cart items

* Require login for cart actions

Part 9 — Order creation

Simple checkout and order placement

* Review cart items and order total

* Collect only essential order details, such as customer name and contact information, if needed

* Create an order and its order items

* Save a snapshot of each product's price

* Update stock and order status

* Clear the cart after successful order creation

* Use a database transaction to ensure consistency

Part 10 — Order management and project completion

Customer order history, admin order management and final integration

* View customer order history and order details

* Admin order list and detail pages

* Update order status (e.g. pending, confirmed, shipped, cancelled, if applicable)

* Validate stock and cancellation behavior

* Test the end-to-end customer journey

* Final cleanup, README and project documentation


## Let's begin Part 8 — Step 1: Customer authentication

We'll implement registration, login and logout first, then build the storefront pages on top of authenticated customer sessions.

### 1. Update the Customer model

In `app/models/customer.py`, add the password hash field to your existing `Customer` model:

Python

Run

```
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

# Add inside your existing Customer model
password_hash: Mapped[str | None] = mapped_column(
    String(255),
    nullable=True,
)
```

Keep your existing customer fields, relationships and timestamp mixin.

### 2. Update the MySQL table

Run this once against your existing database:

SQL

```
ALTER TABLE customers
ADD COLUMN password_hash VARCHAR(255) NULL;
```

Verify the change:

SQL

```
DESCRIBE customers;
```

Existing customers will retain their records, with `password_hash` set to `NULL` until they register or have credentials securely provisioned.

### 4. Add customer authentication routes

Create `app/routes/auth_routes.py`:

Python

Run

```
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
```

This assumes your `CustomerRepository` has `get_by_email()` and a `create()` method that accepts `name`, `email` and `password_hash`. If your current `create()` method doesn't accept the password hash yet, update it as follows:

Python

Run

```
def create(
    self,
    name: str,
    email: str,
    password_hash: str | None = None,
):
    customer = Customer(
        name=name,
        email=email,
        password_hash=password_hash,
    )
    self.session.add(customer)
    self.session.flush()
    return customer
```

Keep your existing repository methods and adjust only the `create()` signature and body as needed.


### 5. Create the registration and login templates

Create `app/templates/auth/register.html`:

HTML

```
{% extends "admin/base_admin.html" %}

{% block content %}
<h2>Create Account</h2>

<form method="POST" action="{{ url_for('auth.register') }}">
    <div>
        <label for="name">Full Name</label>
        <input
            type="text"
            id="name"
            name="name"
            value="{{ request.form.get('name', '') }}"
            required
        >
    </div>

    <div>
        <label for="email">Email</label>
        <input
            type="email"
            id="email"
            name="email"
            value="{{ request.form.get('email', '') }}"
            required
        >
    </div>

    <div>
        <label for="password">Password</label>
        <input
            type="password"
            id="password"
            name="password"
            minlength="8"
            required
        >
    </div>

    <button type="submit">Register</button>
</form>

<p>
    Already have an account?
    <a href="{{ url_for('auth.login') }}">Login</a>
</p>
{% endblock %}
```

Create `app/templates/auth/login.html`:

HTML

```
{% extends "admin/base_admin.html" %}

{% block content %}
<h2>Customer Login</h2>

<form method="POST" action="{{ url_for('auth.login') }}">
    <div>
        <label for="email">Email</label>
        <input
            type="email"
            id="email"
            name="email"
            value="{{ request.form.get('email', '') }}"
            required
        >
    </div>

    <div>
        <label for="password">Password</label>
        <input
            type="password"
            id="password"
            name="password"
            required
        >
    </div>

    <button type="submit">Login</button>
</form>

<p>
    Don't have an account?
    <a href="{{ url_for('auth.register') }}">Register</a>
</p>
{% endblock %}
```

These forms assume your existing `base.html` renders Flask flashed messages.

### 6. Register the authentication blueprint

In `app/web.py`, add:

Python

Run

```
from app.routes.auth_routes import auth_bp

app.register_blueprint(auth_bp)
```

The authentication routes will be available at `/register`, `/login` and `/logout`.

The `storefront.home` endpoint referenced above will be added in the next implementation step when we create the storefront blueprint.

Security and integration notes

* Add CSRF protection to registration, login and logout forms before production use.

* Set secure cookie options (`SESSION_COOKIE_HTTPONLY`, `SESSION_COOKIE_SAMESITE`, and `SESSION_COOKIE_SECURE` when using HTTPS).

* Existing admin-created customers with no password cannot log in using this form until they establish credentials.

* For a production application, add rate limiting to login and registration, and ensure customer sessions are checked against the database.

* Don't expose customer management routes to ordinary logged-in customers.

## Step 1 testing

After adding the storefront placeholder endpoint in the next step, test this flow:

1. Register a new customer.

2. Verify the customer record and password hash in MySQL.

3. Log out.

4. Log in with the registered email and password.

5. Try an incorrect password and verify access is denied.

6. Try registering with the same email again and verify the duplicate is rejected.

Once authentication works, we'll move to Step 2: storefront layout and category navigation, followed by category product pages and the shopping cart.
