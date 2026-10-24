# Lesson 07 — Part 8: Step 2 — Build the Storefront and Category Navigation

Now that your Flask secret key and authentication blueprint are configured, let's build the customer-facing storefront. We'll keep your existing admin pages intact and create a separate layout for customers.

Part 8 — Step 2

## 1. Create the storefront blueprint

Create `app/routes/storefront_routes.py`:

Python

Run

```
from flask import (
    Blueprint,
    abort,
    render_template,
)

from app.database import SessionLocal
from app.repositories.category_repository import CategoryRepository
from app.repositories.product_repository import ProductRepository

storefront_bp = Blueprint(
    "storefront",
    __name__,
    url_prefix="/store",
)


@storefront_bp.route("/")
def home():
    with SessionLocal() as session:
        category_repository = CategoryRepository(session)
        product_repository = ProductRepository(session)

        categories = category_repository.get_all()
        products = product_repository.get_all()

        return render_template(
            "storefront/home.html",
            categories=categories,
            products=products,
        )


@storefront_bp.route("/category/<int:category_id>")
def category_products(category_id):
    with SessionLocal() as session:
        category_repository = CategoryRepository(session)
        product_repository = ProductRepository(session)

        category = category_repository.get_by_id(category_id)

        if category is None:
            abort(404)

        products = product_repository.get_by_category(category_id)

        return render_template(
            "storefront/category.html",
            categories=category_repository.get_all(),
            category=category,
            products=products,
        )


@storefront_bp.route("/product/<int:product_id>")
def product_detail(product_id):
    with SessionLocal() as session:
        category_repository = CategoryRepository(session)
        product_repository = ProductRepository(session)

        product = product_repository.get_by_id(product_id)

        if product is None:
            abort(404)

        return render_template(
            "storefront/product_detail.html",
            categories=category_repository.get_all(),
            product=product,
        )
```

This uses your existing repositories. We'll add `get_by_category()` to `ProductRepository` next.


## 2. Add category filtering to ProductRepository

Open `app/repositories/product_repository.py` and add this method to your existing `ProductRepository` class:

Python

Run

```
def get_by_category(self, category_id: int):
    statement = (
        select(Product)
        .options(selectinload(Product.category))
        .where(Product.category_id == category_id)
        .order_by(Product.name)
    )
    return self.session.scalars(statement).all()
```

Also ensure your existing `get_by_id()` eagerly loads the category for product details:

Python

Run

```
def get_by_id(self, product_id: int):
    statement = (
        select(Product)
        .options(selectinload(Product.category))
        .where(Product.id == product_id)
    )
    return self.session.scalar(statement)
```

These methods use SQLAlchemy 2.x `select()` syntax, consistent with your existing repository pattern.

## 3. Register the storefront blueprint

Update `app/web.py` by importing and registering the new blueprint:

Python

Run

```
from app.routes.storefront_routes import storefront_bp
```

Inside `create_app()`, add:

Python

Run

```
app.register_blueprint(storefront_bp)
```

Your existing admin blueprints and home route can remain unchanged. The storefront will be available at `/store/`.

## 4. Create a separate storefront layout

Create `app/templates/storefront/base_store.html`:

HTML

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}My E-Commerce Store{% endblock %}</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f5f6f8;
            color: #222;
        }

        header {
            background: #172554;
            color: white;
            padding: 16px 5%;
        }

        .topbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 20px;
            flex-wrap: wrap;
        }

        .brand {
            color: white;
            font-size: 22px;
            font-weight: bold;
            text-decoration: none;
        }

        nav {
            display: flex;
            gap: 16px;
            align-items: center;
            flex-wrap: wrap;
        }

        nav a {
            color: white;
            text-decoration: none;
        }

        nav a:hover {
            text-decoration: underline;
        }

        .category-nav {
            background: white;
            padding: 14px 5%;
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            border-bottom: 1px solid #ddd;
        }

        .category-nav a {
            color: #172554;
            text-decoration: none;
        }

        main {
            max-width: 1200px;
            margin: 30px auto;
            padding: 0 20px;
        }

        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
            gap: 20px;
        }

        .product-card {
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            padding: 18px;
        }

        .product-card h3 {
            margin-top: 0;
        }

        .price {
            font-size: 18px;
            font-weight: bold;
            color: #15803d;
        }

        .button {
            display: inline-block;
            background: #1d4ed8;
            color: white;
            padding: 10px 14px;
            border: 0;
            border-radius: 6px;
            text-decoration: none;
            cursor: pointer;
        }

        .flash {
            padding: 12px;
            margin-bottom: 15px;
            border-radius: 6px;
            background: #e0f2fe;
        }

        .flash.error {
            background: #fee2e2;
            color: #991b1b;
        }

        .flash.success {
            background: #dcfce7;
            color: #166534;
        }

        footer {
            padding: 25px;
            text-align: center;
            color: #666;
        }
    </style>
</head>
<body>
    <header>
        <div class="topbar">
            <a class="brand" href="{{ url_for('storefront.home') }}">
                My Store
            </a>

            <nav>
                <a href="{{ url_for('storefront.home') }}">Home</a>

                {% if session.get('customer_id') %}
                    <span>
                        Welcome, {{ session.get('customer_name', 'Customer') }}
                    </span>

                    <a href="{{ url_for('cart.view_cart') }}">Cart</a>

                    <form method="POST"
                          action="{{ url_for('auth.logout') }}">
                        <button type="submit">Logout</button>
                    </form>
                {% else %}
                    <a href="{{ url_for('auth.login') }}">Login</a>
                    <a href="{{ url_for('auth.register') }}">Register</a>
                {% endif %}
            </nav>
        </div>
    </header>

    <div class="category-nav">
        <a href="{{ url_for('storefront.home') }}">All Products</a>

        {% for category in categories|default([]) %}
            <a href="{{ url_for(
                'storefront.category_products',
                category_id=category.id
            ) }}">
                {{ category.name }}
            </a>
        {% endfor %}
    </div>

    <main>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% for category, message in messages %}
                <div class="flash {{ category }}">{{ message }}</div>
            {% endfor %}
        {% endwith %}

        {% block content %}{% endblock %}
    </main>

    <footer>
        My E-Commerce Store
    </footer>
</body>
</html>
```

The cart link assumes the planned `cart.view_cart` endpoint, which we'll implement later in Part 8. Until then, you can temporarily remove that link or add the cart blueprint when it is ready.


## 5. Create the storefront home page

Create `app/templates/storefront/home.html`:

HTML

```
{% extends "storefront/base_store.html" %}

{% block title %}Home | My Store{% endblock %}

{% block content %}
<section>
    <h1>Welcome to My Store</h1>
    <p>Browse our categories and discover our products.</p>
</section>

<section>
    <h2>Shop by Category</h2>

    <div class="product-grid">
        {% for category in categories %}
            <div class="product-card">
                <h3>{{ category.name }}</h3>
                <p>{{ category.description or "Explore our products." }}</p>

                <a class="button"
                   href="{{ url_for(
                       'storefront.category_products',
                       category_id=category.id
                   ) }}">
                    View Products
                </a>
            </div>
        {% else %}
            <p>No categories available.</p>
        {% endfor %}
    </div>
</section>

<section>
    <h2>All Products</h2>

    <div class="product-grid">
        {% for product in products %}
            <div class="product-card">
                <h3>{{ product.name }}</h3>

                <p>{{ product.description or "" }}</p>

                <p class="price">₹{{ "%.2f"|format(product.price) }}</p>

                <p>
                    Category:
                    {{ product.category.name if product.category else "Uncategorized" }}
                </p>

                <a class="button"
                   href="{{ url_for(
                       'storefront.product_detail',
                       product_id=product.id
                   ) }}">
                    View Details
                </a>
            </div>
        {% else %}
            <p>No products available.</p>
        {% endfor %}
    </div>
</section>
{% endblock %}
```

## 6. Create the category product page

Create `app/templates/storefront/category.html`:

HTML

```
{% extends "storefront/base_store.html" %}

{% block title %}{{ category.name }} | My Store{% endblock %}

{% block content %}
<h1>{{ category.name }}</h1>

<p>{{ category.description or "Browse products in this category." }}</p>

<div class="product-grid">
    {% for product in products %}
        <div class="product-card">
            <h3>{{ product.name }}</h3>

            <p>{{ product.description or "" }}</p>

            <p class="price">₹{{ "%.2f"|format(product.price) }}</p>

            <p>
                {% if product.stock > 0 %}
                    <span>In stock: {{ product.stock }}</span>
                {% else %}
                    <span>Out of stock</span>
                {% endif %}
            </p>

            <a class="button"
               href="{{ url_for(
                   'storefront.product_detail',
                   product_id=product.id
               ) }}">
                View Details
            </a>
        </div>
    {% else %}
        <p>No products found in this category.</p>
    {% endfor %}
</div>
{% endblock %}
```

## 7. Create the product detail page

Create `app/templates/storefront/product_detail.html`:

HTML

```
{% extends "storefront/base_store.html" %}

{% block title %}{{ product.name }} | My Store{% endblock %}

{% block content %}
<div class="product-card">
    <h1>{{ product.name }}</h1>

    <p>{{ product.description or "No description available." }}</p>

    <p>
        Category:
        {% if product.category %}
            <a href="{{ url_for(
                'storefront.category_products',
                category_id=product.category.id
            ) }}">
                {{ product.category.name }}
            </a>
        {% else %}
            Uncategorized
        {% endif %}
    </p>

    <p class="price">₹{{ "%.2f"|format(product.price) }}</p>

    <p>
        {% if product.stock > 0 %}
            Available stock: {{ product.stock }}
        {% else %}
            Out of stock
        {% endif %}
    </p>

    {% if product.stock > 0 %}
        <p>Shopping cart functionality will be connected in the next step.</p>
    {% endif %}

    <a href="{{ url_for('storefront.home') }}">Continue Shopping</a>
</div>
{% endblock %}
```

## 8. Test the storefront

Start your Flask application using your existing run command, then visit:

* `http://127.0.0.1:5000/store/` — storefront home page

* `http://127.0.0.1:5000/store/category/1` — products in category ID 1

* `http://127.0.0.1:5000/store/product/1` — product detail for product ID 1

* `http://127.0.0.1:5000/register` — customer registration

* `http://127.0.0.1:5000/login` — customer login

## Step 2 completion checklist

0 of 6 verified

Storefront blueprint registered successfully

Home page displays categories and products

Category navigation opens the correct product listing

Product details display price, stock and category name

Admin pages still work independently

Storefront links to login and registration

Next: Step 3 — Customer registration and login integration.

Before moving on, verify the storefront renders correctly and your existing admin pages remain functional. One detail to check: your `Product` model must have `price`, `stock`, `category_id` and the `category` relationship as used in these templates.
