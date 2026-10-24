# Lesson 07 — Part 6: Customer Edit and Delete with Flask, HTML and SQLAlchemy

Practical lesson

CRUD operations

In this lesson, we'll extend your existing Flask e-commerce application to support editing and deleting customers, while reusing a single HTML template for both customer creation and editing.

We'll keep separate Flask route functions for creating and editing customers, use your existing `CustomerRepository`, and follow the SQLAlchemy 2.x `select()` style.

## 1. Learning objectives

By the end of this lesson, you'll be able to:

* Display existing customers with Edit and Delete actions.

* Reuse one `customer_form.html` template for creating and editing.

* Retrieve a customer by ID and prefill the edit form.

* Update customer information with duplicate email validation.

* Delete customers with a confirmation prompt.

* Handle missing customer IDs, database errors and transaction rollbacks.

* Verify changes in MySQL.

## 2. Expected project structure

We'll use the following structure, retaining your existing application files:

```
app/
├── database/
│   ├── __init__.py
│   ├── connection.py
│   └── database.py
├── models/
│   └── customer.py
├── repositories/
│   └── customer_repository.py
├── routes/
│   └── customer_routes.py
├── templates/
│   ├── base.html
│   └── customers/
│       ├── list.html
│       └── customer_form.html
└── web.py
```

The `customer_form.html` template replaces the separate `create.html` and `edit.html` templates.

## 3. Customer CRUD routes

|
Operation

|

HTTP method

|

Route

|

Description

|
| --- | --- | --- | --- |
|

Create

|

GET, POST

|

`/customers/create`

|

Display form and insert customer

|
|

Read

|

GET

|

`/customers/`

|

List all customers

|
|

Update

|

GET, POST

|

`/customers/<id>/edit`

|

Display form and update customer

|
|

Delete

|

POST

|

`/customers/<id>/delete`

|

Delete customer

|

We'll use POST for deletion to avoid destructive actions from simply opening a URL.

## 4. Update the CustomerRepository

Open `app/repositories/customer_repository.py`.

Use SQLAlchemy 2.x syntax with `select()` and `session.scalars()` for queries.

Python

Run

```
from sqlalchemy import select

from app.models.customer import Customer


class CustomerRepository:

    def __init__(self, session):
        self.session = session

    def create(self, name: str, email: str):
        customer = Customer(
            name=name,
            email=email
        )

        self.session.add(customer)
        self.session.flush()

        return customer

    def get_by_id(self, customer_id: int):
        return self.session.get(Customer, customer_id)

    def get_by_email(self, email: str):
        statement = select(Customer).where(
            Customer.email == email
        )

        return self.session.scalars(statement).first()

    def get_all(self):
        statement = (
            select(Customer)
            .order_by(Customer.id.desc())
        )

        return self.session.scalars(statement).all()

    def update(
        self,
        customer: Customer,
        name: str,
        email: str
    ):
        customer.name = name
        customer.email = email

        self.session.flush()

        return customer

    def delete(self, customer: Customer):
        self.session.delete(customer)
        self.session.flush()
```

### Understanding the repository methods

* `create()` adds a new customer and flushes the pending insert.

* `get_by_id()` retrieves a customer using its primary key.

* `get_by_email()` finds a customer by email, useful for duplicate validation.

* `get_all()` returns customers ordered by descending ID.

* `update()` modifies the existing ORM object.

* `delete()` marks the customer for deletion.

The repository does not commit transactions. The route manages `commit()` and `rollback()` so the application can control transaction boundaries.

## 5. Create a shared customer form

Create `app/templates/customers/customer_form.html`.

This single template will serve both create and edit operations.

HTML

```
{% extends "admin/base_admin.html" %}

{% block title %}
    {% if customer %}
        Edit Customer
    {% else %}
        Add Customer
    {% endif %}
{% endblock %}

{% block content %}

<h2>
    {% if customer %}
        Edit Customer
    {% else %}
        Add Customer
    {% endif %}
</h2>

<form method="POST"
      action="{% if customer %}
          {{ url_for(
              'customers.edit_customer',
              customer_id=customer.id
          ) }}
      {% else %}
          {{ url_for('customers.create_customer') }}
      {% endif %}">

    <label for="name">Customer Name</label>
    <input
        type="text"
        id="name"
        name="name"
        value="{{ customer.name if customer else '' }}"
        placeholder="Enter customer name"
        required
        maxlength="100"
    >

    <label for="email">Email Address</label>
    <input
        type="email"
        id="email"
        name="email"
        value="{{ customer.email if customer else '' }}"
        placeholder="Enter email address"
        required
        maxlength="255"
    >

    <button type="submit">
        {% if customer %}
            Update Customer
        {% else %}
            Create Customer
        {% endif %}
    </button>

    <a href="{{ url_for('customers.list_customers') }}">
        Cancel
    </a>

</form>

{% endblock %}
```

### How the shared template works

The template checks whether a `customer` object was passed to it.

Create mode

Add Customer

Customer Name

Enter customer name

Email Address

Enter email address

Create Customer

Submits to `create_customer()`.

Edit mode

Edit Customer

Customer Name

Bhupendra Mehra

Email Address

[bhupendra@example.com](mailto:bhupendra@example.com)

Update Customer

Submits to `edit_customer()` with the customer ID.

Illustrative previews; the actual form is rendered by Flask and Jinja.

When creating a customer, the route passes `customer=None`, so the form is empty. When editing, the route passes the retrieved customer object, so the existing values are prefilled.


## 6. Update customer routes

Open `app/routes/customer_routes.py`. The following is the complete route module, combining the existing customer listing and creation functionality with the new edit and delete routes.

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
    abort,
)
from sqlalchemy.exc import IntegrityError

from app.database import SessionLocal
from app.repositories.customer_repository import CustomerRepository


customer_bp = Blueprint(
    "customers",
    __name__,
    url_prefix="/customers"
)


# READ: List all customers
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


# CREATE: Add a new customer
# CREATE: Add a new customer
@customer_bp.route("/create", methods=["GET", "POST"])
def create_customer():
    if request.method == "GET":
        return render_template(
            "customers/customer_form.html",
            customer=None
        )

    session = SessionLocal()

    try:
        return _save_customer(session)

    finally:
        session.close()


# UPDATE: Edit an existing customer
@customer_bp.route(
    "/<int:customer_id>/edit",
    methods=["GET", "POST"]
)
def edit_customer(customer_id):
    session = SessionLocal()

    try:
        repository = CustomerRepository(session)
        customer = repository.get_by_id(customer_id)

        if customer is None:
            abort(404)

        if request.method == "GET":
            return render_template(
                "customers/customer_form.html",
                customer=customer
            )

        return _save_customer(
            session=session,
            customer=customer
        )

    finally:
        session.close()


# DELETE: Remove an existing customer
@customer_bp.route(
    "/<int:customer_id>/delete",
    methods=["POST"]
)
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

        flash(
            f"Customer {customer_name} deleted successfully.",
            "success"
        )

        return redirect(
            url_for("customers.list_customers")
        )

    except IntegrityError:
        session.rollback()

        flash(
            "Cannot delete this customer because related records "
            "exist, such as orders.",
            "error"
        )

        return redirect(
            url_for("customers.list_customers")
        )

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
        return render_template(
            "customers/customer_form.html",
            customer=customer
        ), 400

    # Check for duplicate email
    existing_customer = repository.get_by_email(email)

    if (
        existing_customer is not None
        and (
            not is_edit
            or existing_customer.id != customer.id
        )
    ):
        flash(
            "A customer with this email already exists.",
            "error"
        )
        return render_template(
            "customers/customer_form.html",
            customer=customer
        ), 409

    try:
        if is_edit:
            repository.update(
                customer=customer,
                name=name,
                email=email
            )
            action = "updated"
        else:
            customer = repository.create(
                name=name,
                email=email
            )
            action = "created"

        customer_name = customer.name
        session.commit()

        flash(
            f"Customer {customer_name} {action} successfully.",
            "success"
        )

        return redirect(
            url_for("customers.list_customers")
        )

    except IntegrityError:
        session.rollback()
        flash(
            "This email is already registered.",
            "error"
        )
        return render_template(
            "customers/customer_form.html",
            customer=customer
        ), 409

    except Exception:
        session.rollback()
        raise
```

Important implementation notes

* The create and edit routes remain separate, but both render `customer_form.html`.

* The edit route excludes the current customer when checking for duplicate emails.

* `IntegrityError` catches database constraint violations, including concurrent duplicate-email attempts.

* Each route closes its session using `finally`.

* The example uses basic form validation. For production, add server-side email format validation, CSRF protection, authentication and authorization.

## 7. Update the customer listing template

Open `app/templates/customers/list.html` and add Edit and Delete actions to your customer table.

HTML

```
{% extends "admin/base_admin.html" %}

{% block title %}Customers{% endblock %}

{% block content %}

<h2>Customers</h2>

<a href="{{ url_for('customers.create_customer') }}">
    Add Customer
</a>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Actions</th>
        </tr>
    </thead>

    <tbody>
        {% for customer in customers %}
        <tr>
            <td>{{ customer.id }}</td>
            <td>{{ customer.name }}</td>
            <td>{{ customer.email }}</td>
            <td>
                <a href="{{ url_for(
                    'customers.edit_customer',
                    customer_id=customer.id
                ) }}">
                    Edit
                </a>

                <form
                    method="POST"
                    action="{{ url_for(
                        'customers.delete_customer',
                        customer_id=customer.id
                    ) }}"
                    onsubmit="return confirm(
                        'Are you sure you want to delete this customer?'
                    );"
                    style="display: inline;"
                >
                    <button type="submit">Delete</button>
                </form>
            </td>
        </tr>
        {% else %}
        <tr>
            <td colspan="4">No customers found.</td>
        </tr>
        {% endfor %}
    </tbody>
</table>

{% endblock %}
```

The Edit link navigates to the customer-specific edit page. The Delete form submits a POST request and uses a browser confirmation dialog to help prevent accidental deletion.

## 8. Verify the Flask application setup

Make sure `app/web.py` registers the customer blueprint. If your existing file already does this, no change is necessary.

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

The default secret key is for local learning only. Set a strong, random `SECRET_KEY` through your environment before deploying.


## 9. Run the application

From your project root:

Bash

```
cd /var/www/html/advanced-python-database/ecommerce-db

python -m app.run
```

Open these pages in your browser:

|
URL

|

Expected result

|
| --- | --- |
|

`http://127.0.0.1:5000/customers/`

|

Customer list with Edit and Delete

|
|

`http://127.0.0.1:5000/customers/create`

|

Empty customer form

|
|

`http://127.0.0.1:5000/customers/1/edit`

|

Edit form for customer ID 1

|

Replace `1` with an existing customer ID in your database.

## 10. Test the CRUD operations

Practical exercise checklist

0 / 8

Open the customer list and verify existing records are displayed.

Click Add Customer and create a new customer.

Click Edit and verify the existing customer details are prefilled.

Change the customer's name and save; verify the updated success message.

Try changing the email to one already used by another customer.

Open an invalid customer ID edit URL and verify a 404 response.

Delete a customer without related orders and verify it disappears from the list.

Attempt to delete a customer with existing orders and verify the database constraint error is handled.

Reset checklist

## 11. Verify the database in MySQL

SQL

```
USE ecommerce;

-- List customers
SELECT
    id,
    name,
    email,
    created_at,
    updated_at
FROM customers
ORDER BY id DESC;

-- Check a specific customer
SELECT *
FROM customers
WHERE id = 1;

-- Check whether a customer has existing orders
SELECT
    customer_id,
    COUNT(*) AS total_orders
FROM orders
WHERE customer_id = 1
GROUP BY customer_id;
```

Replace `1` with the customer ID you're testing. After editing, verify the new values and `updated_at` timestamp. After deletion, verify the customer no longer exists.

## 12. Important e-commerce considerations

Avoid deleting customers with order history

In a real e-commerce application, customer records are often linked to orders, invoices, payments and shipping details. Permanently deleting a customer could compromise historical records.

For production, consider:

* Soft deletion using an `is_active` or `deleted_at` field.

* Deactivation instead of permanent deletion.

* Preserving historical order and transaction records.

* Adding CSRF protection using Flask-WTF.

* Restricting customer modifications and deletion to authorized users.

The current lesson deliberately uses hard deletion to demonstrate CRUD and database integrity handling. If your database has a foreign key from `orders.customer_id` to `customers.id` with restrictive deletion behavior, the delete route will roll back and display its related-records error.

## 13. Final project structure

```
app/
├── database/
│   ├── __init__.py
│   ├── connection.py
│   └── database.py
├── models/
│   ├── customer.py
│   ├── category.py
│   ├── product.py
│   ├── order.py
│   └── order_item.py
├── repositories/
│   ├── customer_repository.py
│   ├── product_repository.py
│   └── order_repository.py
├── routes/
│   └── customer_routes.py
├── services/
│   ├── order_service.py
│   └── product_service.py
├── templates/
│   ├── base.html
│   └── customers/
│       ├── list.html
│       └── customer_form.html
├── web.py
├── main.py
├── seed.py
└── tables.py
```

## Lesson 07 — Part 6 complete

Customer Edit and Delete

You've now implemented customer creation, listing, editing and deletion using Flask, Jinja, SQLAlchemy 2.x and MySQL, with one shared form for create and edit.

Next: Lesson 07 — Part 7: Category and Product Management

* Create and list product categories.

* Create and edit products with a category dropdown.

* Validate product SKU, price and stock.

* Persist product data through SQLAlchemy repositories.

* Prepare the application for order placement using your existing `OrderService`.
