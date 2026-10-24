# Lesson 07 — Part 5: Add Customer Form with Flask, HTML and SQLAlchemy

We'll continue from the customer listing page and implement the Add Customer form. When you submit the form, Flask will validate the input, use your existing `CustomerRepository`, and save the customer to MySQL.

Current progress

* SQLAlchemy models, relationships and MySQL tables created

* Database session and customer repository configured

* Flask application and Jinja templates set up

* Customer listing page implemented

* Next: customer creation form and database insertion

## 1. Create the customer form template

Create `app/templates/customers/create.html`:


HTML

```
{% extends "admin/base_admin.html" %}

{% block title %}Add Customer{% endblock %}

{% block content %}

<h2>Add Customer</h2>

<form method="POST" action="{{ url_for('customers.create_customer') }}">

    <label for="name">Customer Name</label>
    <input
        type="text"
        id="name"
        name="name"
        placeholder="Enter customer name"
        required
        maxlength="100"
    >

    <label for="email">Email Address</label>
    <input
        type="email"
        id="email"
        name="email"
        placeholder="Enter email address"
        required
        maxlength="255"
    >

    <button type="submit">Create Customer</button>

    <a href="{{ url_for('customers.list_customers') }}">Cancel</a>

</form>

{% endblock %}
```

## 2. Add the create route

Update `app/routes/customer_routes.py` to include the customer creation endpoint. Keep your existing listing route and add the following imports and route.

Python

Run

```
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from sqlalchemy.exc import IntegrityError

from app.database import SessionLocal
from app.repositories.customer_repository import CustomerRepository


customer_bp = Blueprint(
    "customers",
    __name__,
    url_prefix="/customers"
)


@customer_bp.route("/")
def list_customers():
    session = SessionLocal()

    try:
        repository = CustomerRepository(session)
        customers = repository.get_all()

        return render_template(
            "customers/list.html",
            customers=customers
        )
    finally:
        session.close()


@customer_bp.route("/create", methods=["GET", "POST"])
def create_customer():
    if request.method == "GET":
        return render_template("customers/create.html")

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()

    if not name or not email:
        flash("Name and email are required.", "error")
        return render_template("customers/create.html"), 400

    session = SessionLocal()

    try:
        repository = CustomerRepository(session)

        existing_customer = repository.get_by_email(email)

        if existing_customer:
            flash("A customer with this email already exists.", "error")
            return render_template("customers/create.html"), 409

        customer = repository.create(
            name=name,
            email=email
        )

        session.commit()

        flash(
            f"Customer {customer.name} created successfully.",
            "success"
        )

        return redirect(url_for("customers.list_customers"))

    except IntegrityError:
        session.rollback()
        flash("This email is already registered.", "error")
        return render_template("customers/create.html"), 409

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()
```

The `IntegrityError` handler catches a database uniqueness violation, including a duplicate email inserted concurrently after the initial lookup. The `finally` block ensures the session is closed on every path.

## 3. Enable Flask flash messages

In `app/web.py`, configure a secret key so Flask can securely sign its session cookie. Use an environment variable rather than committing a production secret.

Python

Run

```
import os

from flask import Flask, render_template

from app.routes.customer_routes import customer_bp


def create_app():
    app = Flask(__name__)

    app.secret_key = os.getenv(
        "SECRET_KEY",
        "dev-only-change-this-secret"
    )

    app.register_blueprint(customer_bp)

    @app.route("/")
    def home():
        return render_template("index.html")

    return app
```

Add this to your local `.env`:

env

```
SECRET_KEY=replace-with-a-long-random-secret
```

Keep `.env` excluded from Git, and add a placeholder to `.env.example`:

env

```
SECRET_KEY=
```

The fallback secret is for local learning only; configure a strong secret in any deployed environment.


## 4. Display success and error messages

Update `app/templates/base.html`. Add this inside `<main>`, before the content block:

HTML

```
<main>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% for category, message in messages %}
            <div class="alert {{ category }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endwith %}

    {% block content %}
    {% endblock %}
</main>
```

Add these styles to `app/static/css/style.css`:

CSS

```
.alert {
    padding: 12px;
    margin-bottom: 20px;
    border-radius: 4px;
}

.alert.success {
    background: #d1fae5;
    color: #065f46;
}

.alert.error {
    background: #fee2e2;
    color: #991b1b;
}

form a {
    margin-left: 12px;
}
```

## 5. Understand the request flow

HTML customer form

Name and email submitted using POST

Flask route

Validates input and checks for duplicate email

CustomerRepository

Creates the Customer ORM object and flushes it

SQLAlchemy Session

Commits the transaction

MySQL

Persists the customer in the `customers` table

## 6. Run and test the application

From your project root:

Bash

```
python -m app.run
```

Open these pages:

|
URL

|

Purpose

|
| --- | --- |
|

`http://127.0.0.1:5000/`

|

Home page

|
|

`http://127.0.0.1:5000/customers/`

|

Customer list

|
|

`http://127.0.0.1:5000/customers/create`

|

Add customer form

|

## Expected form

# Add Customer

Customer Name

Email Address

Illustrative form preview; submit the actual form on your local Flask application to save a record.

Copy test data

Test with a new customer, for example:

```
Name: Bhupendra Mehra
Email: bhupendra@example.com
```

After submitting, the application should redirect to the customer list and display a success message.

Verify the database:

SQL

```
USE ecommerce;

SELECT id, name, email, created_at, updated_at
FROM customers
ORDER BY id DESC;
```

Also test submitting the same email twice. The application should display a duplicate-email message rather than inserting a second customer.

## Completion checklist

Customer creation page loads

Valid customer can be inserted

Customer appears in the listing

Duplicate email is rejected

Timestamps are populated in MySQL

0 of 5 completed

Next: We'll build the Category and Product creation forms, including a category dropdown populated from MySQL. After that, we'll implement the order placement form with stock validation, order items, price snapshots, and a single transaction with commit or rollback.

For a learning project, this is sufficient to proceed. Before deploying it publicly, add CSRF protection (for example, Flask-WTF), stronger validation, and production-grade error handling.
