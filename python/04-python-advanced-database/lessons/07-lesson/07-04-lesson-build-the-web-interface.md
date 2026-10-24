# Lesson 07 — Part 4: Build the Web Interface

We will now turn our SQLAlchemy project into a small working e-commerce application using:

```text
Flask
Jinja2
HTML
CSS
SQLAlchemy
MySQL
```

We will **not change your existing ORM architecture**.

## 1. Install Flask

Inside your virtual environment:

```bash
pip install Flask
```

Then update `requirements.txt`:

```text
Flask
SQLAlchemy
mysql-connector-python
python-dotenv
```

You can verify:

```bash
pip show Flask
```

---

# 2. Target architecture

Your current project:

```text
ecommerce-db/
└── app/
    ├── config/
    ├── database/
    ├── exceptions/
    ├── models/
    ├── repositories/
    ├── services/
    ├── engine.py
    ├── main.py
    ├── seed.py
    └── tables.py
```

We'll add:

```text
app/
├── routes/
│   ├── __init__.py
│   ├── customer_routes.py
│   ├── product_routes.py
│   └── order_routes.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   │
│   ├── customers/
│   │   ├── list.html
│   │   └── create.html
│   │
│   ├── products/
│   │   ├── list.html
│   │   └── create.html
│   │
│   └── orders/
│       ├── list.html
│       ├── create.html
│       └── detail.html
│
└── static/
    └── css/
        └── style.css
```

We'll build this incrementally rather than creating all the files at once.

---

# 3. First: create the Flask application

Create:

```text
app/web.py
```

Put:

```python
from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return """
        <h1>E-Commerce Application</h1>
        <p>SQLAlchemy ORM + Flask + MySQL</p>
        """

    return app
```

Now create:

```text
app/run.py
```

```python
from app.web import create_app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
```

---

# 4. Start the application

From the project root:

```bash
python -m app.run
```

You should see something similar to:

```text
* Running on http://127.0.0.1:5000
```

Open:

```text
http://127.0.0.1:5000
```

You should see:

```text
E-Commerce Application

SQLAlchemy ORM + Flask + MySQL
```

---

# 5. Why are we using `create_app()`?

Instead of:

```python
app = Flask(__name__)
```

directly in a huge file, we're using:

```python
def create_app():
    app = Flask(__name__)
    return app
```

This is called the **Application Factory pattern**.

It becomes useful as the application grows.

Eventually:

```text
create_app()
    │
    ├── configure database
    ├── register routes
    ├── register error handlers
    ├── register extensions
    └── return Flask application
```

This is a common pattern in real Flask applications.

---

# 6. Create our first HTML template

Right now we're returning HTML directly from Python:

```python
return """
<h1>E-Commerce Application</h1>
"""
```

That's okay for testing, but we don't want to build an application this way.

Create:

```bash
mkdir -p app/templates
```

Create:

```text
app/templates/base.html
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{% block title %}E-Commerce Application{% endblock %}</title>

    <link
        rel="stylesheet"
        href="{{ url_for('static', filename='css/style.css') }}"
    >
</head>

<body>

<header>
    <h1>E-Commerce Application</h1>

    <nav>
        <a href="/">Home</a>
        <a href="/customers">Customers</a>
        <a href="/products">Products</a>
        <a href="/orders">Orders</a>
    </nav>
</header>

<main>
    {% block content %}
    {% endblock %}
</main>

</body>
</html>
```

---

# 7. Create the CSS

Create the directory:

```bash
mkdir -p app/static/css
```

Create:

```text
app/static/css/style.css
```

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    padding: 20px;
    border-bottom: 1px solid #ddd;
}

nav a {
    margin-right: 15px;
    text-decoration: none;
}

main {
    padding: 30px;
}

form {
    max-width: 500px;
}

label {
    display: block;
    margin-top: 15px;
}

input,
select {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
}

button {
    margin-top: 20px;
    padding: 10px 20px;
    cursor: pointer;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

th,
td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}
```

---

# 8. Change `web.py` to use Jinja

Update:

```text
app/web.py
```

to:

```python
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("index.html")

    return app
```

Now create:

```text
app/templates/index.html
```

```html
{% extends "admin/base_admin.html" %}

{% block title %}
Home
{% endblock %}

{% block content %}

<h2>Welcome to the E-Commerce Application</h2>

<p>
    This application demonstrates:
</p>

<ul>
    <li>Flask</li>
    <li>SQLAlchemy ORM</li>
    <li>MySQL</li>
    <li>Repository Pattern</li>
    <li>Service Layer</li>
    <li>Database Transactions</li>
</ul>

{% endblock %}
```

Restart Flask if necessary:

```bash
python -m app.run
```

Then refresh:

```text
http://127.0.0.1:5000
```

---

# 9. Why Jinja templates?

Our architecture is now:

```text
Browser
   ↓
Flask Route
   ↓
render_template()
   ↓
Jinja
   ↓
HTML
   ↓
Browser
```

For example:

```python
return render_template(
    "index.html"
)
```

Flask finds:

```text
app/templates/index.html
```

and sends the rendered HTML to the browser.

---

# 10. Now connect Customers to the UI

This is where things become interesting.

We already have:

```text
Customer
CustomerRepository
SQLAlchemy Session
MySQL
```

Now we'll connect them to:

```text
HTML Form
```

Create:

```text
app/routes/
```

and:

```text
app/routes/__init__.py
```

Leave it empty for now.

Create:

```text
app/routes/customer_routes.py
```

```python
from flask import Blueprint, render_template

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
```

---

# 11. Register the customer route

Update `app/web.py`:

```python
from flask import Flask, render_template

from app.routes.customer_routes import customer_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(customer_bp)

    @app.route("/")
    def home():
        return render_template("index.html")

    return app
```

Now Flask knows:

```text
/customers/
```

---

# 12. Create customer list template

Create:

```bash
mkdir -p app/templates/customers
```

Create:

```text
app/templates/customers/list.html
```

```html
{% extends "admin/base_admin.html" %}

{% block title %}
Customers
{% endblock %}

{% block content %}

<h2>Customers</h2>

<a href="/customers/create">
    Add Customer
</a>

<table>

    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Created At</th>
        </tr>
    </thead>

    <tbody>

        {% for customer in customers %}

        <tr>
            <td>{{ customer.id }}</td>
            <td>{{ customer.name }}</td>
            <td>{{ customer.email }}</td>
            <td>{{ customer.created_at }}</td>
        </tr>

        {% else %}

        <tr>
            <td colspan="4">
                No customers found.
            </td>
        </tr>

        {% endfor %}

    </tbody>

</table>

{% endblock %}
```

---

# 13. Test the customer page

Start:

```bash
python -m app.run
```

Open:

```text
http://127.0.0.1:5000/customers/
```

If you already inserted the customer:

```text
Bhupendra
bhupendra@example.com
```

you should see it in the browser.

The complete flow is now:

```text
Browser
   │
   │ GET /customers/
   ▼
Flask Route
   │
   ▼
CustomerRepository
   │
   ▼
SQLAlchemy Session
   │
   ▼
MySQL
   │
   ▼
Customer objects
   │
   ▼
Jinja Template
   │
   ▼
HTML
   │
   ▼
Browser
```

This is exactly why I recommended adding the web interface at this stage.

---

# Important architecture rule

Notice that the route does **not** contain SQL:

```python
customers = repository.get_all()
```

We don't do this:

```python
# DON'T do this in the route

session.execute(...)
```

Our layers remain:

```text
Route
  ↓
Service
  ↓
Repository
  ↓
SQLAlchemy
  ↓
MySQL
```

For simple listing, we can temporarily call the repository directly. For order creation, we'll definitely use the service layer because it contains business rules and the transaction.

---

## What we have completed

```text
✅ SQLAlchemy ORM
✅ MySQL
✅ Models
✅ Relationships
✅ Repository
✅ Session
✅ Timestamps
✅ Flask
✅ Jinja
✅ Base HTML layout
✅ CSS
✅ Customer listing
```

### Next step

We'll build the **Add Customer** form:

```text
Name:  [________________]
Email: [________________]

       [ Create Customer ]
```

and connect:

```text
HTML POST
   ↓
Flask
   ↓
CustomerRepository
   ↓
SQLAlchemy
   ↓
MySQL
```

Then we'll do the same for **Category + Product**, followed by the most important part: **Place Order from the browser with stock validation and a real database transaction**.
