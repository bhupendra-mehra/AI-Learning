# Lesson 08 — Database Performance

Practical lesson

Python + Flask + SQLAlchemy + MySQL

Project: `advanced-python-database/ecommerce-db`

In this lesson, we'll improve the performance of your existing e-commerce application. We'll work with the `Product`, `Category`, `Customer`, `Order`, and `OrderItem` models, using practical examples that fit your Flask + SQLAlchemy project.&#x20;

By the end, you'll know how to identify slow queries, reduce unnecessary database calls, paginate large results, configure connection pooling, and understand caching.

## What we'll complete

### 01

Indexing

Speed up filtering and sorting

### 02

Query optimization + EXPLAIN

Understand how MySQL executes queries

### 03

N+1 queries

Load related records efficiently

### 04

Pagination

Fetch a limited number of products at a time

### 05

Connection pooling

Reuse database connections efficiently

### 06

Caching fundamentals

Avoid repeating expensive reads

### 07

Final performance checks

Run tests and review the results

## Step 0 — Open the project safely

Do this work in your local WSL environment, not directly on your GCP VM. Keep the running application and MySQL data untouched.

```
cd /var/www/html/advanced-python-database/ecommerce-db
```

Activate your existing virtual environment using the activation path you normally use. Then check:

```
python --version
python -m pytest -v
ruff check .
```

If the tests fail before you start, note the existing failures first rather than assuming they were caused by this lesson.

## 1. Indexing — make database lookups faster

### What is an index?

An index helps MySQL find matching rows without scanning the entire table in many cases. It is useful for columns frequently used in `WHERE`, `JOIN`, `ORDER BY`, or lookup conditions.

For our e-commerce project, possible candidates include:

- `products.category_id` — filtering products by category.
- `products.name` — searching products by name, depending on the search pattern.
- `orders.customer_id` — retrieving a customer's orders.
- `order_items.order_id` — retrieving items belonging to an order.

These are candidates, not instructions to create every index. Check existing primary keys, foreign keys, and indexes first.

### Step 1.1 — Inspect existing indexes

Connect to the MySQL database using your normal local development configuration, then run:

```
SHOW INDEX FROM products;
SHOW INDEX FROM categories;
SHOW INDEX FROM orders;
SHOW INDEX FROM order_items;
```

Look at the `Column_name` and `Key_name` columns. `PRIMARY` identifies the primary-key index.

Important: A foreign-key constraint and its required index are related, but don't assume every useful query has an appropriate index just because a foreign key exists. Inspect the actual schema.

### Step 1.2 — Test a query before adding an index

For example, retrieving products in a particular category:

```
SELECT id, name, price
FROM products
WHERE category_id = 2
ORDER BY name
LIMIT 20;
```

Use `EXPLAIN` to inspect how MySQL plans to execute it:

```
EXPLAIN
SELECT id, name, price
FROM products
WHERE category_id = 2
ORDER BY name
LIMIT 20;
```

Important fields include:

- `type`: the access method MySQL expects to use.
- `possible_keys`: indexes it considers applicable.
- `key`: the index it chooses, if any.
- `rows`: its estimate of rows examined.
- `Extra`: additional details, potentially including sorting or temporary work.

A table scan is not automatically bad for a small table. The goal is to improve a real bottleneck, not to eliminate every scan.

### Step 1.3 — Add a targeted index

If `category_id` is frequently used to filter products and no suitable index exists, you could add:

```
CREATE INDEX idx_products_category_id
ON products (category_id);
```

For a query that filters by category and then sorts by name, a composite index might be worth testing:

```
CREATE INDEX idx_products_category_name
ON products (category_id, name);
```

Don't create both automatically. Test the actual query plan and compare results.

A composite index on `(category_id, name)` can support queries using the leftmost column `category_id`, and queries using both columns in the appropriate order. It generally does not replace an index designed for searching by `name` alone.

### Step 1.4 — Represent indexes in SQLAlchemy

In your `Product` model, an index can be declared using SQLAlchemy:

```
from sqlalchemy import Indexclass Product(Base):    __tablename__ = "products"    # Keep your existing mapped columns and relationships here.    __table_args__ = (        Index("idx_products_category_name", "category_id", "name"),    )
```

Do not paste this declaration blindly into your model. Keep your existing columns, relationships, and `__table_args__`; merge the index into the existing model definition.

Adding an index to a model does not automatically guarantee that an already-existing production database has been migrated. Use a migration or a controlled schema change, and verify whether the index already exists.

### When indexes help — and when they hurt

| Index benefit              | Trade-off                                |
| -------------------------- | ---------------------------------------- |
| Faster selective lookups   | Additional disk space                    |
| Can help joins and sorting | Slower inserts and updates in some cases |
| Can reduce rows examined   | More indexes to maintain                 |

Checkpoint: You can inspect indexes, run `EXPLAIN`, and explain why an index should be added rather than adding one to every column.

## 2. Query optimization and `EXPLAIN`

Query optimization starts by measuring what a query does and how much data it processes.

### Step 2.1 — Avoid fetching unnecessary columns

Less efficient when only three fields are needed:

```
products = session.query(Product).all()
```

This loads full ORM objects for every matching product, including columns the current operation may not need.

A more targeted query:

```
from sqlalchemy import selectstmt = select(    Product.id,    Product.name,    Product.price,).where(Product.category_id == category_id)rows = session.execute(stmt).all()
```

Use the full model when you need to work with its relationships or update it. Use a column projection for read-only operations that need only a few fields.

### Step 2.2 — Filter in the database

Avoid loading all products and filtering them in Python:

```
# Inefficient for a large tableproducts = session.query(Product).all()cheap_products = [p for p in products if p.price < 1000]
```

Instead, let MySQL perform the filtering:

```
stmt = select(Product).where(Product.price < 1000)products = session.scalars(stmt).all()
```

The second approach lets the database filter rows before returning results to Python.

### Step 2.3 — Use `EXPLAIN` for a real query

Suppose the storefront fetches products by category:

```
EXPLAIN
SELECT id, name, price
FROM products
WHERE category_id = 2
ORDER BY name
LIMIT 20;
```

Run the query before and after a candidate index, preferably on a representative development dataset.

For deeper analysis, MySQL supports `EXPLAIN ANALYZE` in supported versions. It actually executes the query and reports measured execution details, so use it carefully on expensive queries or production data.

### Step 2.4 — Avoid common query mistakes

- Don't run a query repeatedly inside a loop if one query can fetch the needed data.
- Don't fetch every row when only a few columns are required.
- Don't add indexes without examining query patterns.
- Don't assume a query is fast because the development database contains only a few records.
- Don't use `COUNT(*)` on every page request unless the total count is needed.

Checkpoint: You should be able to compare the query's purpose, its execution plan, and the amount of data returned.

## 3. N+1 queries — the common ORM performance problem

Imagine the storefront loads 20 products. Each product then accesses its category.

A naive implementation may run:

1. One query to fetch the products.
2. Up to 20 additional queries to fetch their categories.

That's the N+1 query problem.

### Step 3.1 — Recognize the pattern

```
products = session.scalars(    select(Product).limit(20)).all()for product in products:    print(product.name, product.category.name)
```

If `category` is lazily loaded and not already present in the session, accessing it can issue additional SQL queries.

The exact number depends on relationships and session state; it is not necessarily always 21.

### Step 3.2 — Use `joinedload` for a many-to-one relationship

For a product's single category:

```
from sqlalchemy import selectfrom sqlalchemy.orm import joinedloadstmt = (    select(Product)    .options(joinedload(Product.category))    .limit(20))products = session.scalars(stmt).all()for product in products:    print(product.name, product.category.name)
```

`joinedload()` fetches the related category using a join, avoiding separate lazy-load queries for each product's category.

Use the actual relationship name declared in your model. Here, `Product.category` is an example.

### Step 3.3 — Use `selectinload` for collections

Suppose you load customers and need their orders:

```
from sqlalchemy.orm import selectinloadstmt = (    select(Customer)    .options(selectinload(Customer.orders))    .limit(20))customers = session.scalars(stmt).all()for customer in customers:    print(customer.id, len(customer.orders))
```

`selectinload()` generally fetches the parent records first, then retrieves related records in one or more additional queries using an `IN` condition. This often works well for one-to-many collections.

Again, `Customer.orders` must match your model's actual relationship name.

### Step 3.4 — Choose the right loading strategy

| Situation                                 | Typical choice                  |
| ----------------------------------------- | ------------------------------- |
| Product → one category                    | `joinedload()`                  |
| Customer → many orders                    | `selectinload()`                |
| Need no relationship data                 | Don't load it                   |
| Large collection with only a count needed | Consider a database count query |

### How to verify the improvement

Enable SQL logging in a local development environment or use SQLAlchemy's query logging. Compare how many SQL statements run for the same operation before and after the change.

Don't enable verbose SQL logging in production indefinitely; it can generate a lot of output and may expose query parameters.

Checkpoint: You can identify a loop that triggers relationship queries and choose an appropriate eager-loading strategy.

## 4. Pagination — load products in manageable batches

If a store has 10,000 products, loading all of them on one page wastes memory and increases response time.

Pagination limits how many records a request retrieves.

### Step 4.1 — Understand `LIMIT` and `OFFSET`

```
SELECT id, name, price
FROM products
ORDER BY id
LIMIT 20 OFFSET 0;
```

This returns the first 20 products.

The next page:

```
SELECT id, name, price
FROM products
ORDER BY id
LIMIT 20 OFFSET 20;
```

The third page uses `OFFSET 40`, and so on.

Always use a deterministic `ORDER BY` when paginating. Without it, page boundaries may be unpredictable.

### Step 4.2 — Add pagination to a Flask route

Here is a simple SQLAlchemy 2.x example:

```
from flask import request, render_templatefrom sqlalchemy import select@app.get("/products")def product_list():    page = request.args.get("page", 1, type=int)    per_page = 20    page = max(page, 1)    stmt = (        select(Product)        .order_by(Product.id)        .limit(per_page)        .offset((page - 1) * per_page)    )    products = db.session.scalars(stmt).all()    return render_template(        "products.html",        products=products,        page=page,        per_page=per_page,    )
```

This is a teaching example. Adapt it to your project's existing Flask blueprint, database session, route names, and template structure rather than replacing an existing route wholesale.

### Step 4.3 — Add navigation links

In a template, a minimal navigation example is:

```
{% if page > 1 %}
  <a href="?page={{ page - 1 }}">Previous</a>
{% endif %}

<a href="?page={{ page + 1 }}">Next</a>
```

This is simplified navigation; it doesn't yet know whether a next page exists. A production template should handle the final page and preserve any active filters or sorting options.

### Step 4.4 — Know when to use keyset pagination

Large offsets can become expensive because MySQL may still need to walk past many rows before returning the requested page.

For deep pagination, keyset pagination can be more efficient. If `id` is an increasing unique key:

```
SELECT id, name, price
FROM products
WHERE id > 500
ORDER BY id
LIMIT 20;
```

The next request uses the last ID from the previous page instead of a large offset. In a real implementation, use the actual last-seen ID rather than hardcoding `500`.

Checkpoint: Your queries can return a limited page of products instead of loading the full catalog.

## 5. Connection pooling — reuse database connections

Opening a new database connection for every query is expensive. SQLAlchemy's engine uses a connection pool to reuse connections when possible.

### Step 5.1 — Understand the flow

Flask request

SQLAlchemy `Session`

SQLAlchemy connection pool

MySQL

A session manages a unit of ORM work. The pool manages reusable database connections. They are related but not the same thing.

### Step 5.2 — Configure the SQLAlchemy engine

If your project creates an engine directly, a configuration might look like:

```
from sqlalchemy import create_engineengine = create_engine(    DATABASE_URL,    pool_size=5,    max_overflow=2,    pool_timeout=30,    pool_recycle=1800,    pool_pre_ping=True,)
```

Meaning:

- `pool_size=5`: keep up to five pooled connections.
- `max_overflow=2`: allow up to two temporary connections above that pool size.
- `pool_timeout=30`: wait up to 30 seconds for a connection before raising an error.
- `pool_recycle=1800`: recycle old connections after the configured age.
- `pool_pre_ping=True`: check whether a connection is alive before using it.

Don't create a second engine blindly. If your Flask application already initializes SQLAlchemy, configure the existing engine using the pattern appropriate to that setup. For example, Flask-SQLAlchemy supports engine options through its application configuration before `db.init_app(app)`.

### Step 5.3 — Keep the pool appropriate for your VM

Your GCP VM has limited memory and runs both the application and MySQL. A large pool can consume database connections unnecessarily.

Also remember that pool limits are generally per application process. If Gunicorn runs several workers, the potential total number of connections can be higher than the pool size configured for one worker.

Start small, measure usage, and ensure the MySQL connection limit can accommodate all workers and other clients.

### Common issues

- Too many connections: reduce per-process pool usage or worker count, then review connection leaks.
- Stale connections: consider `pool_pre_ping` and an appropriate recycle interval.
- Connection pool timeout: investigate long-running queries and sessions that aren't being released.

Checkpoint: You understand what the pool does and why increasing pool size is not always an improvement.

## 6. Caching fundamentals — avoid repeating expensive reads

Caching stores the result of a computation or query so that a later request can reuse it.

For example, category names may be requested frequently but change relatively rarely.

### Step 6.1 — Understand cache flow

Request for categories

Check cache

Cache hit

Return cached data

Cache miss

Query MySQL, store result

### Step 6.2 — A simple in-process cache example

Python's `functools.lru_cache` is useful for demonstrating caching:

```
from functools import lru_cache@lru_cache(maxsize=128)def format_category_label(category_id: int) -> str:    # Demonstration only: this function must be deterministic.    return f"Category {category_id}"
```

This caches a function's return value for repeated calls with the same argument.

However, this is not a suitable general-purpose database cache. It doesn't automatically expire entries when the database changes, and each application process has its own separate cache.

### Step 6.3 — Cache actual database data carefully

For data such as category lists, a real cache design needs:

1. A cache key, such as `categories:all`.
2. A TTL (time to live), such as 60 seconds.
3. A plan to invalidate or refresh the cached value after a category is created, edited, or deleted.
4. A suitable shared cache backend if multiple workers need to share the same values.

For a multi-process deployment, an external cache such as Redis is a common option, but it adds infrastructure and resource usage. For your small VM, first optimize SQL and measure the benefit before adding another service.

### What should you cache?

| Data                  | Possible strategy                                        |
| --------------------- | -------------------------------------------------------- |
| Category list         | Short TTL; invalidate after category changes             |
| Product details       | Short TTL; invalidate on product updates                 |
| Cart contents         | Be careful: user-specific and changes frequently         |
| Customer account data | Avoid careless shared caching; protect private data      |
| Order/payment data    | Prioritize correctness; don't serve stale critical state |

Checkpoint: You understand cache hits, cache misses, TTL, invalidation, and why stale or user-mixed data can cause bugs.

## 7. Final practical exercise — optimize the product listing

Now combine the lesson topics into one task for your e-commerce application.

### Your task

Implement a performance improvement for product listing, using your existing project structure.

## Lesson 08 checklist

7 of 7

Inspect existing indexes

Check products, categories and related tables before creating new indexes.

Analyze a product query

Run EXPLAIN on a category filter and sorting query.

Optimize relationships

Use joinedload or selectinload where your actual models need related data.

Add pagination

Ensure a product-list request returns a limited number of products.

Review connection pooling

Find the existing SQLAlchemy engine configuration before changing it.

Decide whether caching is useful

Identify one repeated read and define its TTL and invalidation strategy.

Run checks

Run pytest and Ruff after your changes.

### Final validation commands

From your local application directory:

```
python -m pytest -v
ruff check .
```

If you add database indexes or change query code, also verify the actual SQL and execution plan. Tests passing alone don't prove that a query is faster.

### Interview questions and answers

1\. Why do we use database indexes?

Indexes help the database locate rows more efficiently, but they consume space and add overhead to writes.

2\. What is `EXPLAIN`?

It shows the database's planned execution strategy, including possible indexes, the chosen access method, and estimated rows examined.

3\. What is the N+1 query problem?

It happens when an initial query fetches multiple records and additional queries are triggered for related data, often one per record. Eager loading can reduce those queries.

4\. What is the difference between `joinedload()` and `selectinload()`?

`joinedload()` commonly fetches related data through a join. `selectinload()` fetches parent records and then loads related records using one or more additional queries.

5\. Why is pagination important?

It limits the number of rows returned and the amount of data processed for one request.

6\. What is connection pooling?

It reuses database connections instead of repeatedly establishing new ones.

7\. What are cache invalidation and TTL?

TTL determines how long a cache entry remains valid. Invalidation removes or refreshes cached data when the underlying information changes.

## Lesson 08 — Completion criteria

You've completed this lesson when you can inspect existing indexes, analyze a query with `EXPLAIN`, avoid N+1 queries, paginate product listings, explain connection-pool settings, and design a basic cache strategy.

Keep the changes practical: measure first, make one improvement at a time, and verify afterward. Avoid making speculative changes directly on your GCP VM.

Once Lesson 08 is complete, we'll cover Lesson 09 — Data Processing with Python in one complete practical lesson, using your e-commerce database to read data, transform records, aggregate results, clean data, work with CSV/JSON and pandas, and build a small ETL workflow.
