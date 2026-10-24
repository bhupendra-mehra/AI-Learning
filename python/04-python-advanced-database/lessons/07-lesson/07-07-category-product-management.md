# Lesson 07 — Part 7: Category and Product Management with Flask, HTML and SQLAlchemy

In this part, we'll extend your e-commerce application by adding category and product forms, following the same Flask, repository, SQLAlchemy and Jinja template structure used for customer management.

Practical lesson

CRUD operations

## 1. What we'll build

* Category management: Create, list, edit and delete product categories.

* Product management: Create, list, edit and delete products.

* Database relationships: Associate each product with a category using SQLAlchemy.

* Form validation: Validate required fields, prices, stock and category selection.

* Reusable templates: Follow the shared create/edit form approach from Part 6.


## 2. Expected project structure

Add the following files to your existing `app/` directory:

```
app/
├── repositories/
│   ├── category_repository.py
│   └── product_repository.py
├── routes/
│   ├── category_routes.py
│   └── product_routes.py
└── templates/
    ├── categories/
    │   ├── list.html
    │   └── category_form.html
    └── products/
        ├── list.html
        └── product_form.html
```

We'll assume your existing models have these fields:

|
Model

|

Fields

|
| --- | --- |
|

`Category`

|

`id`, `name`, `description`, `products`

|
|

`Product`

|

`id`, `name`, `description`, `price`, `stock`, `category_id`, `category`

|

If your model uses different field names, adjust the examples accordingly.

## 3. Category repository

Create `app/repositories/category_repository.py`:

Python

Run

```
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.category import Category


class CategoryRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = select(Category).order_by(Category.name)
        return self.session.scalars(statement).all()

    def get_by_id(self, category_id: int):
        return self.session.get(Category, category_id)

    def get_by_name(self, name: str):
        statement = select(Category).where(Category.name == name)
        return self.session.scalar(statement)

    def create(self, name: str, description: str | None = None):
        category = Category(
            name=name,
            description=description,
        )
        self.session.add(category)
        self.session.flush()
        return category

    def update(
        self,
        category: Category,
        name: str,
        description: str | None = None,
    ):
        category.name = name
        category.description = description
        self.session.flush()
        return category

    def delete(self, category: Category):
        self.session.delete(category)
        self.session.flush()
```

Important: The repository does not commit transactions. The route handles `commit()` and `rollback()`, keeping transaction control in one place.

## 4. Category routes

Create `app/routes/category_routes.py`:

Python

Run

```
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
from app.repositories.category_repository import CategoryRepository

category_bp = Blueprint(
    "categories",
    __name__,
    url_prefix="/categories",
)


@category_bp.route("/")
def list_categories():
    with SessionLocal() as session:
        repository = CategoryRepository(session)
        categories = repository.get_all()

        return render_template(
            "categories/list.html",
            categories=categories,
        )


def save_category(category=None):
    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip() or None

    if not name:
        flash("Category name is required.", "error")
        return render_template(
            "categories/category_form.html",
            category=category,
        )

    with SessionLocal() as session:
        repository = CategoryRepository(session)

        existing = repository.get_by_name(name)

        if existing and (
            category is None or existing.id != category.id
        ):
            flash("A category with this name already exists.", "error")
            return render_template(
                "categories/category_form.html",
                category=category,
            )

        try:
            if category is None:
                repository.create(name, description)
                action = "created"
            else:
                # Reload the model in this session before updating.
                current_category = repository.get_by_id(category.id)

                if current_category is None:
                    abort(404)

                repository.update(
                    current_category,
                    name,
                    description,
                )
                action = "updated"

            session.commit()
            flash(f"Category {name} {action} successfully.", "success")

        except IntegrityError:
            session.rollback()
            flash("Unable to save category. Check for duplicate values.", "error")
            return render_template(
                "categories/category_form.html",
                category=category,
            )

    return redirect(url_for("categories.list_categories"))


@category_bp.route("/create", methods=["GET", "POST"])
def create_category():
    if request.method == "POST":
        return save_category()

    return render_template(
        "categories/category_form.html",
        category=None,
    )


@category_bp.route("/<int:category_id>/edit", methods=["GET", "POST"])
def edit_category(category_id):
    with SessionLocal() as session:
        repository = CategoryRepository(session)
        category = repository.get_by_id(category_id)

        if category is None:
            abort(404)

        if request.method == "GET":
            return render_template(
                "categories/category_form.html",
                category=category,
            )

        # Pass the ID, then reload the model in the save session.
        category_id_for_save = category.id

    class CategoryReference:
        id = category_id_for_save

    return save_category(category=CategoryReference())


@category_bp.route("/<int:category_id>/delete", methods=["POST"])
def delete_category(category_id):
    with SessionLocal() as session:
        repository = CategoryRepository(session)
        category = repository.get_by_id(category_id)

        if category is None:
            abort(404)

        if category.products:
            flash(
                "This category has products. Reassign or remove them before deleting it.",
                "error",
            )
            return redirect(url_for("categories.list_categories"))

        try:
            repository.delete(category)
            session.commit()
            flash("Category deleted successfully.", "success")
        except IntegrityError:
            session.rollback()
            flash("Unable to delete this category because it is in use.", "error")

    return redirect(url_for("categories.list_categories"))
```

A small design improvement for the edit route

The example above demonstrates the CRUD flow, but the `CategoryReference` workaround is unnecessary. A cleaner implementation is to make `save_category()` accept a `category_id` and load the category within its own session. This avoids passing an ORM object between sessions.

Replace the helper signature and edit branch with:

Python

Run

```
def save_category(category_id=None):
    # Read and validate form values here.

    with SessionLocal() as session:
        repository = CategoryRepository(session)
        category = (
            repository.get_by_id(category_id)
            if category_id is not None
            else None
        )

        if category_id is not None and category is None:
            abort(404)

        # Perform duplicate check, create/update, commit.
```

Then call `save_category(category_id)` from the edit route. Use this pattern in your implementation.

## 5. Shared category form

Create `app/templates/categories/category_form.html`:

HTML

```
{% extends "admin/base_admin.html" %}

{% block content %}
<h2>
    {{ "Edit Category" if category else "Add Category" }}
</h2>

<form method="POST"
      action="{{
          url_for('categories.edit_category', category_id=category.id)
          if category else url_for('categories.create_category')
      }}">

    <div>
        <label for="name">Category Name</label>
        <input
            type="text"
            id="name"
            name="name"
            value="{{ request.form.get('name', category.name if category else '') }}"
            required
        >
    </div>

    <div>
        <label for="description">Description</label>
        <textarea id="description" name="description">{{ request.form.get('description', category.description if category else '') }}</textarea>
    </div>

    <button type="submit">
        {{ "Update Category" if category else "Create Category" }}
    </button>

    <a href="{{ url_for('categories.list_categories') }}">Cancel</a>
</form>
{% endblock %}
```

## 6. Category list template

Create `app/templates/categories/list.html`:

HTML

```
{% extends "admin/base_admin.html" %}

{% block content %}
<h2>Categories</h2>

<a href="{{ url_for('categories.create_category') }}">
    Add Category
</a>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Description</th>
            <th>Products</th>
            <th>Actions</th>
        </tr>
    </thead>

    <tbody>
        {% for category in categories %}
        <tr>
            <td>{{ category.id }}</td>
            <td>{{ category.name }}</td>
            <td>{{ category.description or "-" }}</td>
            <td>{{ category.products|length }}</td>
            <td>
                <a href="{{ url_for('categories.edit_category', category_id=category.id) }}">
                    Edit
                </a>

                <form
                    method="POST"
                    action="{{ url_for('categories.delete_category', category_id=category.id) }}"
                    onsubmit="return confirm('Delete this category?');"
                    style="display:inline"
                >
                    <button type="submit">Delete</button>
                </form>
            </td>
        </tr>
        {% else %}
        <tr>
            <td colspan="5">No categories found.</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

## 7. Register the category blueprint

In `app/web.py`, import and register the new blueprint:

Python

Run

```
from app.routes.category_routes import category_bp

app.register_blueprint(category_bp)
```

Add a link to your existing `base.html` navigation:

HTML

```
<a href="{{ url_for('categories.list_categories') }}">
    Categories
</a>
```

## 8. Product management

The product CRUD flow will use the same pattern, with additional validation for price, stock and category.

### Product repository

Create `app/repositories/product_repository.py`:

Python

Run

```
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = select(Product).order_by(Product.id.desc())
        return self.session.scalars(statement).all()

    def get_by_id(self, product_id: int):
        return self.session.get(Product, product_id)

    def create(
        self,
        name: str,
        description: str | None,
        price,
        stock: int,
        category_id: int,
    ):
        product = Product(
            name=name,
            description=description,
            price=price,
            stock=stock,
            category_id=category_id,
        )
        self.session.add(product)
        self.session.flush()
        return product

    def update(self, product: Product, **values):
        for field, value in values.items():
            setattr(product, field, value)

        self.session.flush()
        return product

    def delete(self, product: Product):
        self.session.delete(product)
        self.session.flush()
```

### Product form validation

When processing a product form, validate values before creating or updating the product:

Python

Run

```
from decimal import Decimal, InvalidOperation

name = request.form.get("name", "").strip()
description = request.form.get("description", "").strip() or None

try:
    price = Decimal(request.form.get("price", ""))
    if not price.is_finite() or price < 0:
        raise ValueError("Price must be a non-negative number.")
except (InvalidOperation, ValueError):
    flash("Enter a valid non-negative price.", "error")
    # Re-render the product form here.

try:
    stock = int(request.form.get("stock", ""))
    if stock < 0:
        raise ValueError("Stock cannot be negative.")
except ValueError:
    flash("Enter a valid non-negative stock quantity.", "error")
    # Re-render the product form here.

try:
    category_id = int(request.form.get("category_id", ""))
except ValueError:
    flash("Select a valid category.", "error")
    # Re-render the product form here.
```

Also check that the selected category exists:

Python

Run

```
category = category_repository.get_by_id(category_id)

if category is None:
    flash("Selected category does not exist.", "error")
    # Re-render the product form here.
```

Use `Decimal` rather than `float` for monetary values. Confirm that your `Product.price` column uses SQLAlchemy `Numeric`, and that your database schema supports the desired precision.

## 9. Product form fields

Your `product_form.html` should include:

HTML

```
<div>
    <label for="name">Product Name</label>
    <input type="text" id="name" name="name" required>
</div>

<div>
    <label for="description">Description</label>
    <textarea id="description" name="description"></textarea>
</div>

<div>
    <label for="price">Price</label>
    <input type="number" id="price" name="price"
           min="0" step="0.01" required>
</div>

<div>
    <label for="stock">Stock</label>
    <input type="number" id="stock" name="stock"
           min="0" step="1" required>
</div>

<div>
    <label for="category_id">Category</label>
    <select id="category_id" name="category_id" required>
        <option value="">Select Category</option>
        {% for category in categories %}
            <option value="{{ category.id }}"
                {% if product and product.category_id == category.id %}
                    selected
                {% endif %}
            >
                {{ category.name }}
            </option>
        {% endfor %}
    </select>
</div>

<button type="submit">
    {{ "Update Product" if product else "Create Product" }}
</button>
```

Populate `categories` from `CategoryRepository.get_all()` in both the GET and validation-error paths. Populate `product` with the existing product for edits, or `None` for creation.

## 10. Testing checklist

Part 7 progress

0/9 complete

Start the Flask application and open /categories/.

Create a category and verify it appears in the list.

Edit the category and verify the changes persist.

Try creating a duplicate category and confirm validation.

Try deleting a category that has products and confirm deletion is blocked.

Create a product with a valid category, price and stock.

Edit the product and change its category.

Delete a product and verify it is removed.

Verify the product-category relationship in the database.

Database verification:

SQL

```
SELECT id, name, description
FROM categories
ORDER BY id DESC;

SELECT
    p.id,
    p.name,
    p.price,
    p.stock,
    c.name AS category_name
FROM products p
JOIN categories c ON c.id = p.category_id
ORDER BY p.id DESC;
```

Before using this in production

* Protect create, edit and delete routes with authentication and authorization.

* Add CSRF protection to POST forms.

* Ensure database constraints enforce category and product integrity.

* Avoid deleting products referenced by historical order items; use deactivation or soft deletion where appropriate.

* Use Alembic migrations for schema changes. `Base.metadata.create_all()` does not update existing tables.

Suggested next step: Implement and test category CRUD first, then complete product CRUD using the same shared-form and repository patterns. This keeps the work manageable and makes it easier to isolate errors before moving on to the next lesson.
