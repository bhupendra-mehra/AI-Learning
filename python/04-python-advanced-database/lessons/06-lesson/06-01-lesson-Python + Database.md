# Lesson 06 — Python + Database

Now we connect the two areas we've been learning separately:

```text
Python
   ↓
Database Driver
   ↓
SQL
   ↓
MySQL / PostgreSQL
   ↓
Query Result
   ↓
Python
```

This is a major step because we're moving from **writing Python programs and SQL queries independently** to building real backend applications.

---

# 1. What We'll Learn

In this lesson:

```text
01. Database drivers
02. Database connection
03. Executing SQL from Python
04. Parameterized queries
05. Fetching results
06. INSERT / UPDATE / DELETE
07. Transactions
08. Commit / Rollback
09. Error handling
10. Logging
11. Connection management
12. Practical e-commerce project
```

We'll use **MySQL** because it aligns well with your Magento experience.

---

# 2. Why Does Python Need a Database Driver?

Python doesn't directly know how to communicate with MySQL.

We need a **database driver**.

Conceptually:

```text
Python Application
       ↓
MySQL Driver
       ↓
MySQL Protocol
       ↓
MySQL Server
```

Popular Python MySQL libraries include:

```text
mysql-connector-python
PyMySQL
SQLAlchemy
```

For this lesson, we'll first learn the lower-level approach with:

```text
mysql-connector-python
```

Later, in **Lesson 07**, we'll use:

```text
SQLAlchemy
```

and learn ORM.

---

# 3. Installing the Driver

Inside your virtual environment:

```bash
pip install mysql-connector-python
```

Check:

```bash
pip show mysql-connector-python
```

You can save the dependency:

```bash
pip freeze > requirements.txt
```

---

# 4. Importing the Driver

```python
import mysql.connector
```

Now Python can communicate with MySQL.

---

# 5. Connecting to MySQL

Basic connection:

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="ecommerce"
)

print("Connected successfully")
```

Conceptually:

```text
host
 ↓
Which server?

user
 ↓
Who are we?

password
 ↓
Authentication

database
 ↓
Which database?
```

---

# 6. Don't Hardcode Credentials

This is important.

Avoid:

```python
password="mypassword123"
```

inside source code.

Why?

Because source code may be:

```text
committed to Git
shared with teammates
uploaded to GitHub
copied into logs
```

Instead use environment variables.

---

# 7. Environment Variables

Example `.env`:

```text
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ecommerce
DB_USER=root
DB_PASSWORD=secret
```

Install:

```bash
pip install python-dotenv
```

Then:

```python
import os

from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
```

Now credentials aren't directly embedded in Python code.

---

# 8. Never Commit `.env`

Add to `.gitignore`:

```text
.env
```

You can commit:

```text
.env.example
```

Example:

```text
DB_HOST=
DB_PORT=3306
DB_NAME=
DB_USER=
DB_PASSWORD=
```

This tells another developer which configuration values are required without exposing your secrets.

---

# 9. Creating a Connection Function

Instead of connecting everywhere:

```python
import os
import mysql.connector

from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
```

Now:

```python
connection = get_connection()
```

This is cleaner and reusable.

---

# 10. Creating a Cursor

A **cursor** allows Python to execute SQL.

```python
connection = get_connection()

cursor = connection.cursor()

cursor.execute(
    "SELECT * FROM products"
)
```

Think:

```text
Connection
     ↓
Cursor
     ↓
SQL
     ↓
Database
```

---

# 11. Fetching Results

After executing:

```python
cursor.execute(
    "SELECT * FROM products"
)
```

fetch all rows:

```python
products = cursor.fetchall()

for product in products:
    print(product)
```

Example result:

```text
(101, 2, 'Laptop', 60000.00)
(102, 3, 'Mouse', 2000.00)
(103, 3, 'Keyboard', 3000.00)
```

---

# 12. fetchone()

If you only need one record:

```python
cursor.execute(
    "SELECT * FROM products WHERE id = 101"
)

product = cursor.fetchone()

print(product)
```

Result:

```text
(101, 2, 'Laptop', 60000.00)
```

---

# 13. fetchmany()

You can also fetch a limited number of rows:

```python
rows = cursor.fetchmany(10)
```

This can be useful when processing results in batches.

---

# 14. Selecting Specific Columns

Prefer:

```python
cursor.execute(
    """
    SELECT id, name, price
    FROM products
    """
)

products = cursor.fetchall()
```

rather than:

```python
SELECT *
```

when you know exactly what your application needs.

This reduces unnecessary data transfer and makes the code more explicit.

---

# 15. Parameterized Queries

This is **extremely important**.

Never construct SQL like this:

```python
product_id = 101

query = f"""
SELECT *
FROM products
WHERE id = {product_id}
"""

cursor.execute(query)
```

It can become unsafe when values originate from users or other external sources.

Instead:

```python
product_id = 101

query = """
SELECT id, name, price
FROM products
WHERE id = %s
"""

cursor.execute(query, (product_id,))
```

The driver safely handles the parameter.

---

# 16. SQL Injection

Imagine a login query constructed like:

```python
query = f"""
SELECT *
FROM users
WHERE email = '{email}'
AND password = '{password}'
"""
```

If an attacker manipulates the input, they may alter the SQL statement.

This is called:

> **SQL Injection**

Parameterized queries help prevent this class of vulnerability.

Remember:

```text
❌ String concatenation
❌ f-string SQL values

✅ Parameterized queries
```

---

# 17. Multiple Parameters

Example:

```python
query = """
SELECT *
FROM products
WHERE category_id = %s
AND price > %s
"""

cursor.execute(
    query,
    (3, 5000)
)
```

This means:

```text
category_id = 3
price > 5000
```

---

# 18. INSERT from Python

Suppose we want to create a product.

```python
query = """
INSERT INTO products
(category_id, sku, name, price, stock_quantity, created_at, updated_at)
VALUES (%s, %s, %s, %s, %s, NOW(), NOW())
"""

values = (
    3,
    "USB001",
    "USB Cable",
    500.00,
    100
)

cursor.execute(query, values)

connection.commit()
```

The important part:

```python
connection.commit()
```

---

# 19. Why commit()?

Database modifications normally occur inside a transaction.

For:

```text
INSERT
UPDATE
DELETE
```

you need to commit if you want the transaction persisted.

Think:

```text
Python
   ↓
INSERT
   ↓
Transaction
   ↓
COMMIT
   ↓
Data persisted
```

Without the commit, the change may not be persisted depending on the driver's transaction behavior.

---

# 20. UPDATE from Python

```python
query = """
UPDATE products
SET price = %s
WHERE id = %s
"""

values = (
    65000,
    101
)

cursor.execute(query, values)

connection.commit()
```

---

# 21. DELETE from Python

```python
query = """
DELETE FROM products
WHERE id = %s
"""

cursor.execute(
    query,
    (104,)
)

connection.commit()
```

Again:

**Be extremely careful with DELETE queries.**

---

# 22. rowcount

After an operation:

```python
print(cursor.rowcount)
```

For example:

```text
1
```

means one row was affected.

This is useful for validating application behavior.

Example:

```python
cursor.execute(
    query,
    (65000, 101)
)

if cursor.rowcount == 0:
    print("Product not found")
else:
    connection.commit()
```

---

# 23. Transactions

Now let's revisit the transaction concept from Lesson 01.

Suppose placing an order requires:

```text
1. Create order
2. Create order items
3. Reduce inventory
4. Create payment record
```

We don't want:

```text
Create order       ✅
Create items       ✅
Reduce inventory   ❌
Payment            ❌
```

Instead:

```text
BEGIN
  ↓
Create order
  ↓
Create items
  ↓
Update inventory
  ↓
Create payment
  ↓
COMMIT
```

If something fails:

```text
ROLLBACK
```

---

# 24. Python Transaction Example

```python
try:
    cursor.execute(order_query, order_values)

    cursor.execute(item_query, item_values)

    cursor.execute(stock_query, stock_values)

    connection.commit()

except Exception:
    connection.rollback()
    raise
```

This is a fundamental backend pattern.

---

# 25. Why Rollback?

Suppose:

```text
Order created
Order item created
Inventory update failed
```

Without rollback:

```text
Database
----------------
Order exists       ❌ incomplete
Order item exists  ❌ incomplete
Inventory unchanged
```

With rollback:

```text
Database
----------------
Previous state restored
```

This helps preserve data consistency.

---

# 26. Error Handling

Database operations can fail for many reasons:

```text
Connection failure
Invalid SQL
Duplicate SKU
Foreign key violation
Timeout
Deadlock
Constraint violation
Network failure
```

Use exception handling:

```python
try:
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM products"
    )

except mysql.connector.Error as error:
    print(f"Database error: {error}")

finally:
    cursor.close()
    connection.close()
```

But there's an issue here.

If connection creation fails, `cursor` may not exist.

A production implementation should manage resources more carefully.

---

# 27. Resource Management

You should always release:

```text
cursor
connection
```

Otherwise, long-running applications can exhaust database connections.

A basic pattern:

```python
connection = None
cursor = None

try:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name FROM products"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

except mysql.connector.Error as error:
    print(f"Database error: {error}")

finally:
    if cursor:
        cursor.close()

    if connection:
        connection.close()
```

Later, SQLAlchemy will make connection/session management much cleaner.

---

# 28. Logging

You already learned Python logging in **Advanced Python Lesson 07**.

Use it here.

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Connecting to database")
logger.info("Fetching products")
logger.error("Database operation failed")
```

Never log passwords or database credentials.

Bad:

```python
logger.info("DB password: %s", password)
```

Never do this.

---

# 29. Returning Dictionaries

By default, results may look like:

```text
(101, 'Laptop', 60000)
```

You can configure a dictionary cursor:

```python
cursor = connection.cursor(
    dictionary=True
)
```

Then:

```python
cursor.execute(
    "SELECT id, name, price FROM products"
)

products = cursor.fetchall()

for product in products:
    print(product["name"])
```

Result:

```text
Laptop
Mouse
Keyboard
```

This is often easier to work with in Python applications.

---

# 30. Connecting Python + Dataclass

Now we can combine concepts from Advanced Python.

We already learned:

```python
@dataclass
class Product:
    name: str
    price: float
    category: str
```

We can convert database rows into Python objects.

For example:

```python
from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float
```

Then:

```python
products = []

for row in rows:
    products.append(
        Product(
            id=row["id"],
            name=row["name"],
            price=float(row["price"])
        )
    )
```

Now:

```text
Database Row
     ↓
Python Dictionary
     ↓
Product Dataclass
```

This is an important bridge between **database data and application objects**.

---

# 31. A Better Project Structure

Let's create a small Python database application:

```text
ecommerce-db/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── connection.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── product.py
│   │
│   └── services/
│       ├── __init__.py
│       └── product_service.py
│
├── tests/
│   └── test_products.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

Notice we're reusing **Lesson 10 — Professional Project Structure**.

---

# 32. Connection Module

`database/connection.py`

```python
import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
```

---

# 33. Product Model

`models/product.py`

```python
from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float
```

---

# 34. Product Service

`services/product_service.py`

```python
from app.database.connection import get_connection
from app.models.product import Product


def get_products() -> list[Product]:

    connection = get_connection()

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT id, name, price
            FROM products
            """
        )

        rows = cursor.fetchall()

        return [
            Product(
                id=row["id"],
                name=row["name"],
                price=float(row["price"])
            )
            for row in rows
        ]

    finally:
        cursor.close()
        connection.close()
```

Notice how several things we've already learned come together:

```text
Type hints
Dataclass
Modules
Database connection
SQL
List comprehension
Exception-safe resource cleanup
```

---

# 35. Main Application

`main.py`

```python
from app.services.product_service import get_products


def main():
    products = get_products()

    for product in products:
        print(
            product.id,
            product.name,
            product.price
        )


if __name__ == "__main__":
    main()
```

Run:

```bash
python -m app.main
```

---

# 36. Why `python -m app.main`?

Our application is structured as a package:

```text
app/
├── main.py
├── models/
├── services/
└── database/
```

Using:

```bash
python -m app.main
```

runs the module within the package context.

This reduces import/path issues compared with arbitrarily executing files from inside nested directories.

---

# 37. Real-World Architecture

We're beginning to build this:

```text
             ┌─────────────┐
             │   Client    │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │ Application │
             │   Service   │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │   Database  │
             │    Driver   │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │    MySQL    │
             └─────────────┘
```

Later this evolves into:

```text
API
 ↓
Service Layer
 ↓
ORM
 ↓
Database
```

and eventually:

```text
API
 ↓
Business Logic
 ↓
Database
 ↓
Data Processing
 ↓
AI / ML / LLM
```

---

# 38. Where This Fits in Your AI Roadmap

This lesson may look like pure backend development, but it is actually important preparation for AI.

AI applications need data.

For example:

```text
E-commerce Database
        ↓
Python
        ↓
Data Extraction
        ↓
Data Cleaning
        ↓
Pandas
        ↓
Embeddings / ML / LLM
```

Later you'll use these same concepts for:

```text
RAG
AI Agents
AI Analytics
LLM applications
Magento AI integration
```

So we're not taking a detour.

We're building the data layer that AI applications depend on.

---

# 39. Practical Project — Product Repository

Let's build a small **Product Repository**.

It should support:

```text
create_product()
get_product()
get_products()
update_product_price()
delete_product()
```

### Model

```python
@dataclass
class Product:
    id: int
    name: str
    price: float
```

---

## `get_product()`

```python
def get_product(product_id: int) -> Product | None:
    connection = get_connection()

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT id, name, price
            FROM products
            WHERE id = %s
            """,
            (product_id,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Product(
            id=row["id"],
            name=row["name"],
            price=float(row["price"])
        )

    finally:
        cursor.close()
        connection.close()
```

---

# 40. `create_product()`

```python
def create_product(
    name: str,
    price: float
) -> int:

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO products
            (name, price)
            VALUES (%s, %s)
            """,
            (name, price)
        )

        connection.commit()

        return cursor.lastrowid

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()
```

`lastrowid` gives us the newly created ID when supported by the driver/database configuration.

---

# 41. `update_product_price()`

```python
def update_product_price(
    product_id: int,
    price: float
) -> bool:

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE products
            SET price = %s
            WHERE id = %s
            """,
            (price, product_id)
        )

        connection.commit()

        return cursor.rowcount > 0

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()
```

---

# 42. Important Improvement

Our repository methods currently open and close a connection for every operation.

For a simple learning application, that's fine.

But a high-traffic application shouldn't necessarily establish a brand-new database connection for every request.

Instead we eventually use:

```text
Connection Pool
```

Conceptually:

```text
Application
    │
    ├── Request 1 ──┐
    ├── Request 2 ──┤
    ├── Request 3 ──┤
    └── Request 4 ──┤
                    ▼
             Connection Pool
             ├── Connection 1
             ├── Connection 2
             ├── Connection 3
             └── Connection 4
```

We'll study this properly in **Lesson 08 — Database Performance**.

---

# 43. What You Should Remember

The most important concepts from this lesson are:

### Connection

```python
get_connection()
```

### Cursor

```python
cursor.execute(...)
```

### Parameters

```python
cursor.execute(query, values)
```

### Read

```python
fetchone()
fetchall()
```

### Write

```python
INSERT
UPDATE
DELETE
```

### Persist

```python
connection.commit()
```

### Failure

```python
connection.rollback()
```

### Cleanup

```python
cursor.close()
connection.close()
```

### Security

```text
Parameterized queries
```

### Architecture

```text
Python
 ↓
Service
 ↓
Database Driver
 ↓
SQL
 ↓
Database
```

---

# 🎯 Lesson 06 Practical Exercise

Build the following functions:

```python
create_product()
get_product()
get_products()
update_product_price()
delete_product()
```

Use:

```text
Python
MySQL
Parameterized SQL
Dataclass
Type hints
Exception handling
Transactions
Logging
```

### Requirements

#### 1. Create

```python
create_product(
    name="Keyboard",
    price=3000
)
```

Return the new product ID.

#### 2. Get

```python
get_product(101)
```

Return:

```python
Product(...)
```

or:

```python
None
```

#### 3. Get all

```python
get_products()
```

Return:

```python
list[Product]
```

#### 4. Update

```python
update_product_price(
    product_id=101,
    price=65000
)
```

Return:

```text
True / False
```

#### 5. Delete

```python
delete_product(101)
```

Return whether a row was deleted.

---

# ⭐ Final Challenge — Order Creation Transaction

This is the most important exercise.

Implement conceptually:

```python
create_order(
    customer_id=1,
    product_id=101,
    quantity=2
)
```

It should:

```text
1. Start transaction
       ↓
2. Read product price
       ↓
3. Check stock
       ↓
4. Create order
       ↓
5. Create order_item
       ↓
6. Reduce stock
       ↓
7. Commit
```

If **any step fails**:

```text
ROLLBACK
```

And use logging:

```text
INFO  Order creation started
INFO  Product validated
INFO  Order created
INFO  Inventory updated
INFO  Order committed

OR

ERROR Order creation failed
ERROR Transaction rolled back
```

This one exercise will combine almost everything we've learned so far:

```text
Python
+ Type Hints
+ Dataclasses
+ Logging
+ SQL
+ Database Relationships
+ Parameterized Queries
+ Transactions
+ Commit/Rollback
+ Error Handling
+ Project Structure
```

**Once you've completed/reviewed this, Lesson 07 will be ORM with SQLAlchemy**, where we'll replace much of the manual SQL/connection handling with models, sessions, relationships, CRUD, and transactions.
