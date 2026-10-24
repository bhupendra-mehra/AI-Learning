# Lesson 05 — Database Design

In Lessons 01–04, we learned how databases work and how to query them.

Now we move to an important **senior-level skill**:

> **How do you design a database correctly before writing the application code?**

This is especially important for Magento, APIs, backend systems, reporting, and AI/data pipelines.

---

# 1. Database Design Process

A typical database design process is:

```text
Business Requirements
        ↓
Identify Entities
        ↓
Identify Attributes
        ↓
Define Relationships
        ↓
Define Primary Keys
        ↓
Define Foreign Keys
        ↓
Normalize Data
        ↓
Add Constraints
        ↓
Add Indexes
        ↓
Create Schema
        ↓
Optimize Based on Real Queries
```

Don't start by randomly creating tables.

Start with the **business requirements**.

---

# 2. Entity

An **entity** is something important that needs to be represented in the system.

For our e-commerce application:

```text
Customer
Product
Category
Order
Order Item
Payment
```

Each can become a table.

For example:

```text
Customer → customers
Product  → products
Order    → orders
```

---

# 3. Attributes

An entity has properties.

For `Customer`:

```text
Customer
├── id
├── first_name
├── last_name
├── email
├── phone
└── created_at
```

These properties become columns.

So:

```sql
CREATE TABLE customers (
    id BIGINT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    phone VARCHAR(30),
    created_at DATETIME
);
```

---

# 4. Primary Key

Every important entity should have a way to uniquely identify a record.

Example:

```text
customers.id
products.id
orders.id
```

For example:

```text
Customer ID = 101
```

uniquely identifies that customer.

### Good Primary Key Characteristics

A primary key should generally be:

* unique
* stable
* non-null
* efficient for indexing
* simple to reference

A common choice is:

```sql
id BIGINT PRIMARY KEY
```

For very large systems, `BIGINT` gives much more room than `INT`.

---

# 5. Foreign Key

A foreign key connects tables.

Example:

```text
orders.customer_id
        ↓
customers.id
```

Conceptually:

```sql
customer_id BIGINT,
FOREIGN KEY (customer_id)
    REFERENCES customers(id)
```

This establishes a relationship between the tables.

---

# 6. One-to-One Relationship

Example:

```text
Customer
   │
   │ 1:1
   ▼
Customer Profile
```

Possible schema:

```text
customers
-----------
id
name

customer_profiles
-----------------
id
customer_id
address
date_of_birth
```

`customer_profiles.customer_id` can have a `UNIQUE` constraint:

```sql
UNIQUE (customer_id)
```

This prevents one customer from having multiple profile rows.

### Real-world examples

* User → User Profile
* Employee → Employee Details
* Order → certain types of order metadata

---

# 7. One-to-Many

This is one of the most common relationships.

```text
Customer
   │
   │ 1:N
   ▼
Orders
```

One customer:

```text
Customer 1
   ├── Order 1001
   ├── Order 1002
   └── Order 1003
```

The foreign key belongs on the **many side**:

```text
orders.customer_id
```

Remember:

> In a one-to-many relationship, the foreign key normally goes into the "many" table.

---

# 8. Many-to-Many

Suppose:

```text
Orders ↔ Products
```

One order can contain multiple products.

One product can appear in many orders.

Therefore:

```text
Orders N:N Products
```

Relational databases typically resolve this using a junction/intermediate table:

```text
orders
   │
   ▼
order_items
   ▲
   │
products
```

`order_items` contains:

```text
order_id
product_id
quantity
unit_price
```

This is a very important database design pattern.

---

# 9. Composite Unique Constraint

Suppose an `order_items` table should not contain the exact same product twice within one order.

We could use:

```sql
UNIQUE(order_id, product_id)
```

This means:

```text
Order 1001 + Product 101
```

can appear only once.

However, whether you want this constraint depends on the business model. Some systems intentionally allow multiple lines for the same SKU due to promotions, bundles, fulfillment, or other business rules.

That's an important senior-level point:

> **Database constraints should enforce actual business rules, not assumptions.**

---

# 10. Normalization

Normalization helps reduce unnecessary duplication and inconsistencies.

Consider this bad design:

```text
orders
---------------------------------------------------
order_id
customer_name
customer_email
product_name
product_price
category_name
quantity
```

Suppose customer Bhupendra has 50 orders.

His:

```text
name
email
```

may be repeated many times.

Instead:

```text
customers
orders
order_items
products
categories
```

Each piece of information has a logical home.

---

# 11. First Normal Form — 1NF

A simplified rule:

> Each column should contain atomic values rather than a list of values.

Bad:

```text
customer_id | products
1           | Laptop, Mouse, Keyboard
```

Better:

```text
order_items
-----------------------
order_id | product_id
1001     | 101
1001     | 102
1001     | 103
```

Each row represents one relationship.

---

# 12. Second Normal Form — 2NF

2NF is mainly relevant when you have composite keys.

The idea is:

> Non-key attributes should depend on the whole key, not just part of it.

For example, imagine:

```text
order_id
product_id
product_name
quantity
```

If the logical key is:

```text
(order_id, product_id)
```

then:

```text
quantity
```

depends on both.

But:

```text
product_name
```

depends only on:

```text
product_id
```

So product information belongs in:

```text
products
```

rather than being duplicated in every order-item row.

---

# 13. Third Normal Form — 3NF

Simplified rule:

> Non-key columns should depend on the key, not on another non-key column.

Example:

```text
products
-----------------------
id
category_id
category_name
```

`category_name` depends on:

```text
category_id
```

not directly on:

```text
product.id
```

So move category information into:

```text
categories
```

Then:

```text
products.category_id
        ↓
categories.id
```

---

# 14. Normalization vs Denormalization

Normalization is not always the answer.

### Normalized

```text
customers
orders
order_items
products
categories
```

Advantages:

* less duplication
* better consistency
* easier updates
* cleaner relationships

### Denormalized

Sometimes we intentionally duplicate data for performance or historical correctness.

For example:

```text
order_items.unit_price
```

even though:

```text
products.price
```

already exists.

Why?

Because the product price may change.

So:

```text
products.price = current price
order_items.unit_price = price at purchase time
```

This is a practical form of storing historical snapshot data.

---

# 15. Indexes

Indexes are critical for database performance.

Imagine:

```text
orders
```

contains:

```text
50 million rows
```

Query:

```sql
SELECT *
FROM orders
WHERE customer_id = 100;
```

Without an appropriate index, the database may need to examine many rows.

An index can make lookup much more efficient.

---

# 16. Creating an Index

```sql
CREATE INDEX idx_orders_customer_id
ON orders(customer_id);
```

Now the database has an index on:

```text
customer_id
```

---

# 17. When Should We Index?

Good candidates often include columns frequently used in:

```text
WHERE
JOIN
ORDER BY
GROUP BY
```

For example:

```text
orders.customer_id
orders.created_at
orders.status
order_items.order_id
order_items.product_id
products.category_id
```

But don't blindly index everything.

---

# 18. Why Not Index Every Column?

Indexes have a cost.

They:

* consume storage
* slow down `INSERT`
* slow down `UPDATE`
* slow down `DELETE`
* increase maintenance overhead

Think of an index as:

> A tool that makes specific access patterns faster.

Not:

> Something every column should automatically have.

---

# 19. Composite Index

Suppose we frequently run:

```sql
SELECT *
FROM orders
WHERE customer_id = 100
AND status = 'complete';
```

A composite index may help:

```sql
CREATE INDEX idx_orders_customer_status
ON orders(customer_id, status);
```

The **column order matters**.

For example:

```text
(customer_id, status)
```

is not automatically equivalent to:

```text
(status, customer_id)
```

We'll explore this much more in **Lesson 08 — Database Performance**.

---

# 20. UNIQUE Constraint

A `UNIQUE` constraint prevents duplicate values.

For example, customer email:

```sql
email VARCHAR(255) UNIQUE
```

Then:

```text
user@example.com
```

cannot appear twice if the business rule requires email uniqueness.

Another common example:

```text
products.sku
```

SKU is typically unique.

---

# 21. NOT NULL

Use `NOT NULL` when a value must exist.

Example:

```sql
name VARCHAR(255) NOT NULL
```

This prevents:

```text
name = NULL
```

when the business rule requires a product name.

---

# 22. DEFAULT

You can provide a default value.

Example:

```sql
status VARCHAR(30) DEFAULT 'pending'
```

If the application doesn't provide a status:

```text
pending
```

is used.

---

# 23. CHECK Constraint

A `CHECK` constraint can enforce a rule.

Example:

```sql
price DECIMAL(12,2) CHECK (price >= 0)
```

Conceptually:

```text
price = 5000   ✅
price = 0      ✅
price = -100   ❌
```

Database support and behavior can vary by database/version, so always verify against the specific database engine you're using.

---

# 24. Foreign Key Constraints

Example:

```sql
FOREIGN KEY (customer_id)
REFERENCES customers(id)
```

This protects referential integrity.

Suppose:

```text
customers
id = 1
```

exists.

Then:

```text
orders.customer_id = 1
```

is valid.

But:

```text
orders.customer_id = 999999
```

should fail if customer `999999` doesn't exist and the foreign key is enforced.

---

# 25. ON DELETE

Foreign keys can define what happens when the parent record is deleted.

Example:

```sql
FOREIGN KEY (customer_id)
REFERENCES customers(id)
ON DELETE CASCADE
```

This means deleting a customer can automatically delete related rows.

### ⚠️ Be careful

`CASCADE` can be dangerous in production.

For business-critical data such as orders, you often **do not want deleting a customer to automatically destroy historical orders**.

Instead, the system may use:

```text
soft delete
status
is_active
```

or restrict deletion.

This is an important production design consideration.

---

# 26. Soft Delete

Instead of:

```sql
DELETE FROM customers
WHERE id = 10;
```

we may use:

```text
deleted_at
```

Example:

```text
customers
--------------------
id
name
email
deleted_at
```

Active:

```text
deleted_at = NULL
```

Deleted:

```text
deleted_at = 2026-09-15 20:00:00
```

The data remains available for auditing/history.

This pattern is common in business applications.

---

# 27. E-commerce Schema Design

Let's design our final simplified e-commerce database.

### Customers

```text
customers
-------------------------
id PK
first_name
last_name
email UNIQUE
phone
created_at
updated_at
```

### Categories

```text
categories
-------------------------
id PK
name
created_at
```

### Products

```text
products
-------------------------
id PK
category_id FK
sku UNIQUE
name
price
stock_quantity
created_at
updated_at
```

### Orders

```text
orders
-------------------------
id PK
customer_id FK
order_number UNIQUE
status
total_amount
created_at
updated_at
```

### Order Items

```text
order_items
-------------------------
id PK
order_id FK
product_id FK
quantity
unit_price
subtotal
```

---

# 28. Relationship Diagram

```text
                    ┌──────────────┐
                    │  categories  │
                    └──────┬───────┘
                           │
                          1:N
                           │
                           ▼
                    ┌──────────────┐
                    │   products   │
                    └──────┬───────┘
                           │
                          1:N
                           │
                           ▼
┌──────────────┐      ┌──────────────┐
│  customers   │ 1:N  │    orders    │
└──────────────┘─────►└──────┬───────┘
                             │
                            1:N
                             │
                             ▼
                      ┌──────────────┐
                      │ order_items  │
                      └──────┬───────┘
                             │
                            N:1
                             │
                             ▼
                         products
```

---

# 29. SQL Schema

Now let's translate the design into SQL.

```sql
CREATE TABLE customers (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(30),
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);
```

Categories:

```sql
CREATE TABLE categories (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL
);
```

Products:

```sql
CREATE TABLE products (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    category_id BIGINT NOT NULL,
    sku VARCHAR(100) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(12,2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,

    FOREIGN KEY (category_id)
        REFERENCES categories(id)
);
```

Orders:

```sql
CREATE TABLE orders (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    customer_id BIGINT NOT NULL,
    order_number VARCHAR(50) NOT NULL UNIQUE,
    status VARCHAR(30) NOT NULL DEFAULT 'pending',
    total_amount DECIMAL(12,2) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,

    FOREIGN KEY (customer_id)
        REFERENCES customers(id)
);
```

Order items:

```sql
CREATE TABLE order_items (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    order_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(12,2) NOT NULL,
    subtotal DECIMAL(12,2) NOT NULL,

    FOREIGN KEY (order_id)
        REFERENCES orders(id),

    FOREIGN KEY (product_id)
        REFERENCES products(id)
);
```

---

# 30. Why DECIMAL Instead of FLOAT?

For money, prefer:

```sql
DECIMAL(12,2)
```

rather than:

```sql
FLOAT
```

Why?

Floating-point numbers can introduce precision issues.

For financial values such as:

```text
₹60,000.00
₹2,999.99
₹149.50
```

we generally want exact decimal representation.

This is particularly important for:

* prices
* taxes
* discounts
* invoices
* payments
* order totals

---

# 31. Database Design vs Application Logic

A common mistake is putting **everything** into the application.

For example:

```python
if price < 0:
    raise ValueError(...)
```

is useful.

But the database can also enforce:

```text
price >= 0
```

where supported.

The strongest systems use both:

```text
Application validation
        +
Database constraints
```

Why?

Application validation improves user experience.

Database constraints protect the data even if another application, script, API, or developer accidentally bypasses the application logic.

---

# 32. Magento Connection

This lesson is particularly relevant to Magento.

When developing a Magento module, you may need to decide:

```text
Should this be a new entity?
Should this be a new table?
What is the primary key?
What relationships exist?
What indexes are required?
What constraints are required?
Should data be normalized?
Should historical data be stored?
```

Magento's schema is considerably more sophisticated, but these fundamental decisions remain.

You should be able to look at a requirement such as:

> "Store customer-specific AI job recommendations."

and think:

```text
What is the entity?
What fields?
What relationship?
What key?
What indexes?
What constraints?
How will it be queried?
```

That's database design thinking.

---

# 33. Practical Real-World Scenario

Imagine JobPilot eventually stores:

```text
Candidate
Job
Application
Skill
Candidate Skill
Job Skill
```

You immediately have:

```text
Candidate 1:N Applications
Candidate N:N Skills
Job N:N Skills
```

So you might design:

```text
candidates
jobs
applications
skills
candidate_skills
job_skills
```

Notice how the same database concepts we're learning apply to your **JobPilot** project too.

---

# 34. Lesson 05 Practical Exercise

Design the following system:

> An e-commerce store wants to support **product reviews**.

Requirements:

* A customer can write multiple reviews.
* A product can have multiple reviews.
* A customer can review a product.
* A review has a rating from 1–5.
* A review has a title and comment.
* A review has a creation date.
* A customer should not be able to create unlimited duplicate reviews for the same product if the business rule is "one review per customer per product."

### Your task

Design:

```text
reviews
```

Identify:

1. Primary key
2. Foreign key to customer
3. Foreign key to product
4. Rating
5. Title
6. Comment
7. Created date
8. Appropriate constraints
9. Appropriate index
10. Whether `(customer_id, product_id)` should have a unique constraint

---

# 🎯 Senior-Level Challenge

Now design the database for this requirement:

> **A customer can have multiple addresses. Each address can be used for multiple orders, but an order must preserve the address that was actually used at the time of purchase.**

Think carefully.

You need to decide whether:

```text
orders
```

should simply reference:

```text
customer_addresses
```

or whether the order needs its own **address snapshot**.

This is a very realistic e-commerce database-design problem.

Try designing:

```text
customers
customer_addresses
orders
```

and explain:

* relationships
* primary keys
* foreign keys
* indexes
* why historical order addresses need special treatment

---

## What comes next

**Lesson 06 — Python + Database**

We'll finally connect the Python you've learned in Parts 1–3 to the databases you've learned here:

```text
Python
   ↓
Database Driver
   ↓
SQL
   ↓
Database
   ↓
Results
   ↓
Python Objects
```

We'll cover:

* MySQL/PostgreSQL drivers
* database connections
* executing SQL from Python
* parameterized queries
* fetching results
* transactions
* commit/rollback
* error handling
* logging
* a practical Python + database application

This is where your **Python + SQL skills start becoming actual backend development skills**.
