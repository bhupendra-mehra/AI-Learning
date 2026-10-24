# Lesson 07 — Part 3: SQLAlchemy Session + Insert Real E-Commerce Data

Now that the tables are successfully created, we move to the most important ORM concept: **the SQLAlchemy `Session`**.

The goal is to insert actual e-commerce data:

```text
Category
   ↓
Product
   ↓
Customer
```

and understand exactly how:

```text
Python Object
      ↓
SQLAlchemy Session
      ↓
INSERT SQL
      ↓
MySQL
```

---

## 1. What is a SQLAlchemy Session?

A `Session` is the main object SQLAlchemy uses to:

* add new ORM objects
* retrieve objects
* track changes
* manage transactions
* commit changes
* rollback failed transactions

Think of it as the **working area between your Python application and database**.

```text
Application
     │
     ▼
 SQLAlchemy Session
     │
     ├── Add
     ├── Query
     ├── Update
     ├── Delete
     ├── Commit
     └── Rollback
     │
     ▼
   MySQL
```

This is similar to the role a database connection/transaction layer plays in Magento, but SQLAlchemy's ORM gives you Python objects mapped directly to database rows.

---

# 2. Create a Session Factory

Your current `app/database/database.py` contains the engine.

Add `sessionmaker`:

```python
import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()


class Base(DeclarativeBase):
    pass


database_url = URL.create(
    drivername="mysql+mysqlconnector",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", "3306")),
    database=os.getenv("DB_NAME"),
)


engine = create_engine(
    database_url,
    echo=True
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
```

### What is `SessionLocal`?

This:

```python
SessionLocal = sessionmaker(...)
```

creates a **factory** for SQLAlchemy sessions.

It doesn't create a session immediately.

When we do:

```python
session = SessionLocal()
```

we get an actual session.

---

# 3. Why `sessionmaker`?

Instead of repeatedly doing complicated session configuration:

```python
session = ...
```

we configure it once:

```python
SessionLocal = sessionmaker(...)
```

and then every part of the application can create a properly configured session:

```python
session = SessionLocal()
```

This becomes particularly useful when we later build:

* repositories
* services
* APIs
* background workers
* transactions

---

# 4. Create a Database Session Test

Create:

```text
app/session_test.py
```

Put:

```python
from app.database import SessionLocal


session = SessionLocal()

print("Database session created successfully")

session.close()

print("Database session closed successfully")
```

Run:

```bash
python -m app.session_test
```

Expected:

```text
Database session created successfully
Database session closed successfully
```

---

# 5. Now Insert a Customer

Let's make this practical.

Create:

```text
app/seed.py
```

Start with:

```python
from app.database import SessionLocal
from app.models.customer import Customer


session = SessionLocal()

customer = Customer(
    name="Bhupendra",
    email="bhupendra@example.com"
)

session.add(customer)

session.commit()

print(f"Customer created with ID: {customer.id}")

session.close()
```

Run:

```bash
python -m app.seed
```

Because you have:

```python
echo=True
```

you should see SQL similar to:

```sql
INSERT INTO customers
(name, email, created_at, updated_at)
VALUES
(%(name)s, %(email)s, %(created_at)s, %(updated_at)s)
```

Then:

```text
Customer created with ID: 1
```

The exact ID may be different depending on your database.

---

# 6. Understand `session.add()`

This:

```python
session.add(customer)
```

does **not necessarily immediately execute the INSERT**.

It places the object into the session's pending state.

Conceptually:

```text
Customer object
      ↓
 session.add()
      ↓
Session tracks object
```

Then:

```python
session.commit()
```

causes the transaction to be committed to MySQL.

```text
Session
   ↓
INSERT
   ↓
COMMIT
   ↓
MySQL
```

---

# 7. What is `flush()`?

This is an important ORM concept.

You can do:

```python
session.add(customer)

session.flush()

print(customer.id)

session.commit()
```

`flush()` sends pending SQL to the database **without committing the transaction**.

For example:

```text
session.add(customer)
        ↓
    pending
        ↓
session.flush()
        ↓
INSERT executed
        ↓
customer.id available
        ↓
session.commit()
        ↓
transaction permanently committed
```

This is why our repositories previously used:

```python
self.session.add(customer)
self.session.flush()
```

We can get the generated ID before committing the entire business transaction.

---

# 8. `flush()` vs `commit()`

This distinction is extremely important.

| Operation    | Purpose                        |
| ------------ | ------------------------------ |
| `add()`      | Put object into session        |
| `flush()`    | Send pending SQL to DB         |
| `commit()`   | Permanently commit transaction |
| `rollback()` | Undo uncommitted transaction   |
| `close()`    | Close session                  |

Example:

```python
session.add(customer)

session.flush()

print(customer.id)

session.commit()
```

---

# 9. Verify the Customer in MySQL

Run:

```bash
mysql -u root -p
```

Then:

```sql
USE ecommerce;

SELECT
    id,
    name,
    email,
    created_at,
    updated_at
FROM customers;
```

You should see something like:

```text
+----+-----------+-------------------------+---------------------+---------------------+
| id | name      | email                   | created_at          | updated_at          |
+----+-----------+-------------------------+---------------------+---------------------+
|  1 | Bhupendra | bhupendra@example.com   | ...                 | ...                 |
+----+-----------+-------------------------+---------------------+---------------------+
```

This is our first complete ORM flow:

```text
Customer Python Object
        ↓
Customer ORM Model
        ↓
SQLAlchemy Session
        ↓
INSERT
        ↓
MySQL customers table
```

---

# 10. Important: Don't Run the Seed Script Repeatedly

Our current code:

```python
customer = Customer(
    name="Bhupendra",
    email="bhupendra@example.com"
)
```

will attempt to insert the same email every time.

Because our model has:

```python
email = mapped_column(
    String(255),
    unique=True,
    nullable=False
)
```

running the script a second time will eventually produce a duplicate-key error.

That's actually useful for learning.

But don't repeatedly run it yet.

---

# 11. Let's Use the Repository We Already Created

We already have:

```text
app/repositories/customer_repository.py
```

with:

```python
class CustomerRepository:
```

So instead of directly doing:

```python
session.add(customer)
```

from our application, we can use:

```text
Application
     ↓
CustomerRepository
     ↓
SQLAlchemy Session
     ↓
Customer Model
     ↓
MySQL
```

Update `app/seed.py`:

```python
from app.database import SessionLocal
from app.repositories.customer_repository import CustomerRepository


session = SessionLocal()

try:
    customer_repository = CustomerRepository(session)

    customer = customer_repository.create(
        name="Bhupendra",
        email="bhupendra@example.com"
    )

    session.commit()

    print(f"Customer created with ID: {customer.id}")

except Exception:
    session.rollback()
    raise

finally:
    session.close()
```

This is much closer to a real application.

---

# 12. Why `try / except / finally`?

This pattern is extremely important for database code:

```python
try:
    # database operations

except Exception:
    session.rollback()
    raise

finally:
    session.close()
```

If something fails:

```text
Database Error
     ↓
except
     ↓
rollback()
     ↓
transaction cancelled
```

Regardless of success/failure:

```text
finally
   ↓
session.close()
```

So we don't leave database sessions open unnecessarily.

---

# 13. Why Doesn't the Repository Commit?

Notice our repository:

```python
def create(self, name: str, email: str) -> Customer:
    customer = Customer(
        name=name,
        email=email
    )

    self.session.add(customer)
    self.session.flush()

    return customer
```

doesn't do:

```python
self.session.commit()
```

That's intentional.

The **service/application layer should control the transaction**.

This becomes very important for our e-commerce order.

Imagine:

```text
Create Order
     ↓
Add Order Item
     ↓
Reduce Product Stock
     ↓
Calculate Total
     ↓
Everything succeeds?
     │
    YES
     ↓
   COMMIT
```

But if stock update fails:

```text
Create Order
     ↓
Add Order Item
     ↓
Stock update FAILED
     ↓
ROLLBACK
```

We don't want half an order stored in the database.

This is one of the major reasons we separate:

```text
Repository
    ↓
Database operations

Service
    ↓
Business transaction
```

---

# 14. Our E-Commerce Transaction

Eventually our `OrderService` will perform:

```python
order = create_order()

add_order_item()

reduce_stock()

calculate_total()

commit()
```

as **one transaction**.

Conceptually:

```text
                 Transaction
┌──────────────────────────────────┐
│                                  │
│ Create Order                     │
│       ↓                          │
│ Create Order Item                │
│       ↓                          │
│ Reduce Product Stock             │
│       ↓                          │
│ Calculate Order Total            │
│       ↓                          │
│           COMMIT                 │
│                                  │
└──────────────────────────────────┘
```

If any operation fails:

```text
             ERROR
               ↓
            ROLLBACK
               ↓
     No partial order
```

This is exactly the type of problem an e-commerce system must handle correctly.

---

# 15. Your Task Now

### Step 1

Add this to:

```text
app/database/database.py
```

```python
from sqlalchemy.orm import sessionmaker
```

and:

```python
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
```

### Step 2

Create:

```text
app/session_test.py
```

and test the session.

### Step 3

Create:

```text
app/seed.py
```

using the repository version.

### Step 4

Run:

```bash
python -m app.seed
```

### Step 5

Verify:

```sql
SELECT * FROM customers;
```

### Step 6

Also verify the timestamps:

```sql
SELECT
    id,
    name,
    email,
    created_at,
    updated_at
FROM customers;
```

Once the customer insertion works, we'll continue with:

**Lesson 07 — Part 4: Insert Category + Products and use SQLAlchemy relationships**

where we'll create:

```text
Electronics
    ├── Laptop
    ├── Wireless Mouse
    └── Keyboard
```

and access them through ORM relationships such as:

```python
product.category
```

and:

```python
category.products
```

That is where the SQLAlchemy ORM starts becoming much more powerful than writing raw SQL for every operation.
