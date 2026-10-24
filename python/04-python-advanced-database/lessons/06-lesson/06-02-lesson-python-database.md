# Lesson 06 — Python + Database

## Part 2 — Repository, Service & Transaction Architecture

In Part 1, we learned how Python communicates with a database using a database driver.

We covered:

* Database connections
* Cursors
* SQL execution
* Parameterized queries
* `fetchone()`
* `fetchall()`
* INSERT / UPDATE / DELETE
* Transactions
* `commit()`
* `rollback()`
* Exception handling
* Logging
* Type hints
* Dataclasses

In this part, we will improve our application architecture by separating:

```text
User Interface
      ↓
Service Layer
      ↓
Repository Layer
      ↓
Database
```

The goal is to move from:

> "Python code that works"

to:

> "Python code that is easier to maintain, test and extend."

---

# 1. Why Do We Need Layers?

Imagine putting everything into `main.py`:

```python
connection = get_connection()

cursor.execute(...)
cursor.execute(...)
cursor.execute(...)

if stock < quantity:
    ...

print(...)
```

This works for a small program.

But as the application grows, `main.py` becomes responsible for:

* User input
* Business rules
* SQL
* Transactions
* Error handling
* Output

That creates tightly coupled code.

Instead, separate responsibilities.

```text
main.py
   ↓
Service
   ↓
Repository
   ↓
Database
```

---

# 2. Responsibility of Each Layer

## Main / Presentation Layer

Responsible for:

* User input
* Calling services
* Displaying messages

Example:

```python
print("Order created successfully")
```

The service should not decide how the result is displayed.

---

## Service Layer

Responsible for:

* Business logic
* Validation
* Business decisions
* Coordinating multiple repositories
* Transaction management

Example:

```python
if product["stock_quantity"] < quantity:
    raise ApplicationError(...)
```

---

## Repository Layer

Responsible for:

* SQL queries
* Database operations
* Cursor management
* Returning database results

Example:

```python
cursor.execute(
    """
    SELECT *
    FROM products
    WHERE id = %s
    """,
    (product_id,)
)
```

The repository should generally not contain business decisions.

---

# 3. Repository vs Service

This distinction is extremely important.

## Repository

The repository answers:

> "How do I communicate with the database?"

For example:

```python
get_product()
create_product()
update_product()
delete_product()
```

---

## Service

The service answers:

> "What should the application do?"

For example:

```python
place_order()
```

The service might:

1. Validate quantity
2. Find product
3. Check stock
4. Calculate total
5. Create order
6. Create order item
7. Reduce stock
8. Commit transaction

---

# 4. Project Structure

Our project is moving toward:

```text
ecommerce-db/
│
├── app/
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── connection.py
│   │
│   ├── exceptions/
│   │   ├── __init__.py
│   │   └── application.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── product.py
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── product_repository.py
│   │   └── order_repository.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── product_service.py
│   │   └── order_service.py
│   │
│   └── main.py
│
├── tests/
│
├── .env
├── .gitignore
└── requirements.txt
```

---

# 5. Why Should the Service Own the Database Connection?

This is one of the most important concepts in this lesson.

Consider creating an order.

An order consists of multiple operations:

```text
1. Get product
2. Check stock
3. Create order
4. Create order item
5. Reduce stock
6. Commit
```

These operations should be treated as **one transaction**.

Therefore, they should use the same database connection.

```text
Order Service
      │
      │ get_connection()
      ▼
  Connection A
      │
      ├── Get product
      ├── Create order
      ├── Create order item
      ├── Reduce stock
      │
      ├── COMMIT
      │
      └── CLOSE
```

---

# 6. What Happens If Each Repository Creates Its Own Connection?

Imagine:

```text
Service
   │
   ├── Product Repository
   │       └── Connection A
   │
   ├── Order Repository
   │       └── Connection B
   │
   └── Order Item Repository
           └── Connection C
```

Now imagine:

```text
Create order       → SUCCESS
Create order item  → SUCCESS
Update stock       → FAILURE
```

The earlier operations may already have been committed.

We can no longer safely roll back the entire business operation using one transaction.

Therefore:

> When multiple repository operations form one business transaction, the Service should provide the same connection to all repositories.

---

# 7. Connection Ownership

A very useful rule is:

> **Whoever owns a resource is responsible for releasing it.**

If the Service creates the connection:

```python
connection = get_connection()
```

then the Service owns it.

Therefore the Service is responsible for:

```python
connection.commit()
connection.rollback()
connection.close()
```

The Repository receives the connection and uses it.

The Repository should not close it.

---

# 8. Repository Cursor Ownership

The Repository creates the cursor:

```python
cursor = connection.cursor()
```

Therefore the Repository owns the cursor.

It should close the cursor:

```python
finally:
    cursor.close()
```

So the ownership becomes:

```text
Service
 └── owns connection
       │
       ├── Repository
       │     └── owns cursor
       │
       ├── Repository
       │     └── owns cursor
       │
       └── Repository
             └── owns cursor
```

---

# 9. Transaction Ownership

The Service owns:

```python
connection.commit()
```

and:

```python
connection.rollback()
```

The Repository should generally NOT do:

```python
connection.commit()
```

or:

```python
connection.rollback()
```

because it doesn't know whether its operation is part of a larger business transaction.

---

# 10. Example Transaction

Our order operation looks like:

```python
connection = get_connection()

try:

    # repository operations

    connection.commit()

except Exception:

    connection.rollback()
    raise

finally:

    connection.close()
```

This gives us:

```text
Everything succeeds
       ↓
    COMMIT
```

or:

```text
Something fails
       ↓
   ROLLBACK
```

---

# 11. Repository Layer

Our repository should concentrate on SQL.

For example:

```python
def get_product(connection, product_id: int):

    cursor = None

    try:

        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT
                id,
                category_id,
                sku,
                name,
                price,
                stock_quantity,
                created_at,
                updated_at
            FROM products
            WHERE id = %s
            """,
            (product_id,)
        )

        return cursor.fetchone()

    finally:

        if cursor:
            cursor.close()
```

Notice:

* It receives `connection`
* It executes SQL
* It returns data
* It closes its cursor
* It does NOT close the connection
* It does NOT commit
* It does NOT rollback

---

# 12. Insert Repository Example

```python
def create_order(
    connection,
    customer_id: int,
    order_number: str,
    status: str,
    total_amount: float
):

    cursor = None

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO orders
                (
                    customer_id,
                    order_number,
                    status,
                    total_amount
                )
            VALUES
                (%s, %s, %s, %s)
            """,
            (
                customer_id,
                order_number,
                status,
                total_amount
            )
        )

        return cursor.lastrowid

    finally:

        if cursor:
            cursor.close()
```

Again, no:

```python
connection.commit()
```

The Service decides when the transaction is complete.

---

# 13. Update Repository Example

```python
def reduce_stock(
    connection,
    quantity: int,
    product_id: int
):

    cursor = None

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE products
            SET stock_quantity = stock_quantity - %s
            WHERE id = %s
              AND stock_quantity >= %s
            """,
            (
                quantity,
                product_id,
                quantity
            )
        )

        return cursor.rowcount

    finally:

        if cursor:
            cursor.close()
```

Notice the additional condition:

```sql
AND stock_quantity >= %s
```

This provides an additional database-level protection against reducing stock below zero.

---

# 14. Why We Don't Use `lastrowid` for UPDATE

For an INSERT:

```python
order_id = cursor.lastrowid
```

is appropriate because MySQL generated an ID.

For UPDATE:

```python
cursor.lastrowid
```

is not the correct way to determine whether anything changed.

Use:

```python
cursor.rowcount
```

Example:

```python
affected_rows = cursor.rowcount

if affected_rows == 0:
    ...
```

---

# 15. Application Exceptions

We previously considered creating many custom exceptions:

```text
ProductNotFoundError
InsufficientStockError
OrderCreationError
CustomerNotFoundError
...
```

For this learning project, that is unnecessary.

Instead, we use a generic application-level exception.

### `application.py`

```python
class ApplicationError(Exception):

    def __init__(
        self,
        message: str,
        code: str
    ):
        super().__init__(message)

        self.message = message
        self.code = code
```

Now the service can raise:

```python
raise ApplicationError(
    "Product was not found",
    "PRODUCT_NOT_FOUND"
)
```

or:

```python
raise ApplicationError(
    "Insufficient stock",
    "INSUFFICIENT_STOCK"
)
```

No need to create a separate class for every condition.

---

# 16. Expected vs Unexpected Errors

This distinction is important.

## Expected business error

Examples:

```text
Product doesn't exist
Insufficient stock
Invalid quantity
```

Use:

```python
ApplicationError(...)
```

---

## Unexpected technical error

Examples:

```text
Database connection failure
SQL error
Programming bug
Unexpected database exception
```

Don't hide these.

Use logging:

```python
logger.exception(
    "Unexpected error while creating order"
)
```

and re-raise:

```python
raise
```

---

# 17. Service Layer Example

The Service coordinates everything.

```python
def create_order(
    customer_id: int,
    product_id: int,
    quantity: int
) -> int:

    connection = get_connection()

    try:

        if quantity <= 0:
            raise ApplicationError(
                "Quantity must be greater than zero",
                "INVALID_QUANTITY"
            )

        product = repository_get_product(
            connection,
            product_id
        )

        if product is None:
            raise ApplicationError(
                "Product was not found",
                "PRODUCT_NOT_FOUND"
            )

        if product["stock_quantity"] < quantity:
            raise ApplicationError(
                "Insufficient stock",
                "INSUFFICIENT_STOCK"
            )

        price = product["price"]

        subtotal = price * quantity

        order_id = repository_create_order(
            connection,
            customer_id,
            order_number,
            "pending",
            subtotal
        )

        repository_create_order_items(
            connection,
            order_id,
            product_id,
            quantity,
            price,
            subtotal
        )

        affected_rows = reduce_stock(
            connection,
            quantity,
            product_id
        )

        if affected_rows == 0:
            raise ApplicationError(
                "Product stock update failed",
                "STOCK_UPDATE_FAILED"
            )

        connection.commit()

        return order_id

    except Exception:

        connection.rollback()

        raise

    finally:

        connection.close()
```

The important concept is not the exact code.

It is the responsibility:

```text
Service
 ├── Business validation
 ├── Coordinates repositories
 ├── Owns connection
 ├── COMMIT
 ├── ROLLBACK
 └── CLOSE
```

---

# 18. Avoid Naming Conflicts

A common problem occurs when Service and Repository functions have the same name.

For example:

```python
from app.repositories.product_repository import create_product


def create_product(...):

    create_product(...)
```

Now it becomes difficult to determine which `create_product()` is being called.

We can use aliases:

```python
from app.repositories.product_repository import (
    create_product as repository_create_product,
    update_product_price as repository_update_product_price,
    get_product as repository_get_product,
    get_products as repository_get_products,
    delete_product as repository_delete_product,
)
```

Now it is obvious:

```python
repository_create_product(...)
```

means:

> Call the Repository.

while:

```python
create_product(...)
```

means:

> Call the Service.

---

# 19. Why `print()` Should Not Be in the Service

We discussed an important architectural principle:

Avoid:

```python
print("Product not found")
```

inside the Service.

Instead:

```python
raise ApplicationError(
    "Product was not found",
    "PRODUCT_NOT_FOUND"
)
```

Then `main.py` decides how to present it:

```python
try:

    order_id = create_order(
        customer_id,
        product_id,
        quantity
    )

    print(
        f"Order created successfully. "
        f"Order ID: {order_id}"
    )

except ApplicationError as e:

    print(
        f"Order could not be created: "
        f"{e.message} "
        f"(Code: {e.code})"
    )
```

This makes the Service independent from the CLI.

Later, the same Service could be called by:

```text
CLI
REST API
Background Worker
AI Agent
Magento Integration
```

without changing the business logic.

---

# 20. Avoid Calling `main()` Recursively

Another improvement we made was removing:

```python
main()
```

from inside `main()`.

For example, avoid:

```python
if not is_updated:
    print("Product is not updated")
    main()
```

Instead, use the existing:

```python
while True:
```

loop.

```text
main()
  │
  ▼
while True
  │
  ├── option 1
  ├── option 2
  ├── option 3
  ├── option 4
  ├── option 5
  ├── option 6
  │
  └── option 7 → break
```

This avoids unnecessary recursion and keeps the CLI loop clean.

---

# 21. Complete Architecture

Our current architecture is:

```text
                    main.py
                       │
                       │ User interaction
                       ▼
                 Service Layer
                       │
                       │ Business logic
                       │ Transaction ownership
                       ▼
                Repository Layer
                       │
                       │ SQL
                       ▼
                    MySQL
```

For an order:

```text
main.py
   │
   ▼
create_order()
   │
   ▼
Order Service
   │
   │ get_connection()
   │
   ├───────────────┐
   ▼               ▼
Product Repo    Order Repo
   │               │
   │               ├── create order
   │               └── create order item
   │
   └── reduce stock
   │
   ▼
COMMIT
   │
   ▼
CLOSE
```

---

# 22. Real-World Example

Consider an e-commerce website.

A customer buys:

```text
Product: Laptop
Quantity: 2
Price: ₹50,000
```

The application needs to:

```text
Create order
       ↓
Create order item
       ↓
Reduce stock by 2
```

If stock update fails but the order was already committed:

```text
Order exists      ✅
Order item exists ✅
Stock unchanged   ❌
```

Now the system is inconsistent.

With a transaction:

```text
BEGIN
  │
  ├── Create order
  ├── Create order item
  └── Reduce stock
       │
       ├── SUCCESS → COMMIT
       │
       └── FAILURE → ROLLBACK
```

This keeps the database consistent.

---

# 23. How This Relates to Magento

This architecture should feel familiar from your Magento experience.

Conceptually:

```text
Magento Controller
       ↓
Service / Business Logic
       ↓
Repository
       ↓
Resource Model
       ↓
Database
```

Our Python application is using the same general separation of responsibilities:

```text
Python CLI
    ↓
Service
    ↓
Repository
    ↓
MySQL
```

The implementation differs, but the architectural thinking is similar.

---

# 24. How This Helps Future AI Development

This architecture will become even more useful when we start AI development.

Eventually we may have:

```text
AI Agent
   │
   ▼
Tool
   │
   ▼
Service
   │
   ▼
Repository
   │
   ▼
Database
```

For example:

```text
User:
"Create an order for 2 laptops"

AI Agent
    ↓
create_order tool
    ↓
Order Service
    ↓
Repositories
    ↓
Database
```

The AI should not directly execute arbitrary SQL.

Instead, it should interact with a controlled application service.

---

# 25. Important Design Rules

Keep these rules in mind.

### Rule 1

Repository handles:

```text
SQL
```

### Rule 2

Service handles:

```text
Business logic
```

### Rule 3

Main handles:

```text
User interaction
```

### Rule 4

The owner of the connection manages:

```text
commit
rollback
close
```

### Rule 5

Repository closes:

```text
its cursor
```

not the connection supplied by the Service.

### Rule 6

Don't create a custom exception class for every possible error.

Use:

```python
ApplicationError
```

unless there is a real reason to distinguish errors programmatically.

### Rule 7

Don't put user-facing `print()` statements inside Services.

### Rule 8

Don't use recursive calls to `main()` for menu navigation.

---

# 26. Final Mental Model

The most important thing to remember from this lesson is:

```text
MAIN
"What should I show the user?"

        ↓

SERVICE
"What should the application do?"

        ↓

REPOSITORY
"How do I access the database?"

        ↓

DATABASE
"Store/retrieve the data."
```

And for transactions:

```text
SERVICE
   │
   ├── get connection
   │
   ├── repository operation
   ├── repository operation
   ├── repository operation
   │
   ├── commit()
   │      OR
   ├── rollback()
   │
   └── close()
```

---

# 27. Lesson 06 Part 2 — Practical Exercise

Before moving to SQLAlchemy, implement the following in your project:

### Task 1

Create:

```text
app/repositories/product_repository.py
app/repositories/order_repository.py
```

### Task 2

Move SQL operations into the repositories.

### Task 3

Make Services responsible for:

* Connection
* Business validation
* Transaction
* Commit
* Rollback
* Connection close

### Task 4

Make repositories responsible for:

* Cursor creation
* SQL execution
* Returning results
* Cursor closing

### Task 5

Use:

```python
ApplicationError
```

for expected business failures.

### Task 6

Remove service-layer `print()` statements.

### Task 7

Remove recursive:

```python
main()
```

calls.

### Task 8

Test:

```text
Create Product
Update Product
Get Product
Get Products
Delete Product
Create Order
```

For order creation verify:

```sql
SELECT * FROM orders;

SELECT * FROM order_items;

SELECT
    id,
    sku,
    stock_quantity
FROM products;
```

---

# 28. Lesson 06 Complete Architecture

After completing this part, our project has:

```text
Python
  │
  ├── Type hints
  ├── Dataclasses
  ├── Logging
  ├── Exceptions
  ├── Project structure
  │
  └── Database
       │
       ├── Connection
       ├── SQL
       ├── Transactions
       ├── Repository
       └── Service
```

This completes the **professional Python + MySQL foundation** we need before introducing an ORM.

## Next Lesson

**Lesson 07 — ORM with SQLAlchemy**

We will learn:

* What is ORM?
* Why ORM?
* SQLAlchemy
* Models
* Engine
* Session
* CRUD
* Relationships
* Transactions with `Session`
* Querying
* MySQL with SQLAlchemy
* PostgreSQL with SQLAlchemy
* SQLAlchemy vs raw SQL
* When to use ORM vs raw SQL
* Practical e-commerce implementation
* Refactoring our current `ecommerce-db` project

We will specifically use **both MySQL and PostgreSQL** so that you get practical experience with PostgreSQL rather than only hearing about it.
