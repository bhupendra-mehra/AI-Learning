# Part 4 — Data & Database Development

## Lesson 07-01 — ORM / SQLAlchemy

### 1. What is ORM?

**ORM (Object-Relational Mapping)** is a technique that allows us to work with database tables using programming-language objects instead of writing SQL for every operation.

For example, instead of:

```sql
SELECT * FROM customers WHERE id = 10;
```

with an ORM we can write Python code such as:

```python
customer = session.get(Customer, 10)
```

The ORM translates the Python operation into SQL and executes it against the database.

### ORM mapping

| Python       | Database                 |
| ------------ | ------------------------ |
| Class        | Table                    |
| Object       | Row                      |
| Attribute    | Column                   |
| Method/query | SQL operation            |
| Relationship | Foreign key relationship |

For example:

```python
class Customer:
    id = 10
    name = "John"
```

can represent:

```text
customers
--------------------------------
id    name
10    John
```

---

# 2. What is SQLAlchemy?

**SQLAlchemy** is one of the most widely used database libraries in Python.

It provides two major approaches:

1. **SQLAlchemy Core** — SQL-oriented database programming
2. **SQLAlchemy ORM** — object-oriented database programming

For application development, we will primarily use **SQLAlchemy ORM**.

A typical architecture looks like:

```text
Python Application
       |
       v
SQLAlchemy ORM
       |
       v
SQLAlchemy Engine
       |
       v
Database Driver
       |
       v
MySQL / PostgreSQL
```

For example:

```text
Python
  |
  | SQLAlchemy
  v
MySQL
```

or:

```text
Python
  |
  | SQLAlchemy
  v
PostgreSQL
```

The same Python application can therefore work with different relational databases with relatively small changes.

---

# 3. Why use SQLAlchemy instead of writing raw SQL?

You have already worked with Python database connectivity using `mysql-connector-python`.

For example, raw SQL:

```python
query = """
    SELECT id, name, email
    FROM customers
    WHERE id = %s
"""

cursor.execute(query, (customer_id,))
```

This works well, but as an application becomes larger, you may have:

* hundreds of SQL queries
* many tables
* relationships between tables
* repeated CRUD operations
* transactions
* validation
* migrations
* complex application models

SQLAlchemy ORM provides a higher-level abstraction.

Instead of:

```sql
SELECT *
FROM customers
WHERE id = 10;
```

you can work with:

```python
customer = session.get(Customer, 10)
```

---

# 4. SQLAlchemy Installation

Create or activate your virtual environment first:

```bash
source .venv/bin/activate
```

Install SQLAlchemy:

```bash
pip install sqlalchemy
```

For MySQL:

```bash
pip install mysql-connector-python
```

For PostgreSQL:

```bash
pip install psycopg2-binary
```

Alternatively, the modern PostgreSQL driver can be installed with:

```bash
pip install psycopg
```

Check the installation:

```bash
pip show sqlalchemy
```

---

# 5. SQLAlchemy Database URL

SQLAlchemy uses a database URL to establish a connection.

### MySQL

Using MySQL Connector:

```text
mysql+mysqlconnector://username:password@localhost/database_name
```

Example:

```text
mysql+mysqlconnector://root:password@localhost/shop
```

### PostgreSQL

Using psycopg2:

```text
postgresql+psycopg2://username:password@localhost/database_name
```

Example:

```text
postgresql+psycopg2://postgres:password@localhost/shop
```

Using psycopg 3:

```text
postgresql+psycopg://username:password@localhost/database_name
```

---

# 6. Creating an SQLAlchemy Engine

The **Engine** is the central connection interface between SQLAlchemy and the database.

```python
from sqlalchemy import create_engine

DATABASE_URL = "mysql+mysqlconnector://root:password@localhost/shop"

engine = create_engine(DATABASE_URL)
```

For PostgreSQL:

```python
from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost/shop"

engine = create_engine(DATABASE_URL)
```

Think of the engine as:

```text
Application
     |
     v
  Engine
     |
     v
Database Connection Pool
     |
     v
Database
```

---

# 7. Testing the Database Connection

We can test the connection using `text()`.

```python
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

database_url = URL.create(
    drivername="mysql+mysqlconnector",
    username="root",
    password="Encora@1",
    host="localhost",
    port=3306,
    database="ecommerce",
)

engine = create_engine(database_url)

try:
    engine.connect()
    print("Success")
except Exception as e:
    print(f"Failed : {e}")
```

Output:

```text
1
```

For PostgreSQL, only the connection URL changes:

```python
DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost/shop"
```

The rest of the code can remain the same.

---

# 8. SQLAlchemy Declarative Models

Now we move from database connections to ORM.

Create a model:

```python
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
```

### SQLAlchemy `Base` Class

The `Base` class is the foundation for SQLAlchemy ORM models. It inherits from `DeclarativeBase` and provides SQLAlchemy with the metadata and mapping information needed to associate Python model classes with database tables.

All ORM models should inherit from `Base`:

```python
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
```

For example:

```python
class Customer(Base):
    __tablename__ = "customers"
```

Here, `Customer` becomes a SQLAlchemy ORM model and its table definition is registered in `Base.metadata`.

`Base.metadata` can then be used to create or manage the application's database table definitions:

```python
Base.metadata.create_all(engine)
```

**In short:** `Base` acts as the common foundation and registry for all SQLAlchemy ORM models.


Then create a model representing a database table:

```python
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))
```

This Python class represents:

```text
customers
--------------------------------
id
name
email
```

The mapping is:

```text
Customer
   |
   +---- id
   |
   +---- name
   |
   +---- email
```

---

# 9. Creating Tables

We can ask SQLAlchemy to create tables from our models:

```python
Base.metadata.create_all(engine)
```

Complete example:

```python
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


DATABASE_URL = "mysql+mysqlconnector://root:password@localhost/shop"

engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))


Base.metadata.create_all(engine)
```

SQLAlchemy generates the required `CREATE TABLE` statement.

Conceptually:

```sql
CREATE TABLE customers (
    id INTEGER NOT NULL,
    name VARCHAR(100),
    email VARCHAR(255),
    PRIMARY KEY (id)
);
```

---

# 10. SQLAlchemy Session

The **Session** is one of the most important concepts in SQLAlchemy ORM.

It manages:

* database operations
* objects
* transactions
* inserts
* updates
* deletes
* queries

Create a session factory:

```python
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)
```

Then:

```python
session = SessionLocal()
```

A modern approach is:

```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    ...
```

This is preferable because the session is automatically closed.

---

# 11. INSERT — Creating a Record

Create a Python object:

```python
customer = Customer(
    name="John Doe",
    email="john@example.com"
)
```

Add it to the session:

```python
session.add(customer)
```

Commit the transaction:

```python
session.commit()
```

Complete example:

```python
with Session(engine) as session:
    customer = Customer(
        name="John Doe",
        email="john@example.com"
    )

    session.add(customer)
    session.commit()
```

Database:

```text
id | name      | email
---|-----------|------------------
1  | John Doe  | john@example.com
```

---

# 12. Getting the Generated ID

After committing:

```python
print(customer.id)
```

Example:

```python
with Session(engine) as session:
    customer = Customer(
        name="John Doe",
        email="john@example.com"
    )

    session.add(customer)
    session.commit()

    print(customer.id)
```

Output:

```text
1
```

SQLAlchemy automatically populates the generated primary key.

---

# 13. SELECT — Reading Records

SQLAlchemy provides `select()` for queries.

```python
from sqlalchemy import select
```

Example:

```python
with Session(engine) as session:
    statement = select(Customer)

    result = session.execute(statement)

    customers = result.scalars().all()

    for customer in customers:
        print(customer.name, customer.email)
```

Output:

```text
John Doe john@example.com
Jane Smith jane@example.com
```

---

# 14. Selecting a Single Customer

```python
with Session(engine) as session:
    customer = session.get(Customer, 1)

    if customer:
        print(customer.name)
```

This is conceptually equivalent to:

```sql
SELECT *
FROM customers
WHERE id = 1;
```

---

# 15. Filtering Records

Suppose we want:

```sql
SELECT *
FROM customers
WHERE email = 'john@example.com';
```

SQLAlchemy:

```python
from sqlalchemy import select

with Session(engine) as session:
    statement = select(Customer).where(
        Customer.email == "john@example.com"
    )

    customer = session.scalars(statement).first()

    if customer:
        print(customer.name)
```

Notice:

```python
Customer.email == "john@example.com"
```

SQLAlchemy converts the Python expression into SQL.

---

# 16. Multiple Conditions

SQL:

```sql
SELECT *
FROM customers
WHERE name = 'John Doe'
AND email = 'john@example.com';
```

SQLAlchemy:

```python
statement = select(Customer).where(
    Customer.name == "John Doe",
    Customer.email == "john@example.com"
)
```

This is equivalent to an `AND`.

---

# 17. OR Conditions

Use `or_()`:

```python
from sqlalchemy import or_, select

statement = select(Customer).where(
    or_(
        Customer.name == "John Doe",
        Customer.name == "Jane Smith"
    )
)
```

Equivalent SQL:

```sql
WHERE name = 'John Doe'
   OR name = 'Jane Smith'
```

---

# 18. UPDATE

Suppose we need to change John's email.

First retrieve the object:

```python
with Session(engine) as session:

    customer = session.get(Customer, 1)

    if customer:
        customer.email = "john.doe@example.com"
        session.commit()
```

SQLAlchemy detects that the object changed and generates an `UPDATE`.

Conceptually:

```sql
UPDATE customers
SET email = 'john.doe@example.com'
WHERE id = 1;
```

This is one of the major benefits of ORM.

---

# 19. DELETE

```python
with Session(engine) as session:

    customer = session.get(Customer, 1)

    if customer:
        session.delete(customer)
        session.commit()
```

Equivalent SQL:

```sql
DELETE FROM customers
WHERE id = 1;
```

---

# 20. Complete CRUD Example

```python
from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


DATABASE_URL = "mysql+mysqlconnector://root:password@localhost/shop"

engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))


Base.metadata.create_all(engine)


# CREATE
with Session(engine) as session:
    customer = Customer(
        name="John Doe",
        email="john@example.com"
    )

    session.add(customer)
    session.commit()


# READ
with Session(engine) as session:
    statement = select(Customer)
    customers = session.scalars(statement).all()

    for customer in customers:
        print(customer.id, customer.name, customer.email)


# UPDATE
with Session(engine) as session:
    customer = session.get(Customer, 1)

    if customer:
        customer.email = "new@example.com"
        session.commit()


# DELETE
with Session(engine) as session:
    customer = session.get(Customer, 1)

    if customer:
        session.delete(customer)
        session.commit()
```

---

# 21. ORM Relationships

Real applications rarely have only one table.

Consider an e-commerce application:

```text
customers
    |
    | 1
    |
    | many
    v
orders
    |
    | 1
    |
    | many
    v
order_items
```

For example:

```text
Customer
   |
   +-- Order #1001
   |      |
   |      +-- Product A
   |      +-- Product B
   |
   +-- Order #1002
          |
          +-- Product C
```

SQLAlchemy allows us to represent these relationships using Python objects.

---

# 22. One-to-Many Relationship

Example:

```python
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    orders: Mapped[list["Order"]] = relationship(
        back_populates="customer"
    )


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id")
    )

    customer: Mapped["Customer"] = relationship(
        back_populates="orders"
    )
```

Now we can do:

```python
customer.orders
```

and get the customer's orders.

Or:

```python
order.customer
```

to get the customer associated with an order.

---

# 23. Why Relationships Matter

Without ORM:

```sql
SELECT *
FROM orders
WHERE customer_id = 10;
```

Then another query:

```sql
SELECT *
FROM customers
WHERE id = 10;
```

With ORM:

```python
customer.orders
```

and:

```python
order.customer
```

The relationship becomes part of the application's object model.

---

# 24. Lazy Loading

SQLAlchemy relationships can be loaded when they are accessed.

Example:

```python
customer = session.get(Customer, 1)

print(customer.orders)
```

When `orders` is accessed, SQLAlchemy can execute the required query.

Conceptually:

```text
session.get(Customer, 1)
        |
        v
Customer object
        |
        v
customer.orders
        |
        v
SELECT ... FROM orders
WHERE customer_id = 1
```

This is called **lazy loading**.

---

# 25. Eager Loading

Sometimes we already know that we need related data.

SQLAlchemy provides eager-loading techniques such as:

```python
selectinload()
```

Example:

```python
from sqlalchemy.orm import selectinload

statement = (
    select(Customer)
    .options(selectinload(Customer.orders))
)

customers = session.scalars(statement).all()
```

This can help avoid excessive database queries when processing related data.

---

# 26. The N+1 Query Problem

This is an important real-world ORM problem.

Suppose we retrieve 100 customers:

```python
customers = session.scalars(
    select(Customer)
).all()
```

Then:

```python
for customer in customers:
    print(customer.orders)
```

Depending on the loading strategy, the application may perform:

```text
1 query → customers

+ 100 queries → orders
-----------------------
101 queries
```

This is known as the **N+1 query problem**.

For large applications this can severely affect performance.

Using eager loading can reduce unnecessary queries:

```python
statement = (
    select(Customer)
    .options(selectinload(Customer.orders))
)
```

This is particularly important for your background in **Magento/e-commerce performance optimization**, where inefficient database access can become a major bottleneck.

---

# 27. Transactions

Transactions are critical in production applications.

Example:

```python
with Session(engine) as session:

    try:
        customer = Customer(
            name="John",
            email="john@example.com"
        )

        session.add(customer)

        session.commit()

    except Exception:
        session.rollback()
        raise
```

If something fails:

```python
session.rollback()
```

undoes the uncommitted changes.

Conceptually:

```text
BEGIN
   |
   +-- INSERT customer
   |
   +-- UPDATE order
   |
   +-- INSERT payment
   |
   +-- error
   |
ROLLBACK
```

Without rollback, applications can leave transactions in an undesirable state.

---

# 28. Session vs Connection

This distinction is important for interviews.

| Connection                     | Session                    |
| ------------------------------ | -------------------------- |
| Lower-level database interface | ORM interface              |
| Executes SQL                   | Manages ORM objects        |
| SQLAlchemy Core                | SQLAlchemy ORM             |
| Database-focused               | Application/object-focused |
| Doesn't track ORM objects      | Maintains ORM object state |

Think:

```text
Connection
    ↓
SQL statements

Session
    ↓
Python objects + transactions + ORM
```

---

# 29. ORM vs Raw SQL

| Raw SQL                          | SQLAlchemy ORM                  |
| -------------------------------- | ------------------------------- |
| SQL is written directly          | Python objects are used         |
| More database-specific           | More database abstraction       |
| Full SQL control                 | Higher-level abstraction        |
| Good for complex SQL             | Good for application CRUD       |
| Easy to understand SQL execution | Easier object-based development |
| Can become repetitive            | Reduces repetitive CRUD code    |

ORM does **not** mean SQL becomes unnecessary.

In real applications, you may use both.

For example:

```text
Simple CRUD
     ↓
SQLAlchemy ORM

Complex reporting query
     ↓
SQLAlchemy Core / SQL

Performance-critical query
     ↓
Optimized SQL
```

---

# 30. SQLAlchemy and Magento

This is particularly useful for understanding how SQLAlchemy maps to your existing Magento experience.

Magento uses models and database abstractions heavily.

Conceptually:

```text
Magento
   |
   +-- Model
   +-- Resource Model
   +-- Collection
   |
   v
Database
```

SQLAlchemy:

```text
Python
   |
   +-- ORM Model
   +-- Session
   +-- Query
   |
   v
Database
```

For example, Magento-style thinking:

```php
$customer = $customerRepository->getById($customerId);
```

SQLAlchemy:

```python
customer = session.get(Customer, customer_id)
```

Magento collection-style querying:

```php
$collection->addFieldToFilter(
    'email',
    'john@example.com'
);
```

SQLAlchemy:

```python
statement = select(Customer).where(
    Customer.email == "john@example.com"
)
```

The concepts are different implementations of a similar application/database abstraction.

---

# 31. MySQL vs PostgreSQL

One important goal of this lesson is to make your Python database skills transferable.

Your ORM model can often remain almost identical.

### MySQL

```python
DATABASE_URL = (
    "mysql+mysqlconnector://root:password@localhost/shop"
)

engine = create_engine(DATABASE_URL)
```

### PostgreSQL

```python
DATABASE_URL = (
    "postgresql+psycopg2://postgres:password@localhost/shop"
)

engine = create_engine(DATABASE_URL)
```

The model:

```python
class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))
```

can generally remain unchanged.

That's one of the benefits of using an ORM.

---

# 32. Recommended Project Structure

For your `advanced-python-database` learning repository, use:

```text
advanced-python-database/
│
├── part-4-data-database/
│   │
│   └── lesson-07-sqlalchemy/
│       │
│       ├── README.md
│       │
│       ├── requirements.txt
│       │
│       ├── config.py
│       ├── database.py
│       ├── models.py
│       ├── crud.py
│       └── main.py
│
└── .gitignore
```

---

# 33. `requirements.txt`

```text
SQLAlchemy
mysql-connector-python
psycopg2-binary
```

Install:

```bash
pip install -r requirements.txt
```

---

# 34. `database.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


DATABASE_URL = "mysql+mysqlconnector://root:password@localhost/shop"

engine = create_engine(
    DATABASE_URL,
    echo=True
)


class Base(DeclarativeBase):
    pass
```

`echo=True` is extremely useful while learning because SQLAlchemy prints generated SQL.

For example:

```text
SELECT customers.id,
       customers.name,
       customers.email
FROM customers
```

In production, you normally don't leave SQL logging configured this way.

---

# 35. `models.py`

```python
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    email: Mapped[str] = mapped_column(
        String(255)
    )
```

---

# 36. `main.py`

```python
from sqlalchemy.orm import Session

from database import Base, engine
from models import Customer


Base.metadata.create_all(engine)


with Session(engine) as session:

    customer = Customer(
        name="John Doe",
        email="john@example.com"
    )

    session.add(customer)
    session.commit()

    print(
        customer.id,
        customer.name,
        customer.email
    )
```

Run:

```bash
python main.py
```

---

# 37. Real-World Use Case

Imagine you are building a **JobPilot** backend.

You might have:

```text
candidates
jobs
skills
candidate_skills
applications
resumes
```

Relationships:

```text
Candidate
   |
   +---- Skills
   |
   +---- Resumes
   |
   +---- Applications
              |
              v
             Job
```

Instead of manually writing SQL for every CRUD operation, you could model:

```python
class Candidate(Base):
    ...

class Job(Base):
    ...

class Skill(Base):
    ...

class Application(Base):
    ...
```

Then application code could look like:

```python
candidate = session.get(Candidate, candidate_id)

print(candidate.skills)
print(candidate.resumes)
print(candidate.applications)
```

This becomes particularly useful when we later build APIs using **FastAPI**.

The eventual architecture could be:

```text
                ┌──────────────┐
                │   FastAPI    │
                └──────┬───────┘
                       │
                       v
                ┌──────────────┐
                │ Service Layer│
                └──────┬───────┘
                       │
                       v
                ┌──────────────┐
                │ SQLAlchemy   │
                │     ORM      │
                └──────┬───────┘
                       │
              ┌────────┴────────┐
              v                 v
           MySQL           PostgreSQL
```

This is the kind of architecture we will eventually use when moving toward **AI applications and production AI systems**.

---

# 38. Practical Exercise

Create the following model:

```text
Product
----------------
id
name
sku
price
quantity
```

Requirements:

### CREATE

Insert:

```text
Laptop
LAP-001
75000
10
```

### READ

Retrieve all products.

### FILTER

Find products where:

```text
price > 50000
```

### UPDATE

Change:

```text
quantity = 8
```

### DELETE

Delete a product by ID.

---

# 39. Interview Questions

### Q1. What is ORM?

ORM stands for Object-Relational Mapping. It maps database tables to programming-language objects so developers can interact with relational databases using objects instead of writing SQL for every operation.

---

### Q2. What is SQLAlchemy?

SQLAlchemy is a Python SQL toolkit and ORM that provides both SQL-oriented and object-oriented ways to interact with relational databases.

---

### Q3. What is an SQLAlchemy Engine?

The Engine is the central SQLAlchemy object responsible for communicating with the database and managing database connections through its connection pool.

---

### Q4. What is a Session?

A Session provides the ORM interface for managing objects, executing ORM queries, and coordinating transactions.

---

### Q5. What is `Base` in SQLAlchemy?

`Base` is the declarative base class from which ORM models inherit.

Example:

```python
class Customer(Base):
    ...
```

SQLAlchemy uses this metadata to understand the application's database models.

---

### Q6. What is `mapped_column()`?

`mapped_column()` defines a mapped database column in a SQLAlchemy ORM model.

Example:

```python
id: Mapped[int] = mapped_column(primary_key=True)
```

---

### Q7. What is lazy loading?

Lazy loading means related data is loaded when the relationship is accessed rather than when the original object is initially loaded.

---

### Q8. What is the N+1 query problem?

It occurs when an application executes one query to retrieve a collection of objects and then executes an additional query for each object to retrieve related data.

For 100 objects:

```text
1 + 100 = 101 queries
```

Eager-loading strategies can help avoid this.

---

### Q9. ORM or raw SQL—which should you use?

Neither is universally better.

ORM is useful for application CRUD and object relationships, while raw SQL or SQLAlchemy Core can be preferable for complex queries, reporting, or cases requiring precise SQL control.

---

### Q10. Can SQLAlchemy work with both MySQL and PostgreSQL?

Yes.

Only the database URL/driver configuration generally changes for basic ORM usage:

```text
MySQL      → mysql+mysqlconnector
PostgreSQL → postgresql+psycopg2
```

The ORM models can often remain the same.

---

# 40. What You Should Remember

The most important concepts from Lesson 07 are:

```text
ORM
 ↓
SQLAlchemy
 ↓
Engine
 ↓
Base
 ↓
Model
 ↓
Session
 ↓
CRUD
 ↓
Relationships
 ↓
Transactions
 ↓
Loading Strategies
 ↓
N+1 Problem
```

And the practical mapping:

```text
Python Class      → Database Table
Python Object     → Database Row
Python Attribute  → Database Column
ForeignKey        → Table Relationship
Session           → ORM Transaction/Unit of Work
```

### Lesson 07 Practical Goal

By the end of this lesson, you should be able to build:

```text
Python
  |
  v
SQLAlchemy ORM
  |
  +---- CREATE
  +---- READ
  +---- UPDATE
  +---- DELETE
  |
  +---- Relationships
  +---- Transactions
  |
  +---- MySQL
  +---- PostgreSQL
```

**Next lesson:** **Part 4 — Lesson 08: Database Migrations with Alembic** — why `Base.metadata.create_all()` is not enough for production, how migrations work, and how to safely add/modify database columns without destroying existing data.
