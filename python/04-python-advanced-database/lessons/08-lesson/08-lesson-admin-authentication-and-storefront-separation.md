# Lesson 08 — Admin Authentication and Storefront Separation

**Goal:** Separate the existing admin CRUD area from the customer storefront and add a temporary `.env`-based admin authentication system.

At the moment:

```text
http://127.0.0.1:5000/
```

contains the existing customer/category/product management functionality, while:

```text
http://127.0.0.1:5000/store/
```

is the customer storefront.

We will change this to:

```text
http://127.0.0.1:5000/
        │
        ├── Customer Store
        │      └── /store/
        │
        └── Admin
               ├── /admin/login
               ├── /admin/
               ├── /admin/customers/
               ├── /admin/categories/
               ├── /admin/products/
               └── /admin/orders/
```

The important requirement is:

> **Nobody should be able to access admin CRUD pages without successfully logging in as an administrator.**

---

# Lesson 08 — Part 1: Configure Admin Credentials

For now, we will keep the admin credentials in `.env`.

Later, we can replace this with a proper database-backed admin user system.

## 1.1 Update `.env`

Add:

```dotenv
SECRET_KEY=your-existing-secret-key

ADMIN_USERNAME=admin
ADMIN_PASSWORD=Admin@12345
```

Use your own strong password.

### Do not commit `.env`

Make sure `.gitignore` contains:

```gitignore
.env
```

Your GitHub repository should contain `.env.example`, but **never your actual `.env`**.

---

# Lesson 08 — Part 2: Create Admin Authentication Utility

Create:

```text
app/utils/admin_auth.py
```

Add:

```python
from functools import wraps

from flask import (
    session,
    redirect,
    url_for,
    flash,
)


def admin_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):

        if not session.get("admin_authenticated"):
            flash(
                "Please log in as administrator.",
                "error",
            )

            return redirect(
                url_for("admin_auth.login")
            )

        return view(*args, **kwargs)

    return wrapped_view
```

## What this does

Whenever an admin route is accessed, it checks:

```python
session.get("admin_authenticated")
```

If it doesn't exist:

```text
User
  ↓
Admin page
  ↓
Not authenticated
  ↓
/admin/login
```

If it exists:

```text
User
  ↓
Admin page
  ↓
Authenticated
  ↓
Allow access
```

---

# Lesson 08 — Part 3: Create Admin Login and Logout

Create:

```text
app/routes/admin_auth_routes.py
```

Add:

```python
import os
import hmac

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
)


admin_auth_bp = Blueprint(
    "admin_auth",
    __name__,
    url_prefix="/admin",
)


@admin_auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if session.get("admin_authenticated"):
        return redirect(url_for("admin.home"))

    if request.method == "POST":

        username = request.form.get(
            "username",
            "",
        ).strip()

        password = request.form.get(
            "password",
            "",
        )

        admin_username = os.getenv(
            "ADMIN_USERNAME"
        )

        admin_password = os.getenv(
            "ADMIN_PASSWORD"
        )

        if not admin_username or not admin_password:
            flash(
                "Admin credentials are not configured.",
                "error",
            )

            return render_template(
                "admin_auth/login.html"
            )

        username_valid = hmac.compare_digest(
            username,
            admin_username,
        )

        password_valid = hmac.compare_digest(
            password,
            admin_password,
        )

        if username_valid and password_valid:

            session.clear()

            session["admin_authenticated"] = True
            session["admin_username"] = admin_username

            flash(
                "Admin login successful.",
                "success",
            )

            return redirect(
                url_for("admin.home")
            )

        flash(
            "Invalid administrator credentials.",
            "error",
        )

    return render_template(
        "admin_auth/login.html"
    )


@admin_auth_bp.route("/logout", methods=["POST"])
def logout():

    session.clear()

    flash(
        "Administrator logged out.",
        "success",
    )

    return redirect(
        url_for("admin_auth.login")
    )
```

### Why use `hmac.compare_digest()`?

Instead of directly comparing:

```python
username == admin_username
```

we use:

```python
hmac.compare_digest(
    username,
    admin_username,
)
```

This provides a safer comparison for credentials.

---

# Lesson 08 — Part 4: Create the Admin Dashboard

Create:

```text
app/routes/admin_routes.py
```

Add:

```python
from flask import (
    Blueprint,
    render_template,
)

from app.utils.admin_auth import admin_required


admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin",
)


@admin_bp.route("/")
@admin_required
def home():

    return render_template(
        "admin/index.html"
    )
```

The admin dashboard will now be:

```text
http://127.0.0.1:5000/admin/
```

---

# Lesson 08 — Part 5: Create Admin Login Template

Create the directory:

```text
app/templates/admin_auth/
```

Then create:

```text
app/templates/admin_auth/login.html
```

```html
{% extends "admin/base_admin.html" %}

{% block content %}

<div class="auth-container">

    <h1>Administrator Login</h1>

    <form
        method="POST"
        action="{{ url_for('admin_auth.login') }}"
    >

        <div class="form-group">

            <label for="username">
                Username
            </label>

            <input
                type="text"
                id="username"
                name="username"
                required
                autocomplete="username"
            >

        </div>

        <div class="form-group">

            <label for="password">
                Password
            </label>

            <input
                type="password"
                id="password"
                name="password"
                required
                autocomplete="current-password"
            >

        </div>

        <button type="submit">
            Login
        </button>

    </form>

    <p>
        <a href="{{ url_for('storefront.home') }}">
            Back to Store
        </a>
    </p>

</div>

{% endblock %}
```

---

# Lesson 08 — Part 6: Create Admin Dashboard Template

Create:

```text
app/templates/admin/
```

Then:

```text
app/templates/admin/index.html
```

Add:

```html
{% extends "admin/base_admin.html" %}

{% block content %}

<div class="container">

    <h1>Admin Dashboard</h1>

    <p>
        Welcome,
        {{ session.get("admin_username") }}.
    </p>

    <div class="admin-menu">

        <p>
            <a href="{{ url_for('customers.list_customers') }}">
                Manage Customers
            </a>
        </p>

        <p>
            <a href="{{ url_for('categories.list_categories') }}">
                Manage Categories
            </a>
        </p>

        <p>
            <a href="{{ url_for('products.list_products') }}">
                Manage Products
            </a>
        </p>

        <p>
            <a href="{{ url_for('admin_orders.list_orders') }}">
                Manage Orders
            </a>
        </p>

    </div>

    <form
        method="POST"
        action="{{ url_for('admin_auth.logout') }}"
    >

        <button type="submit">
            Logout
        </button>

    </form>

</div>

{% endblock %}
```

> If your existing endpoint names are different, use the endpoint names from your current route files. Don't rename working routes just to match this example.

---

# Lesson 08 — Part 7: Protect Customer Admin CRUD

This is the **most important step of this lesson**.

Your existing:

```text
customer_routes.py
category_routes.py
product_routes.py
```

currently expose administrative CRUD functionality without authentication.

We will protect the entire blueprints.

---

## 7.1 Protect `customer_routes.py`

At the top:

```python
from app.utils.admin_auth import admin_required
```

Your blueprint should look like:

```python
customer_bp = Blueprint(
    "customers",
    __name__,
)

customer_bp.before_request(admin_required)
```

You don't need to put:

```python
@admin_required
```

on every customer route.

The blueprint-level protection covers all routes inside it.

---

# Lesson 08 — Part 8: Protect Category CRUD

In:

```text
app/routes/category_routes.py
```

Add:

```python
from app.utils.admin_auth import admin_required
```

Then:

```python
category_bp = Blueprint(
    "categories",
    __name__,
)

category_bp.before_request(admin_required)
```

Now all category administration requires admin authentication.

---

# Lesson 08 — Part 9: Protect Product CRUD

In:

```text
app/routes/product_routes.py
```

Add:

```python
from app.utils.admin_auth import admin_required
```

Then:

```python
product_bp = Blueprint(
    "products",
    __name__,
)

product_bp.before_request(admin_required)
```

Now:

```text
/products/
```

cannot be accessed anonymously.

---

# Lesson 08 — Part 10: Protect Admin Order Management

You already have:

```text
app/routes/admin_order_routes.py
```

from Part 10.

Protect the entire blueprint:

```python
from app.utils.admin_auth import admin_required
```

Then:

```python
admin_order_bp = Blueprint(
    "admin_orders",
    __name__,
    url_prefix="/admin/orders",
)

admin_order_bp.before_request(admin_required)
```

If you do this, you don't need individual:

```python
@admin_required
```

decorators on every route in that blueprint.

Use one approach consistently.

For your project, I recommend **blueprint-level protection**.

---

# Lesson 08 — Part 11: Update `web.py`

Your `app/web.py` should now register the application components clearly separated into customer and admin sections.

```python
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

from app.routes.admin_auth_routes import admin_auth_bp
from app.routes.admin_routes import admin_bp
from app.routes.admin_order_routes import admin_order_bp


def create_app():

    app = Flask(__name__)

    app.secret_key = os.getenv(
        "SECRET_KEY",
        "dev-only-change-this-secret",
    )

    # =========================================
    # CUSTOMER / STOREFRONT
    # =========================================

    app.register_blueprint(storefront_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(checkout_bp)
    app.register_blueprint(order_bp)

    # =========================================
    # ADMIN AUTHENTICATION
    # =========================================

    app.register_blueprint(admin_auth_bp)

    # =========================================
    # ADMIN DASHBOARD
    # =========================================

    app.register_blueprint(admin_bp)

    # =========================================
    # ADMIN CRUD
    # =========================================

    app.register_blueprint(customer_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(admin_order_bp)

    # =========================================
    # APPLICATION HOME
    # =========================================

    @app.route("/")
    def home():

        return render_template(
            "index.html"
        )

    return app
```

---

# Lesson 08 — Part 12: Change the Root `/` Page

We no longer want:

```text
/
```

to be the admin area.

Instead, it should become a simple application landing page.

The actual admin area will be:

```text
/admin/
```

Create/update:

```text
app/templates/index.html
```

```html
<!DOCTYPE html>

<html>

<head>
    <title>E-Commerce Application</title>
</head>

<body>

    <h1>E-Commerce Application</h1>

    <p>
        Welcome to the e-commerce application.
    </p>

    <p>
        <a href="{{ url_for('storefront.home') }}">
            Visit Store
        </a>
    </p>

    <p>
        <a href="{{ url_for('admin_auth.login') }}">
            Admin Login
        </a>
    </p>

</body>

</html>
```

Now:

```text
http://127.0.0.1:5000/
```

is just the application landing page.

---

# Lesson 08 — Part 13: Final URL Structure

After this lesson, your application should have the following separation.

## Public/customer side

```text
/
│
└── /store/
       │
       ├── /store/
       ├── /store/category/<id>
       └── /store/product/<id>
```

Customer authentication:

```text
/register
/login
/logout
```

Customer functionality:

```text
/cart/
/checkout/
/my-orders/
```

---

## Admin side

Admin login:

```text
/admin/login
```

Admin dashboard:

```text
/admin/
```

Admin CRUD:

```text
/customers/
/categories/
/products/
/admin/orders/
```

These routes are now protected by:

```python
admin_required
```

---

# Lesson 08 — Part 14: Authentication Separation

We now have two completely different session states.

## Customer login

```python
session.clear()

session["customer_id"] = customer.id
session["customer_name"] = customer.name
```

Customer accesses:

```text
/store/
/cart/
/checkout/
/my-orders/
```

---

## Admin login

```python
session.clear()

session["admin_authenticated"] = True
session["admin_username"] = admin_username
```

Admin accesses:

```text
/admin/
/customers/
/categories/
/products/
/admin/orders/
```

This gives us a clear separation:

```text
                 Flask Application
                        │
              ┌─────────┴─────────┐
              │                   │
          CUSTOMER              ADMIN
              │                   │
          /store/            /admin/login
              │                   │
          /cart/              /admin/
          /checkout/              │
          /my-orders/       Admin CRUD
```

---

# Lesson 08 — Part 15: Test Admin Authentication

Now test the implementation carefully.

## Test 1 — Admin login

Open:

```text
http://127.0.0.1:5000/admin/login
```

Use the credentials from `.env`.

For example:

```text
Username: admin
Password: Admin@12345
```

Expected:

```text
/admin/login
       ↓
successful login
       ↓
/admin/
```

---

## Test 2 — Invalid credentials

Enter an incorrect password.

Expected:

```text
Invalid administrator credentials.
```

You should remain on:

```text
/admin/login
```

---

## Test 3 — Access admin without login

Logout first.

Then directly visit:

```text
http://127.0.0.1:5000/products/
```

Expected:

```text
/products/
      ↓
not authenticated
      ↓
/admin/login
```

Test the same for:

```text
/customers/
```

```text
/categories/
```

```text
/admin/orders/
```

---

## Test 4 — Storefront without admin login

Without admin authentication, visit:

```text
http://127.0.0.1:5000/store/
```

It should continue working normally.

This is important:

> **Customer access must not require admin authentication.**

---

## Test 5 — Admin logout

After logging in as admin, click:

```text
Logout
```

Then try:

```text
/admin/
```

Expected:

```text
/admin/
    ↓
not authenticated
    ↓
/admin/login
```

---

# Lesson 08 — Part 16: Final Architecture

After completing this lesson, the architecture becomes:

```text
ecommerce-db/
│
├── app/
│   │
│   ├── routes/
│   │   │
│   │   ├── storefront_routes.py
│   │   ├── auth_routes.py
│   │   ├── cart_routes.py
│   │   ├── checkout_routes.py
│   │   ├── order_routes.py
│   │   │
│   │   ├── admin_auth_routes.py
│   │   ├── admin_routes.py
│   │   ├── admin_order_routes.py
│   │   │
│   │   ├── customer_routes.py
│   │   ├── category_routes.py
│   │   └── product_routes.py
│   │
│   ├── utils/
│   │   └── admin_auth.py
│   │
│   └── templates/
│       │
│       ├── admin_auth/
│       │   └── login.html
│       │
│       ├── admin/
│       │   └── index.html
│       │
│       └── storefront/
│
├── .env
├── .env.example
└── .gitignore
```

---

# Lesson 08 — Completion Checklist

| Requirement                              | Status |
| ---------------------------------------- | ------ |
| Admin credentials in `.env`              | ⬜      |
| Admin login                              | ⬜      |
| Admin logout                             | ⬜      |
| Admin dashboard `/admin/`                | ⬜      |
| Protect customer CRUD                    | ⬜      |
| Protect category CRUD                    | ⬜      |
| Protect product CRUD                     | ⬜      |
| Protect admin orders                     | ⬜      |
| Storefront remains public                | ⬜      |
| Customer authentication remains separate | ⬜      |
| Root `/` becomes landing page            | ⬜      |
| Direct unauthorized admin URL tested     | ⬜      |

---

## Important design decision

For **this version of the project**, we'll intentionally use:

```text
.env
 │
 ├── ADMIN_USERNAME
 └── ADMIN_PASSWORD
```

This keeps the implementation simple while we're learning Flask architecture.

**We will not create an `admins` database table yet.**

Later, as a separate security enhancement, we can upgrade this to:

```text
Admin User
    │
    ├── id
    ├── username
    ├── password_hash
    ├── role
    └── is_active
```

with hashed passwords and proper role-based authorization.

### Lesson 08 outcome

After this lesson, your application has a proper **Admin vs Customer boundary**:

```text
CUSTOMER
http://127.0.0.1:5000/store/

        VS

ADMIN
http://127.0.0.1:5000/admin/login
```

The existing Customer/Category/Product management functionality remains intact, but it is no longer publicly accessible without administrator authentication.

**Do this lesson before adding any more e-commerce features.** It establishes the correct security boundary for the rest of the project.
