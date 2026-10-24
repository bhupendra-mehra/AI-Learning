# Part 4 — Data & Database Development

# Lesson 07 — Part 2: Build E-Commerce ORM with SQLAlchemy

In Part 1, we learned the basic SQLAlchemy concepts.

In this part, we will build a **real e-commerce database layer** using SQLAlchemy and understand the complete flow:

```text
Python Model
      ↓
SQLAlchemy ORM
      ↓
Base / Metadata
      ↓
MySQL Tables
      ↓
Repository
      ↓
Service Layer
      ↓
Application
```

We will also implement:

* `Customer`
* `Category`
* `Product`
* `Order`
* `OrderItem`
* Foreign keys
* ORM relationships
* `created_at`
* `updated_at`
* Timezone-aware UTC timestamps
* Repository pattern
* Service layer
* Transactions
* Actual MySQL tables
* CRUD operations

---

# 1. E-Commerce Database Design

We will build five main tables:

```text
customers
categories
products
orders
order_items
```

The relationships are:

```text
Category
   │
   │ 1:N
   ▼
Product
   │
   │
   │
Customer ──── 1:N ──── Order
                         │
                         │ 1:N
                         ▼
                    OrderItem
                         │
                         │ N:1
                         ▼
                       Product
```

A real example:

```text
Customer: Bhupendra
       │
       └── Order #1001
              │
              ├── Laptop × 1
              └── Mouse × 2
```

---

# 2. Project Structure

Our Lesson 07 project will use:

```text
lesson-07-sqlalchemy/
│
├── README.md
├── requirements.txt
├── .env
│
├── database.py
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── timestamp_mixin.py
│   ├── customer.py
│   ├── category.py
│   ├── product.py
│   ├── order.py
│   └── order_item.py
│
├── repositories/
│   ├── __init__.py
│   ├── customer_repository.py
│   ├── product_repository.py
│   └── order_repository.py
│
└── services/
    ├── __init__.py
    └── order_service.py
```

This is much closer to a real application than putting everything into `main.py`.

---

# 3. Install Dependencies

Create `requirements.txt`:

```text
SQLAlchemy
mysql-connector-python
python-dotenv
```

Install:

```bash
pip install -r requirements.txt
```

Check:

```bash
pip show sqlalchemy
```

---

# 4. Create the MySQL Database

First connect to MySQL:

```bash
mysql -u root -p
```

Create the database:

```sql
CREATE DATABASE ecommerce;
```

Check:

```sql
SHOW DATABASES;
```

You should see:

```text
ecommerce
```

### Important distinction

We are creating the **database** manually:

```text
ecommerce
```

SQLAlchemy will create the **tables** inside it:

```text
ecommerce
│
├── customers
├── categories
├── products
├── orders
└── order_items
```

---

# 5. Configure Environment Variables

Create:

```text
.env
```

```env
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ecommerce
```

Do not commit `.env` to Git.

Add:

```text
.env
.venv/
__pycache__/
```

to `.gitignore`.

---

# 6. Create `database.py`

Use `URL.create()` rather than manually constructing the connection string.

This is especially important because your MySQL password might contain special characters such as:

```text
@
#
:
/
%
```

Create:

```text
database.py
```

```python
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase

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
```

---

# 7. Understanding `Base`

This is the foundation of our ORM:

```python
class Base(DeclarativeBase):
    pass
```

All SQLAlchemy models will inherit from `Base`.

For example:

```python
class Customer(Base):
    ...
```

```python
class Product(Base):
    ...
```

```python
class Order(Base):
    ...
```

SQLAlchemy registers these models in:

```python
Base.metadata
```

Conceptually:

```text
Base
 │
 └── metadata
       │
       ├── customers
       ├── categories
       ├── products
       ├── orders
       └── order_items
```

Therefore:

```python
Base.metadata.create_all(engine)
```

means:

> Create the database tables represented by the registered SQLAlchemy models if they don't already exist.

---

# 8. Why We Need `created_at` and `updated_at`

Almost every important business table should track when a record was created and last modified.

```text
created_at → When the record was created
updated_at → When the record was last updated
```

Example:

```text
customers
----------------------------------------------------------------
id | name      | email       | created_at        | updated_at
----------------------------------------------------------------
1  | Bhupendra | b@test.com  | 2026-09-20 10:00 | 2026-09-20 10:00
```

After changing the email:

```text
customers
----------------------------------------------------------------
id | name      | email       | created_at        | updated_at
----------------------------------------------------------------
1  | Bhupendra | new@test.com| 2026-09-20 10:00 | 2026-09-20 11:30
```

Notice:

```text
created_at → unchanged
updated_at → changed
```

---

# 9. Important: Don't Use `datetime.utcnow()`

In modern Python, this:

```python
datetime.utcnow()
```

is deprecated.

Instead use timezone-aware UTC:

```python
from datetime import datetime, timezone

datetime.now(timezone.utc)
```

This gives a timezone-aware datetime.

---

# 10. Create `TimestampMixin`

We don't want to repeat `created_at` and `updated_at` in every model.

Create:

```text
models/timestamp_mixin.py
```

```python
from datetime import datetime, timezone

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


class TimestampMixin:

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )
```

---

# 11. Why Are We Using `lambda`?

Don't write:

```python
default=datetime.now(timezone.utc)
```

because that evaluates the time when the model definition is loaded.

Instead:

```python
default=lambda: datetime.now(timezone.utc)
```

means:

> Call this function when SQLAlchemy actually needs the value.

Similarly:

```python
onupdate=lambda: datetime.now(timezone.utc)
```

means:

> Generate a new timestamp when the ORM object is updated.

---

# 12. Timestamp Flow

When creating:

```text
INSERT
  │
  ├── created_at = current UTC time
  └── updated_at = current UTC time
```

When updating:

```text
UPDATE
  │
  ├── created_at = unchanged
  └── updated_at = current UTC time
```

Example:

```text
Create:
created_at = 2026-09-20 10:00 UTC
updated_at = 2026-09-20 10:00 UTC

Update:
created_at = 2026-09-20 10:00 UTC
updated_at = 2026-09-20 11:30 UTC
```

---

# 13. Customer Model

Create:

```text
models/customer.py
```

```python
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from models.timestamp_mixin import TimestampMixin


class Customer(TimestampMixin, Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    orders: Mapped[list["Order"]] = relationship(
        back_populates="customer"
    )
```

The table becomes:

```text
customers
--------------------------------
id
name
email
created_at
updated_at
```

---

# 14. Category Model

Create:

```text
models/category.py
```

```python
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from models.timestamp_mixin import TimestampMixin


class Category(TimestampMixin, Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    products: Mapped[list["Product"]] = relationship(
        back_populates="category"
    )
```

Table:

```text
categories
--------------------------------
id
name
created_at
updated_at
```

---

# 15. Product Model

Create:

```text
models/product.py
```

```python
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from models.timestamp_mixin import TimestampMixin


class Product(TimestampMixin, Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    sku: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        nullable=False,
        default=0
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )

    category: Mapped["Category"] = relationship(
        back_populates="products"
    )

    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="product"
    )
```

Table:

```text
products
--------------------------------
id
name
sku
price
quantity
category_id
created_at
updated_at
```

---

# 16. Understanding `ForeignKey`

This:

```python
category_id: Mapped[int] = mapped_column(
    ForeignKey("categories.id"),
    nullable=False
)
```

creates the relationship:

```text
products.category_id
        │
        ▼
categories.id
```

Conceptually MySQL gets:

```sql
FOREIGN KEY (category_id)
REFERENCES categories(id)
```

This maintains referential integrity.

---

# 17. Order Model

Create:

```text
models/order.py
```

```python
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from models.timestamp_mixin import TimestampMixin


class Order(TimestampMixin, Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id"),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="pending"
    )

    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=0
    )

    customer: Mapped["Customer"] = relationship(
        back_populates="orders"
    )

    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order"
    )
```

Table:

```text
orders
--------------------------------
id
customer_id
status
total_amount
created_at
updated_at
```

---

# 18. Order Item Model

Create:

```text
models/order_item.py
```

```python
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from models.timestamp_mixin import TimestampMixin


class OrderItem(TimestampMixin, Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id"),
        nullable=False
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        nullable=False
    )

    unit_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    order: Mapped["Order"] = relationship(
        back_populates="items"
    )

    product: Mapped["Product"] = relationship(
        back_populates="order_items"
    )
```

Table:

```text
order_items
--------------------------------
id
order_id
product_id
quantity
unit_price
created_at
updated_at
```

---

# 19. Model Relationships

We now have:

```text
Customer
   │
   │ 1:N
   ▼
Order
   │
   │ 1:N
   ▼
OrderItem
   │
   │ N:1
   ▼
Product
   │
   │ N:1
   ▼
Category
```

In Python:

```python
customer.orders
```

gets orders.

```python
order.customer
```

gets the customer.

```python
order.items
```

gets order items.

```python
item.product
```

gets the product.

```python
product.category
```

gets the category.

This is the major benefit of ORM relationships.

---

# 20. Register All Models

Create:

```text
models/__init__.py
```

```python
from .customer import Customer
from .category import Category
from .product import Product
from .order import Order
from .order_item import OrderItem
```

This ensures all models are imported and registered before:

```python
Base.metadata.create_all(engine)
```

---

# 21. Create the Tables

Now create:

```text
main.py
```

```python
from database import Base, engine

from models import (
    Customer,
    Category,
    Product,
    Order,
    OrderItem,
)


Base.metadata.create_all(engine)

print("Tables created successfully.")
```

Run:

```bash
python main.py
```

Because:

```python
echo=True
```

is enabled, SQLAlchemy will display SQL statements in the terminal.

Conceptually:

```text
CREATE TABLE customers ...
CREATE TABLE categories ...
CREATE TABLE products ...
CREATE TABLE orders ...
CREATE TABLE order_items ...
```

---

# 22. Verify Tables in MySQL

Connect:

```bash
mysql -u root -p
```

Then:

```sql
USE ecommerce;

SHOW TABLES;
```

Expected:

```text
customers
categories
products
orders
order_items
```

---

# 23. Check the Timestamp Columns

Run:

```sql
DESCRIBE customers;
```

You should see:

```text
id
name
email
created_at
updated_at
```

And:

```sql
DESCRIBE products;
```

should show:

```text
id
name
sku
price
quantity
category_id
created_at
updated_at
```

---

# 24. Important: `create_all()` Is Not a Migration Tool

At this stage:

```python
Base.metadata.create_all(engine)
```

is excellent for learning and initial table creation.

But imagine the database already contains:

```text
products
----------------
id
name
price
```

Then you modify the model:

```python
description: Mapped[str]
```

Running:

```python
Base.metadata.create_all(engine)
```

is **not a complete schema migration mechanism**.

It doesn't manage existing schema changes the way a production migration system does.

That's why we will later use:

```text
Alembic
```

for migrations.

---

# 25. Customer Repository

Now we introduce the **Repository Pattern**.

Create:

```text
repositories/customer_repository.py
```

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.customer import Customer


class CustomerRepository:

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        name: str,
        email: str
    ) -> Customer:

        customer = Customer(
            name=name,
            email=email
        )

        self.session.add(customer)
        self.session.flush()

        return customer

    def get_by_id(
        self,
        customer_id: int
    ) -> Customer | None:

        return self.session.get(
            Customer,
            customer_id
        )

    def get_by_email(
        self,
        email: str
    ) -> Customer | None:

        statement = select(Customer).where(
            Customer.email == email
        )

        return self.session.scalars(
            statement
        ).first()

    def get_all(self) -> list[Customer]:

        statement = select(Customer)

        return list(
            self.session.scalars(statement).all()
        )

    def delete(
        self,
        customer_id: int
    ) -> bool:

        customer = self.get_by_id(customer_id)

        if not customer:
            return False

        self.session.delete(customer)

        return True
```

---

# 26. Why Do We Need a Repository?

Without a repository, we might write SQLAlchemy code throughout our application:

```text
API
 ↓
SQLAlchemy
 ↓
Database
```

This makes database logic spread throughout the application.

With Repository:

```text
API
 ↓
Service
 ↓
Repository
 ↓
SQLAlchemy
 ↓
Database
```

The repository handles persistence.

For example:

```python
customer = customer_repository.get_by_email(
    "bhupendra@example.com"
)
```

instead of repeatedly writing:

```python
statement = select(Customer).where(
    Customer.email == email
)
```

---

# 27. Model vs Repository

Remember this distinction:

```text
Model
 ↓
What the data looks like
```

```text
Repository
 ↓
How data is retrieved and persisted
```

Example:

```text
Customer Model
      ↓
customers table

CustomerRepository
      ↓
create customer
get customer
update customer
delete customer
```

---

# 28. Why Does the Repository Use `flush()`?

We use:

```python
self.session.add(customer)
self.session.flush()
```

rather than:

```python
self.session.commit()
```

`flush()` sends the SQL to the database but keeps the transaction open.

This means we can get the generated ID:

```python
customer.id
```

while still allowing the caller to decide when to commit.

For example:

```python
customer = repository.create(...)
product = repository.create(...)

session.commit()
```

Both operations can belong to the same transaction.

---

# 29. Product Repository

Create:

```text
repositories/product_repository.py
```

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.product import Product


class ProductRepository:

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        name: str,
        sku: str,
        price,
        quantity: int,
        category_id: int
    ) -> Product:

        product = Product(
            name=name,
            sku=sku,
            price=price,
            quantity=quantity,
            category_id=category_id
        )

        self.session.add(product)
        self.session.flush()

        return product

    def get_by_id(
        self,
        product_id: int
    ) -> Product | None:

        return self.session.get(
            Product,
            product_id
        )

    def get_by_sku(
        self,
        sku: str
    ) -> Product | None:

        statement = select(Product).where(
            Product.sku == sku
        )

        return self.session.scalars(
            statement
        ).first()

    def get_all(self) -> list[Product]:

        statement = select(Product)

        return list(
            self.session.scalars(statement).all()
        )
```

---

# 30. Create Customer, Category and Products

Let's create real data.

```python
from decimal import Decimal

from sqlalchemy.orm import Session

from database import engine
from models.category import Category
from repositories.customer_repository import CustomerRepository
from repositories.product_repository import ProductRepository


with Session(engine) as session:

    customer_repository = CustomerRepository(session)
    product_repository = ProductRepository(session)

    customer = customer_repository.create(
        name="Bhupendra",
        email="bhupendra@example.com"
    )

    category = Category(
        name="Electronics"
    )

    session.add(category)
    session.flush()

    laptop = product_repository.create(
        name="Laptop",
        sku="LAP-001",
        price=Decimal("75000.00"),
        quantity=10,
        category_id=category.id
    )

    mouse = product_repository.create(
        name="Wireless Mouse",
        sku="MOU-001",
        price=Decimal("1500.00"),
        quantity=25,
        category_id=category.id
    )

    keyboard = product_repository.create(
        name="Keyboard",
        sku="KEY-001",
        price=Decimal("3000.00"),
        quantity=15,
        category_id=category.id
    )

    session.commit()

    print(customer.id)
    print(laptop.id)
    print(mouse.id)
    print(keyboard.id)
```

---

# 31. What Happens Behind the Scenes?

When you write:

```python
customer = Customer(
    name="Bhupendra",
    email="bhupendra@example.com"
)
```

you create a Python object.

Then:

```python
session.add(customer)
```

registers it with SQLAlchemy.

Then:

```python
session.commit()
```

causes SQLAlchemy to generate an `INSERT`.

Conceptually:

```sql
INSERT INTO customers
    (name, email, created_at, updated_at)
VALUES
    (
        'Bhupendra',
        'bhupendra@example.com',
        ...,
        ...
    );
```

So:

```text
Python Object
      ↓
session.add()
      ↓
SQLAlchemy Session
      ↓
INSERT SQL
      ↓
MySQL
      ↓
customers table
```

---

# 32. Verify the Timestamps

Run:

```sql
SELECT
    id,
    name,
    email,
    created_at,
    updated_at
FROM customers;
```

You should see something similar to:

```text
1 | Bhupendra | bhupendra@example.com
  | 2026-09-20 10:00:00
  | 2026-09-20 10:00:00
```

The exact time will depend on your system/database timezone handling.

---

# 33. Test `updated_at`

Now retrieve a customer:

```python
with Session(engine) as session:

    repository = CustomerRepository(session)

    customer = repository.get_by_email(
        "bhupendra@example.com"
    )

    if customer:
        customer.name = "Bhupendra Mehra"

        session.commit()

        print(customer.created_at)
        print(customer.updated_at)
```

The expected behavior is:

```text
created_at → original time
updated_at → newer time
```

This is an important SQLAlchemy concept.

---

# 34. Order Repository

Create:

```text
repositories/order_repository.py
```

```python
from decimal import Decimal

from sqlalchemy.orm import Session

from models.order import Order
from models.order_item import OrderItem


class OrderRepository:

    def __init__(self, session: Session):
        self.session = session

    def create_order(
        self,
        customer_id: int
    ) -> Order:

        order = Order(
            customer_id=customer_id,
            status="pending",
            total_amount=Decimal("0.00")
        )

        self.session.add(order)
        self.session.flush()

        return order

    def add_item(
        self,
        order_id: int,
        product_id: int,
        quantity: int,
        unit_price
    ) -> OrderItem:

        item = OrderItem(
            order_id=order_id,
            product_id=product_id,
            quantity=quantity,
            unit_price=unit_price
        )

        self.session.add(item)
        self.session.flush()

        return item
```

---

# 35. Create an Order

Now:

```python
from sqlalchemy.orm import Session

from database import engine
from repositories.customer_repository import CustomerRepository
from repositories.product_repository import ProductRepository
from repositories.order_repository import OrderRepository


with Session(engine) as session:

    customer_repository = CustomerRepository(session)
    product_repository = ProductRepository(session)
    order_repository = OrderRepository(session)

    customer = customer_repository.get_by_email(
        "bhupendra@example.com"
    )

    laptop = product_repository.get_by_sku(
        "LAP-001"
    )

    if customer and laptop:

        order = order_repository.create_order(
            customer.id
        )

        order_repository.add_item(
            order_id=order.id,
            product_id=laptop.id,
            quantity=1,
            unit_price=laptop.price
        )

        order.total_amount = laptop.price
        order.status = "confirmed"

        session.commit()

        print("Order created:", order.id)
```

---

# 36. Database Result

We should now have something like:

```text
customers
------------------------------------------------
id | name      | email
1  | Bhupendra  | bhupendra@example.com


categories
------------------------------------------------
id | name
1  | Electronics


products
------------------------------------------------
id | name            | sku     | price
1  | Laptop          | LAP-001 | 75000
2  | Wireless Mouse  | MOU-001 | 1500
3  | Keyboard        | KEY-001 | 3000


orders
------------------------------------------------
id | customer_id | status    | total_amount
1  | 1           | confirmed | 75000


order_items
------------------------------------------------
id | order_id | product_id | quantity | unit_price
1  | 1        | 1          | 1        | 75000
```

Every table also has:

```text
created_at
updated_at
```

---

# 37. Using ORM Relationships

Now the interesting part.

Because we defined:

```python
customer.orders
```

we can do:

```python
customer = session.get(Customer, 1)

for order in customer.orders:
    print(order.id)
```

And:

```python
order.items
```

gets the order items:

```python
for item in order.items:
    print(item.product.name)
```

So the application can navigate:

```text
customer
   ↓
customer.orders
   ↓
order.items
   ↓
item.product
   ↓
product.category
```

This is ORM in action.

---

# 38. Repository + ORM Relationship

The Repository retrieves the object:

```python
customer = customer_repository.get_by_id(1)
```

The ORM relationship lets us navigate:

```python
customer.orders
```

So:

```text
Repository
    ↓
Customer object
    ↓
ORM relationship
    ↓
Orders
```

The repository doesn't need to manually build every SQL query for related objects.

---

# 39. Why We Need a Service Layer

We currently have:

```text
Application
     ↓
Repository
     ↓
SQLAlchemy
     ↓
MySQL
```

But business logic should not live in the repository.

For example:

> Can the customer purchase 5 laptops if only 2 are available?

That's business logic.

So we introduce:

```text
Application
     ↓
Service
     ↓
Repository
     ↓
SQLAlchemy
     ↓
MySQL
```

---

# 40. Order Service

Create:

```text
services/order_service.py
```

```python
from sqlalchemy.orm import Session

from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository


class OrderService:

    def __init__(self, session: Session):

        self.session = session

        self.order_repository = OrderRepository(
            session
        )

        self.product_repository = ProductRepository(
            session
        )

    def create_order(
        self,
        customer_id: int,
        product_id: int,
        quantity: int
    ):

        product = self.product_repository.get_by_id(
            product_id
        )

        if not product:
            raise ValueError(
                "Product not found"
            )

        if product.quantity < quantity:
            raise ValueError(
                "Insufficient stock"
            )

        order = self.order_repository.create_order(
            customer_id
        )

        total = product.price * quantity

        self.order_repository.add_item(
            order_id=order.id,
            product_id=product.id,
            quantity=quantity,
            unit_price=product.price
        )

        product.quantity -= quantity

        order.total_amount = total
        order.status = "confirmed"

        self.session.commit()

        return order
```

---

# 41. What Is the Service Doing?

The Service handles **business rules**:

```text
1. Find product
2. Check product exists
3. Check stock
4. Create order
5. Create order item
6. Calculate total
7. Reduce inventory
8. Confirm order
9. Commit transaction
```

The Repository handles persistence:

```text
Get product
Create order
Create order item
```

That's the separation we want.

---

# 42. Final Order Flow

Now the application only needs:

```python
with Session(engine) as session:

    service = OrderService(session)

    order = service.create_order(
        customer_id=1,
        product_id=1,
        quantity=2
    )

    print("Order created:", order.id)
```

The complete flow:

```text
Application
     │
     ▼
OrderService
     │
     ├── ProductRepository
     │       │
     │       ▼
     │   SQLAlchemy
     │
     ├── Check stock
     │
     ├── Calculate total
     │
     ├── Create Order
     │
     ├── Create OrderItem
     │
     ├── Reduce stock
     │
     └── Commit
             │
             ▼
           MySQL
```

---

# 43. Transaction Management

An order is a perfect example of why transactions matter.

We have:

```text
Create Order
      +
Create OrderItem
      +
Reduce Product Stock
      +
Update Order Total
```

These operations should succeed together.

```text
BEGIN
 │
 ├── Create Order
 ├── Create OrderItem
 ├── Reduce Stock
 └── Update Total
 │
COMMIT
```

If something goes wrong:

```text
BEGIN
 │
 ├── Create Order ✓
 ├── Create OrderItem ✓
 ├── Reduce Stock ✓
 └── ERROR ✗
       │
       ▼
    ROLLBACK
```

This prevents partially completed orders.

---

# 44. Model vs Repository vs Service

This is one of the most important things to understand.

| Layer           | Responsibility                 |
| --------------- | ------------------------------ |
| Model           | Represents database structure  |
| Repository      | Database persistence/retrieval |
| Service         | Business logic                 |
| Application/API | Handles requests               |

Think:

```text
Customer
   ↓
What does the customer data look like?

CustomerRepository
   ↓
How do I save/find the customer?

OrderService
   ↓
What rules apply when placing an order?

API
   ↓
What request did the user send?
```

---

# 45. Complete Architecture

Our e-commerce application now looks like:

```text
                       APPLICATION
                            │
                            ▼
                       SERVICE LAYER
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
        Customer Repo   Product Repo   Order Repo
              │             │             │
              └─────────────┼─────────────┘
                            ▼
                       SQLAlchemy ORM
                            │
                            ▼
                          Session
                            │
                            ▼
                           MySQL
                            │
       ┌────────────────────┼─────────────────────┐
       ▼                    ▼                     ▼
   customers            products               orders
                                                   │
                                                   ▼
                                             order_items
```

And:

```text
Category
   │
   └── Products

Customer
   │
   └── Orders
          │
          └── OrderItems
                 │
                 └── Products
```

---

# 46. Complete Data Flow

Let's put everything together.

Suppose the user wants to buy:

```text
Laptop × 1
Mouse × 2
```

The application receives:

```text
customer_id = 1
products:
    Laptop × 1
    Mouse × 2
```

Then:

```text
Application
     ↓
OrderService
     ↓
ProductRepository
     ↓
SQLAlchemy
     ↓
MySQL
```

The service checks:

```text
Laptop stock = 10
Requested = 1
       ↓
Available ✓
```

```text
Mouse stock = 25
Requested = 2
       ↓
Available ✓
```

Then:

```text
Order
   ↓
OrderItem: Laptop × 1
   ↓
OrderItem: Mouse × 2
   ↓
Calculate total
   ↓
Reduce inventory
   ↓
COMMIT
```

---

# 47. Why `Decimal` for Money?

Notice that we use:

```python
from decimal import Decimal
```

and:

```python
Numeric(10, 2)
```

rather than:

```python
float
```

For example:

```python
price = Decimal("75000.00")
```

Database:

```text
Numeric(10,2)
```

This is important because financial values should generally not rely on binary floating-point arithmetic.

For example, floating-point arithmetic can produce values such as:

```text
0.1 + 0.2 = 0.30000000000000004
```

For e-commerce prices, use appropriate decimal/numeric types.

---

# 48. DateTime Flow

Our timestamp implementation is now:

```text
Python
   │
   ▼
datetime.now(timezone.utc)
   │
   ▼
SQLAlchemy DateTime(timezone=True)
   │
   ▼
Database DATETIME/TIMESTAMP representation
```

Our Python model:

```python
created_at: Mapped[datetime]
```

maps to a database date/time column.

This gives us experience with:

* Python `datetime`
* timezone-aware datetimes
* SQLAlchemy `DateTime`
* database timestamps
* creation timestamps
* update timestamps

---

# 49. Why UTC?

Imagine your application is used by:

```text
India
USA
UK
Australia
```

We don't want to store application events using arbitrary local times.

Instead:

```text
Database
   ↓
UTC
```

Then the application converts UTC into the user's local timezone when needed.

Example:

```text
Database:
2026-09-20 06:00 UTC

India:
2026-09-20 11:30 IST
```

This becomes especially important for distributed applications and cloud systems.

---

# 50. Soft Delete — Important Future Concept

Many e-commerce applications don't physically delete important business records.

Instead of:

```sql
DELETE FROM products
WHERE id = 10;
```

they may use:

```text
deleted_at
```

Example:

```text
id | name   | deleted_at
---+--------+---------------------
10 | Laptop | NULL
```

After soft deletion:

```text
id | name   | deleted_at
---+--------+---------------------
10 | Laptop | 2026-09-20 12:00:00
```

The record remains in the database but is treated as deleted by the application.

We don't need to implement this in Lesson 07, but it's an important production concept.

---

# 51. `create_all()` vs Production Migrations

Our development setup currently uses:

```python
Base.metadata.create_all(engine)
```

This is useful for:

```text
Learning
Local experiments
Initial prototypes
```

But production applications need proper schema migration management.

For example, later we might change:

```text
products
----------------
id
name
price
```

to:

```text
products
----------------
id
name
description
price
quantity
stock_status
created_at
updated_at
```

We shouldn't simply drop and recreate the table.

Instead:

```text
SQLAlchemy Model
       ↓
Alembic
       ↓
Migration Script
       ↓
ALTER TABLE
       ↓
Existing MySQL Database
```

That's what we'll learn next.

---

# 52. Final Project Structure

After completing this lesson, your directory should look like:

```text
lesson-07-sqlalchemy/
│
├── README.md
├── requirements.txt
├── .env
│
├── database.py
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── timestamp_mixin.py
│   ├── customer.py
│   ├── category.py
│   ├── product.py
│   ├── order.py
│   └── order_item.py
│
├── repositories/
│   ├── __init__.py
│   ├── customer_repository.py
│   ├── product_repository.py
│   └── order_repository.py
│
└── services/
    ├── __init__.py
    └── order_service.py
```

---

# 53. Complete Flow to Remember

This is the most important diagram from Lesson 07:

```text
                    PYTHON APPLICATION
                           │
                           ▼
                    SERVICE LAYER
                           │
                           ▼
                    REPOSITORY LAYER
                           │
                           ▼
                    SQLALCHEMY ORM
                           │
                    ┌──────┴──────┐
                    │             │
                    ▼             ▼
                  Model         Session
                    │             │
                    └──────┬──────┘
                           ▼
                       Metadata
                           │
                           ▼
                     MySQL Database
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
      customers        products           orders
          │                                   │
          │                                   ▼
          │                              order_items
          │                                   │
          └──────────── relationships ────────┘
```

---

# 54. What You Should Be Able to Explain After Lesson 07

You should now be able to answer:

### What is `Base`?

The common foundation for SQLAlchemy ORM models and the owner of the model metadata.

### What is a Model?

A Python class mapped to a database table.

### What is `Mapped`?

SQLAlchemy's typed ORM mapping annotation used to describe mapped attributes.

### What is `mapped_column()`?

It defines how a Python attribute maps to a database column.

### What is `ForeignKey`?

It establishes a database-level relationship between tables.

### What is `relationship()`?

It defines how related ORM objects can be navigated from Python.

### What is a Session?

It manages ORM objects, database operations, and transactions.

### What is a Repository?

A layer responsible for database persistence and retrieval.

### What is a Service?

A layer responsible for business rules and workflows.

### What are `created_at` and `updated_at`?

Audit timestamps that track when a record was created and last modified.

### Why use UTC?

To provide a consistent time reference across systems, servers, and geographical regions.

### Why use `Decimal`?

To represent monetary values accurately instead of relying on binary floating-point arithmetic.

---

# 55. Practical Assignment

Before moving to Lesson 08, implement this yourself.

### Step 1 — Create the database

```sql
CREATE DATABASE ecommerce;
```

### Step 2 — Create the five models

```text
Customer
Category
Product
Order
OrderItem
```

### Step 3 — Add timestamps

Every model should have:

```text
created_at
updated_at
```

using the reusable:

```python
TimestampMixin
```

### Step 4 — Create the tables

Run:

```python
Base.metadata.create_all(engine)
```

### Step 5 — Verify MySQL

```sql
SHOW TABLES;
```

Then:

```sql
DESCRIBE customers;
DESCRIBE categories;
DESCRIBE products;
DESCRIBE orders;
DESCRIBE order_items;
```

### Step 6 — Create data

```text
Customer:
    Bhupendra

Category:
    Electronics

Products:
    Laptop       ₹75,000
    Mouse        ₹1,500
    Keyboard     ₹3,000
```

### Step 7 — Create an order

```text
Customer:
    Bhupendra

Order:
    Laptop × 1
    Mouse × 2

Total:
    ₹78,000
```

### Step 8 — Verify timestamps

Create a record and note:

```text
created_at
updated_at
```

Then update the record and verify:

```text
created_at → unchanged
updated_at → changed
```

### Step 9 — Verify the actual database

```sql
SELECT * FROM customers;
SELECT * FROM categories;
SELECT * FROM products;
SELECT * FROM orders;
SELECT * FROM order_items;
```

---

# Lesson 07 — Final Mental Model

Don't remember SQLAlchemy as just a collection of commands.

Remember this:

```text
MODEL
"What does my data look like?"
        ↓
ORM
"How does Python map to SQL?"
        ↓
METADATA
"What tables/models exist?"
        ↓
SESSION
"How do I interact with the database?"
        ↓
REPOSITORY
"How do I persist/retrieve data?"
        ↓
SERVICE
"What business rules apply?"
        ↓
DATABASE
"Where is the data stored?"
```

For our e-commerce project:

```text
Customer Model
       ↓
customers table

Product Model
       ↓
products table

Order Model
       ↓
orders table

OrderItem Model
       ↓
order_items table
```

with:

```text
ForeignKey
    ↓
Database relationships

relationship()
    ↓
Python object relationships

TimestampMixin
    ↓
created_at / updated_at

Repository
    ↓
Database operations

Service
    ↓
Business logic

Session
    ↓
Transaction management
```

**After this implementation, Lesson 08 — Database Migrations with Alembic will build directly on this exact project.** We'll take these existing e-commerce tables and learn how to safely modify them, add columns, create indexes, change constraints, generate migrations, apply migrations, roll them back, and understand why migrations are necessary in production.
