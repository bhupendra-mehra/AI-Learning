# Lesson 07 — Part 10: Customer Order History, Admin Order Management, Integration Testing and Project Completion

Final lesson of the core e-commerce project


In this final part, we'll complete the e-commerce application by adding customer order history, an admin order management interface, integration checks, security improvements and project documentation.


By the end, your application will support the complete learning-project workflow:

## Final application workflow

1. Admin creates categories and products.

2. Customers register, log in and browse products.

3. Customers add products to their shopping cart.

4. Customers check out and place orders.

5. Customers view their order history and order details.

6. Admins view orders and update order statuses.

7. Tests validate the complete purchase workflow.

The examples use the project structure and model names from our earlier lessons. Since I don't have your current model and repository source files in this turn, compare the assumed fields with your actual code and adjust any differences before running.

# Step 1 — Customer order history

Customers should be able to see their previous orders, totals, dates and statuses, and open individual order details. They must only be able to access their own orders.

## 1.1 Create customer order routes

Create `app/routes/order_routes.py`:

Python

Run

```
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    session,
    flash,
)
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.database import SessionLocal
from app.models.order import Order


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
        statement = (
            select(Order)
            .where(Order.customer_id == customer_id)
            .order_by(Order.id.desc())
        )

        orders = db.scalars(statement).all()

        # Render while the session is open.
        return render_template(
            "orders/history.html",
            orders=orders,
        )


@order_bp.route("/<int:order_id>")
def order_detail(order_id):
    customer_id = session.get("customer_id")

    if not customer_id:
        flash("Please log in to view your order.", "error")
        return redirect(url_for("auth.login"))

    with SessionLocal() as db:
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
            order=order,
        )
```

The ownership condition in `order_detail()` is important: it prevents customers from viewing another customer's order by changing the URL.

## 1.2 Create the order history template

Create `app/templates/orders/history.html`:

HTML

```
{% extends "storefront/base_store.html" %}

{% block content %}
<div class="orders-container">
    <h1>My Orders</h1>

    {% if orders %}
        <table class="orders-table">
            <thead>
                <tr>
                    <th>Order ID</th>
                    <th>Status</th>
                    <th>Total</th>
                    <th>Details</th>
                </tr>
            </thead>

            <tbody>
                {% for order in orders %}
                    <tr>
                        <td>#{{ order.id }}</td>
                        <td>
                            <span class="status status-{{ order.status }}">
                                {{ order.status|capitalize }}
                            </span>
                        </td>
                        <td>
                            ₹{{ "%.2f"|format(order.total_amount) }}
                        </td>
                        <td>
                            <a href="{{ url_for(
                                'orders.order_detail',
                                order_id=order.id
                            ) }}">
                                View Order
                            </a>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <p>You haven't placed any orders yet.</p>
        <a href="{{ url_for('storefront.home') }}">
            Start Shopping
        </a>
    {% endif %}
</div>
{% endblock %}
```

## 1.3 Create the order detail template

Create `app/templates/orders/detail.html`:

HTML

```
{% extends "storefront/base_store.html" %}

{% block content %}
<div class="orders-container">
    <h1>Order #{{ order.id }}</h1>

    <p>
        Status:
        <strong>{{ order.status|capitalize }}</strong>
    </p>

    <h2>Items</h2>

    <table class="orders-table">
        <thead>
            <tr>
                <th>Product ID</th>
                <th>Quantity</th>
                <th>Unit Price</th>
                <th>Subtotal</th>
            </tr>
        </thead>

        <tbody>
            {% for item in order.items %}
                <tr>
                    <td>{{ item.product_id }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>
                        ₹{{ "%.2f"|format(item.unit_price) }}
                    </td>
                    <td>
                        ₹{{ "%.2f"|format(item.subtotal) }}
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>

    <h2>
        Total: ₹{{ "%.2f"|format(order.total_amount) }}
    </h2>

    <a href="{{ url_for('orders.order_history') }}">
        Back to My Orders
    </a>
</div>
{% endblock %}
```

If your Order model uses a `created_at` field, you can also display the order date in these templates. The current examples avoid assuming that field exists.

## 1.4 Register the blueprint

In `app/web.py`:

Python

Run

```
from app.routes.order_routes import order_bp
```

Inside `create_app()`:

Python

Run

```
app.register_blueprint(order_bp)
```

Add a link to the authenticated customer navigation in `app/templates/storefront/base_store.html`:

jinja2

```
{% if session.get('customer_id') %}
    <a href="{{ url_for('orders.order_history') }}">
        My Orders
    </a>
{% endif %}
```

# Step 2 — Admin order management

The admin should be able to view all orders, inspect order items and update order statuses.

Authorization requirement

Your existing admin CRUD routes must be protected by an admin-only authentication and authorization check. Do not assume that a logged-in customer is an administrator. The following route examples include an `admin_required` decorator placeholder; connect it to your existing admin authentication system before exposing these endpoints.

## 2.1 Create an admin authorization decorator

If your application already has an admin authorization decorator, reuse it. Otherwise, a basic session-based example is:

Create `app/utils/auth.py`:

Python

Run

```
from functools import wraps

from flask import session, redirect, url_for, flash, abort


def admin_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if not session.get("admin_id"):
            flash("Administrator access is required.", "error")
            abort(403)

        return view(*args, **kwargs)

    return wrapped_view
```

This expects your admin login to set `session["admin_id"]` only after successful administrator authentication. If your current admin login uses another session key, change the decorator to match it.

Create `app/routes/admin_order_routes.py`:

Python

Run

```
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    abort,
)
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.database import SessionLocal
from app.models.order import Order
from app.utils.auth import admin_required


admin_order_bp = Blueprint(
    "admin_orders",
    __name__,
    url_prefix="/admin/orders",
)

ALLOWED_STATUSES = {
    "pending",
    "processing",
    "shipped",
    "completed",
    "cancelled",
}


@admin_order_bp.route("/")
@admin_required
def list_orders():
    with SessionLocal() as db:
        statement = (
            select(Order)
            .order_by(Order.id.desc())
        )
        orders = db.scalars(statement).all()

        return render_template(
            "admin/orders/index.html",
            orders=orders,
        )


@admin_order_bp.route("/<int:order_id>")
@admin_required
def view_order(order_id):
    with SessionLocal() as db:
        statement = (
            select(Order)
            .options(selectinload(Order.items))
            .where(Order.id == order_id)
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
@admin_required
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

    with SessionLocal() as db:
        with db.begin():
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
```

This is a simple status-management workflow. In a production application, enforce allowed status transitions, for example, prevent a completed order from returning to pending, and handle cancellation and stock restoration as explicit business operations.

## 2.2 Register the admin blueprint

In `app/web.py`:

Python

Run

```
from app.routes.admin_order_routes import admin_order_bp
```

Inside `create_app()`:

Python

Run

```
app.register_blueprint(admin_order_bp)
```

## 2.3 Create the admin order list

Create `app/templates/admin/orders/index.html`:

HTML

```
{% extends "admin/base_admin.html" %}

{% block content %}
<div class="container">
    <h1>Order Management</h1>

    {% if orders %}
        <table>
            <thead>
                <tr>
                    <th>Order ID</th>
                    <th>Customer ID</th>
                    <th>Status</th>
                    <th>Total</th>
                    <th>Action</th>
                </tr>
            </thead>

            <tbody>
                {% for order in orders %}
                    <tr>
                        <td>#{{ order.id }}</td>
                        <td>{{ order.customer_id }}</td>
                        <td>{{ order.status|capitalize }}</td>
                        <td>
                            ₹{{ "%.2f"|format(order.total_amount) }}
                        </td>
                        <td>
                            <a href="{{ url_for(
                                'admin_orders.view_order',
                                order_id=order.id
                            ) }}">
                                View
                            </a>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <p>No orders found.</p>
    {% endif %}
</div>
{% endblock %}
```

## 2.4 Create the admin order detail page

Create `app/templates/admin/orders/detail.html`:

HTML

```
{% extends "admin/base_admin.html" %}

{% block content %}
<div class="container">
    <h1>Manage Order #{{ order.id }}</h1>

    <p>Customer ID: {{ order.customer_id }}</p>
    <p>Current Status: {{ order.status|capitalize }}</p>
    <p>
        Total:
        ₹{{ "%.2f"|format(order.total_amount) }}
    </p>

    <h2>Order Items</h2>

    <table>
        <thead>
            <tr>
                <th>Product ID</th>
                <th>Quantity</th>
                <th>Unit Price</th>
                <th>Subtotal</th>
            </tr>
        </thead>

        <tbody>
            {% for item in order.items %}
                <tr>
                    <td>{{ item.product_id }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>
                        ₹{{ "%.2f"|format(item.unit_price) }}
                    </td>
                    <td>
                        ₹{{ "%.2f"|format(item.subtotal) }}
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>

    <h2>Update Status</h2>

    <form method="POST"
          action="{{ url_for(
              'admin_orders.update_order_status',
              order_id=order.id
          ) }}">

        <label for="status">Order Status</label>

        <select id="status" name="status" required>
            {% for status in allowed_statuses %}
                <option value="{{ status }}"
                    {% if status == order.status %}selected{% endif %}>
                    {{ status|capitalize }}
                </option>
            {% endfor %}
        </select>

        <button type="submit">Update Status</button>
    </form>

    <p>
        <a href="{{ url_for('admin_orders.list_orders') }}">
            Back to Orders
        </a>
    </p>
</div>
{% endblock %}
```

These admin templates extend the existing admin `base.html`; the customer-facing templates continue to use `storefront/base_store.html`.


# Step 3 — Integration and security checks

Before writing tests, verify that the application's blueprints are registered and the application can start without endpoint or import errors.

## 3.1 Review the application factory

Your `app/web.py` should now register all the required blueprints. Keep the existing configuration and home route, adding the new ones:

Python

Run

```
import os

from flask import Flask, render_template

from app.routes.customer_routes import customer_bp
from app.routes.category_routes import category_bp
from app.routes.product_routes import product_bp
from app.routes.storefront_routes import storefront_bp
from app.routes.auth_routes import auth_bp
from app.routes.cart_routes import cart_bp
from app.routes.checkout_routes import checkout_bp
from app.routes.order_routes import order_bp
from app.routes.admin_order_routes import admin_order_bp


def create_app():
    app = Flask(__name__)

    app.secret_key = os.getenv(
        "SECRET_KEY",
        "dev-only-change-this-secret",
    )

    app.register_blueprint(customer_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(storefront_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(checkout_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(admin_order_bp)

    @app.route("/")
    def home():
        return render_template("index.html")

    return app
```

Keep `SECRET_KEY` configured in your environment as you already have it. The fallback shown here is for local development only; production should fail safely if a secure key is missing. Also ensure `.env` is loaded before reading environment variables if that's where you store the key.

## 3.2 Fix and verify the checkout implementation

Review the Part 9 checkout code before testing:

* Ensure `request` is imported from Flask.

* Ensure `Order` and `OrderItem` constructor fields match your models.

* Ensure the `Order.items` relationship uses the correct `back_populates` configuration.

* Confirm `Product.stock` is an integer and `price` is a `Decimal`-compatible `Numeric` column.

* Verify your database tables use a transactional engine such as InnoDB.

A crucial improvement: revalidate the cart at the moment of order creation. The service already reloads products, locks rows and checks stock, which is important because stock or prices may change after the checkout page is displayed.

For production, also implement idempotency protection so double-clicking the confirmation button or retrying a request cannot create duplicate orders. A unique checkout token stored server-side and consumed transactionally is one approach.

## 3.3 Add CSRF protection

Install Flask-WTF:

Bash

```
pip install Flask-WTF
```

Initialize CSRF protection in your application factory:

Python

Run

```
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ["SECRET_KEY"]

    csrf.init_app(app)

    # Register blueprints and routes here.
    return app
```

Add a CSRF token to each POST form, including login, registration, cart updates, checkout, logout and admin status changes:

jinja2

```
<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
```

For a Flask-WTF form, use `{{ form.hidden_tag() }}` instead. Do not exempt checkout or administrative forms from CSRF protection.

For production, also configure secure session cookies over HTTPS:

Python

Run

```
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE="Lax",
)
```

Use `SESSION_COOKIE_SECURE=True` in HTTPS deployments; for local HTTP development, configure it appropriately so your browser sends the session cookie.

# Step 4 — Automated integration tests

We'll use `pytest` and Flask's test client. The following are foundational route tests; a full purchase-flow test should additionally use a dedicated test database and fixtures for customers, products and orders.

## 4.1 Install testing dependencies

Bash

```
pip install pytest
```

Add the test dependency to your project's `requirements.txt` or development dependency file.

## 4.2 Create a basic application test

Create `tests/test_app.py`:

Python

Run

```
import pytest

from app.web import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        TESTING=True,
        WTF_CSRF_ENABLED=False,
        SECRET_KEY="test-secret-key",
    )
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_storefront_home_loads(client):
    response = client.get("/store/")

    assert response.status_code == 200


def test_login_page_loads(client):
    response = client.get("/login")

    assert response.status_code == 200


def test_registration_page_loads(client):
    response = client.get("/register")

    assert response.status_code == 200


def test_cart_requires_no_login_to_view(client):
    response = client.get("/cart/")

    assert response.status_code == 200


def test_checkout_requires_login(client):
    response = client.get("/checkout/")

    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


def test_customer_orders_require_login(client):
    response = client.get("/my-orders/")

    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


def test_admin_orders_require_admin(client):
    response = client.get("/admin/orders/")

    assert response.status_code == 403
```

The tests above assume the routes and authorization decorator use the paths and behavior shown in this lesson. They don't yet verify database writes or the entire checkout transaction. Add isolated database fixtures for those tests rather than pointing automated tests at your development database.

## 4.3 Run the tests

From your project root:

Bash

```
pytest -v
```

If the application imports the database configuration during startup, make sure the test environment has valid configuration or uses a dedicated test database. Do not run tests that modify or delete records in your everyday development database.

Recommended additional integration tests

* Register a customer and verify the password is hashed, not stored as plaintext.

* Log in with valid and invalid credentials.

* Add products to the cart and update quantities.

* Complete checkout and verify `Order`, `OrderItem` and stock changes are committed together.

* Force a failure during order creation and verify the transaction rolls back.

* Verify a customer cannot access another customer's order.

* Verify a non-admin cannot access admin order routes.

* Verify admin status changes are persisted.

* Verify a repeated checkout submission cannot duplicate the order once idempotency protection is implemented.


# Step 5 — Final project structure

After completing this lesson, your project should have a structure similar to the following. Keep your existing modules and add the new ones where needed.

```
ecommerce-db/
├── app/
│   ├── __init__.py
│   ├── web.py
│   ├── engine.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── connection.py
│   │   └── database.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── exceptions/
│   │   └── application.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── timestamp_mixin.py
│   │   ├── customer.py
│   │   ├── category.py
│   │   ├── product.py
│   │   ├── order.py
│   │   └── order_item.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── customer_repository.py
│   │   ├── product_repository.py
│   │   └── order_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── product_service.py
│   │   └── order_service.py
│   ├── routes/
│   │   ├── customer_routes.py
│   │   ├── category_routes.py
│   │   ├── product_routes.py
│   │   ├── storefront_routes.py
│   │   ├── auth_routes.py
│   │   ├── cart_routes.py
│   │   ├── checkout_routes.py
│   │   ├── order_routes.py
│   │   └── admin_order_routes.py
│   ├── utils/
│   │   └── auth.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── customers/
│       ├── categories/
│       ├── products/
│       ├── auth/
│       │   ├── login.html
│       │   └── register.html
│       ├── storefront/
│       │   ├── base_store.html
│       │   ├── home.html
│       │   ├── category.html
│       │   └── product_detail.html
│       ├── cart/
│       │   └── cart.html
│       ├── checkout/
│       │   ├── checkout.html
│       │   └── confirmation.html
│       ├── orders/
│       │   ├── history.html
│       │   └── detail.html
│       └── admin/
│           └── orders/
│               ├── index.html
│               └── detail.html
├── tests/
│   └── test_app.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── seed.py
└── tables.py
```

# Step 6 — Update the README

Replace or extend your `README.md` with project documentation like this:

Markdown

````
# Python E-Commerce Application

A learning project demonstrating a database-driven e-commerce application
built with Python, Flask, SQLAlchemy and MySQL.

## Features

### Admin
- Customer management
- Category management
- Product management
- Order listing and order status management

### Customer
- Customer registration and login
- Product storefront and category navigation
- Shopping cart
- Checkout and order creation
- Order history and order details

### Technical
- Flask application factory
- SQLAlchemy 2.x ORM
- MySQL database
- Repository and service layers
- Transactional order creation
- Password hashing
- Session-based authentication and cart
- Automated tests with pytest

## Technology Stack

- Python 3
- Flask
- SQLAlchemy 2.x
- MySQL
- Jinja2
- HTML and CSS
- pytest

## Project Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd ecommerce-db
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and configure the database connection
and application secret.

Example:

```dotenv
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ecommerce_db
SECRET_KEY=replace-with-a-strong-random-secret
```

Never commit your real `.env` file.

### 5. Create the database

Create the MySQL database and ensure the configured user has
the required permissions.

### 6. Create tables and seed data

Run the project's table creation and seed scripts according to
their implementation:

```bash
python -m app.tables
python -m app.seed
```

If your scripts are located at the project root, use the actual
script paths and invocation supported by your project.

### 7. Start the application

```bash
flask --app app.web run --debug
```

Open the local development URL shown by Flask.

## Running Tests

```bash
pytest -v
```

Use a separate test database and test configuration for integration
tests. Do not run destructive tests against your development database.

## Application Routes

| Route | Purpose |
|---|---|
| `/` | Existing application home |
| `/store/` | Customer storefront |
| `/store/category/<id>` | Category products |
| `/store/product/<id>` | Product details |
| `/register` | Customer registration |
| `/login` | Customer login |
| `/cart/` | Shopping cart |
| `/checkout/` | Checkout |
| `/checkout/confirmation/<id>` | Order confirmation |
| `/my-orders/` | Customer order history |
| `/my-orders/<id>` | Customer order details |
| `/admin/orders/` | Admin order management |

Existing customer, category and product administration routes
are retained in their respective route modules.

## Learning Outcomes

- Python application structure and modular design
- SQLAlchemy models, relationships and sessions
- Repository and service patterns
- Flask routes, templates and sessions
- Authentication and authorization fundamentals
- Transactional database operations
- E-commerce cart and order workflows
- Automated testing and project documentation

## Future Enhancements

- Docker Compose
- Alembic database migrations
- Product search, filtering and pagination
- Payment gateway integration
- Shipping and delivery tracking
- REST API
- Cloud deployment and CI/CD
````

Adjust the setup commands and route table to match the actual locations and endpoints in your repository.

# Step 7 — Final manual verification

## Project completion checklist

0 of 23 tasks completed

1. Database and admin

Create and verify all database tables and relationships.

Create, edit, list and delete customers, categories and products.

Verify category and product relationships display correctly.

2. Customer storefront

Browse the storefront and categories.

Open product detail pages and verify prices and stock.

Register, log in and log out successfully.

3. Cart and checkout

Add, update and remove cart items.

Validate stock availability and cart totals.

Place an order and verify order and order-item records.

Verify stock deduction and cart clearing after successful checkout.

4. Order management

View customer order history and details.

Verify customers cannot access other customers' orders.

View all orders as an administrator.

Update order statuses and verify persistence.

5. Quality and security

Run automated tests against a dedicated test database.

Enable CSRF protection on state-changing forms.

Verify administrator authorization and customer access controls.

Check transaction rollback and prevent duplicate checkout submissions.

Verify secrets are excluded from Git and review error handling.

6. Documentation

Update README setup and usage instructions.

Document environment variables and database initialization.

Add project screenshots and architecture notes if useful.

Commit the completed work to Git.

# Final result

Core curriculum complete

# Python E-Commerce Database Project

Your planned core project is now covered by Lessons 1–10, from database fundamentals and ORM development through storefront, authentication, cart, checkout, order history, administration and testing.

What you have learned and practiced:

* Python modular application development

* SQLAlchemy ORM and MySQL database integration

* Repository and service architecture

* Flask routing, templates and sessions

* E-commerce workflows and transactional order processing

* Authentication, authorization and web security fundamentals


* Integration testing and project documentation

One final distinction: this is the complete planned learning-project scope, not a claim that the implementation has been run or verified in your local environment. The code examples still need to be reconciled with your actual model fields, existing admin authentication and database setup, then tested end to end.

Once the checklist passes in your environment, you can consider the core project finished and move on to a separate enhancement phase, such as Docker Compose, database migrations, cloud deployment or a REST API.
