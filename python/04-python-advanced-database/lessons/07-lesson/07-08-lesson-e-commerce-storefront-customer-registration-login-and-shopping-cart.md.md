# Lesson 07 — Part 8: E-Commerce Storefront, Customer Registration, Login and Shopping Cart

Next development phase

Flask + SQLAlchemy + HTML/Jinja

Your backend CRUD for customers, categories and products is working. Now we'll build the customer-facing storefront, where customers can browse categories, view products, register, log in and add products to their cart.

We'll complete this part before moving on to checkout and order placement, as requested.

## Part 8 — Scope

1. Storefront and category navigation

   Display a customer-facing home page with category menus and product listings.

2. Category-wise product pages

   Clicking a category displays its products, with product details and prices.

3. Customer registration

   New customers register with their name, email and password. Save their account securely in the existing customers table.

4. Customer login and logout

   Authenticate existing customers, maintain their login session and provide logout functionality.

5. Shopping cart

   Allow customers to add products, view their cart, update quantities and remove items. Require login before adding items to the cart.

6. Authentication and cart integration

   Redirect unauthenticated customers to login or registration, then return them to the storefront or cart.

Not included in Part 8

* Checkout and shipping details

* Order creation and order-item persistence

* Payment integration

* Order confirmation and order history

## 1. Customer shopping journey

Storefront

Browse categories and featured products

Select a category

View products belonging to the selected category

View product and add to cart

Check product details, price and availability

Already logged in

Add product to cart

Not logged in

Register or log in, then continue

Shopping cart

Review products, change quantities and remove items

Part 8 ends here. Checkout and order placement will be Part 9.


## 2. Updated project structure

We'll add a separate storefront and authentication layer, keeping your existing admin CRUD and database repositories intact.

```
app/
├── models/
│   ├── customer.py
│   ├── category.py
│   └── product.py
├── repositories/
│   ├── customer_repository.py
│   ├── category_repository.py
│   └── product_repository.py
├── routes/
│   ├── customer_routes.py       # Existing customer management
│   ├── category_routes.py       # Existing category management
│   ├── product_routes.py        # Existing product management
│   ├── storefront_routes.py     # New storefront
│   ├── auth_routes.py           # New registration/login/logout
│   └── cart_routes.py           # New cart functionality
├── services/
│   └── cart_service.py          # Cart operations
├── templates/
│   ├── base.html                # Existing admin layout
│   ├── admin/                   # Existing management pages
│   ├── storefront/
│   │   ├── home.html
│   │   ├── category.html
│   │   └── product_detail.html
│   ├── auth/
│   │   ├── register.html
│   │   └── login.html
│   └── cart/
│       └── view.html
└── web.py
```

We'll keep the admin and storefront layouts separate so customer-facing navigation and styling don't interfere with your existing management pages.

## 3. Database change: customer authentication

Your existing `customers` table contains customer details. To support registration and login, we'll add a `password_hash` column rather than storing plain-text passwords.

Run this SQL against your existing database:

SQL

```
ALTER TABLE customers
ADD COLUMN password_hash VARCHAR(255) NULL;
```

The column is nullable initially to preserve existing customer records that were created through the admin interface. New registrations will require a password.

Update `app/models/customer.py` by adding:

Python

Run

```
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

# Inside your existing Customer model:

password_hash: Mapped[str | None] = mapped_column(
    String(255),
    nullable=True,
)
```

Keep all your existing fields, relationships and `TimestampMixin` unchanged.

Security rule

We'll use Werkzeug's password hashing functions to store only password hashes. We won't store, log or display users' raw passwords. Existing admin-created customers without a password will need to register or have an account password set through a separate secure process before they can log in.

## 4. Authentication foundation

We'll use Flask's signed session mechanism for customer login, with the customer ID stored in the session. The secret key must be configured using an environment variable.

In your `.env` file:

dotenv

```
SECRET_KEY=replace_with_a_long_random_secret
```

In your Flask application configuration, load it from the environment rather than hardcoding it:

Python

Run

```
import os

app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
```

For the authentication routes, we'll use:

Python

Run

```
from werkzeug.security import generate_password_hash, check_password_hash
```

* `generate_password_hash(password)` when registering a customer.

* `check_password_hash(customer.password_hash, password)` when logging in.

* `session["customer_id"] = customer.id` after successful authentication.

* `session.clear()` when logging out.

The storefront will distinguish between the authenticated customer session and the existing admin CRUD interface. We'll add authorization checks to ensure customers cannot access administrative operations.


## 5. Storefront pages and routes

These are the planned routes for Part 8.

|
Method

|

Route

|

Purpose

|
| --- | --- | --- |
|

GET

|

`/store/`

|

Storefront home page

|
|

GET

|

`/store/category/<id>`

|

Products in a category

|
|

GET

|

`/store/product/<id>`

|

Product details

|
|

GET, POST

|

`/register`

|

Customer registration

|
|

GET, POST

|

`/login`

|

Customer login

|
|

POST

|

`/logout`

|

Customer logout

|
|

GET

|

`/cart/`

|

View shopping cart

|
|

POST

|

`/cart/add/<id>`

|

Add product to cart

|
|

POST

|

`/cart/update/<id>`

|

Update quantity

|
|

POST

|

`/cart/remove/<id>`

|

Remove cart item

|

We'll use the existing category and product repositories to retrieve storefront data, rather than duplicating database queries in the routes.

## 6. Shopping cart design

For this learning project, we'll initially store the cart in the Flask session. That lets us implement the complete shopping experience without introducing a new cart database table yet.

Example cart data:

Python

Run

```
{
    "1": 2,
    "3": 1,
    "5": 4
}
```

The keys represent product IDs and the values represent quantities.

## Example shopping cart

![Studio shot of silver laptop.](https://images.openai.com/static-rsc-4/BC_TJEdUmj1BBI2UDjwEEiauNlmfsV2cg9-qaZ_5y1ettmDxyO1mQ0lSzOeIaFSQZsX-zyLoXkUpshsaOj4g9SBHDWp0g-VBhhm5qs-0aJYpXSlVkVX-LWmeGkvdpEPP9c4uoK_RK9y-khDtPX-KN9ZJ0FioQ643HeIsV35_xUX79Lp201sZZI-xT0zxK-gq?purpose=inline)

Laptop

₹50,000 × 1

₹50,000

![Computer mouse on a white background](https://images.openai.com/static-rsc-4/DBiBAzqEj52GrsnkYjtKVEFgHTNmm8S0wdSO8_0onc_sqtuJC-nzpbj69yIrSLeeezjohn9mCbvQL3CXCSiT5GkYGaAHrvQ1KK2CzydOThPIGBtps20xEHU-jlWmKGoHy5QKQq2t31b3ECKApaxWNAKSVbXQqtkhM-vW22IRhJb8b5SD_2B-ogHPxzBuUNOI?purpose=inline)

Wireless Mouse

₹800 × 2

₹1,600

Cart total

# ₹51,600

Illustrative storefront example, not actual product data from your database.

When a customer adds a product, the application will:

1. Check whether the customer is logged in.

2. If not logged in, redirect them to the login page, with an option to register.

3. After successful login or registration, return them to the intended storefront action.

4. Verify the product exists and is available.

5. Add or increment the product quantity in the cart.

6. Display the updated cart.

We'll retrieve current product prices from the database when rendering the cart. This prevents customers from manipulating prices through session data. Stock will be checked again during checkout in Part 9.

## 7. Implementation order

1. Start here

   Step 1 — Authentication and customer accounts

   Add the password hash column, registration, login, logout and authentication helpers.

2. Step 2 — Storefront layout

   Build a customer-facing base template with navigation, category menu, login status and cart link.

3. Step 3 — Category and product browsing

   Create the home page, category pages and product detail pages using the existing models and repositories.

4. Step 4 — Shopping cart

   Implement add, view, update and remove operations, with login required for cart actions.

5. Step 5 — Integration and testing

   Test new registration, existing customer login, logout, category navigation, product browsing and cart behavior.

## 8. Part 8 completion criteria

By the end of this part, your application should support the following complete flow:

Target outcome

A new customer visits the storefront, browses categories and products, registers an account, logs in, adds products to the cart, changes quantities and removes items. An existing customer can log in and do the same. The cart remains available while the customer navigates the storefront.

Let's begin with Step 1: customer authentication. First, apply the `password_hash` schema change and model update above. Then implement the registration and login routes using your existing `CustomerRepository`. This builds on your current database architecture without disturbing the working customer, category and product management features.
