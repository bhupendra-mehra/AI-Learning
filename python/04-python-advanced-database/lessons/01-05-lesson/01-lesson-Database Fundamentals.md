# Lesson 01 – Database Fundamentals

We'll start with the foundation rather than jumping directly into SQL.

## 1. What Is a Database?

A database is a system used to **store, organize, retrieve, and manage data**.

For example, an e-commerce application needs to store:

```text
Customers
Products
Orders
Payments
Addresses
Inventory
Categories
```

Instead of keeping everything in Python variables:

```python
customers = [...]
orders = [...]
products = [...]
```

we store persistent data in a database.

---

## 2. Why Not Just Use Files?

You could store data in:

```text
customers.json
orders.json
products.json
```

This works for small applications.

But imagine an e-commerce application with:

```text
10 million customers
50 million orders
1 million products
```

Searching and updating large JSON files becomes inefficient and difficult to manage safely.

A database provides:

* Efficient querying
* Indexing
* Relationships
* Transactions
* Concurrency
* Constraints
* Security
* Data integrity

---

# 3. Relational Databases

A relational database stores data in **tables**.

For example:

### Customers

| id | name      | email                                                 |
| -: | --------- | ----------------------------------------------------- |
|  1 | Bhupendra | [bhupendra@example.com](mailto:bhupendra@example.com) |
|  2 | Rahul     | [rahul@example.com](mailto:rahul@example.com)         |

### Products

|  id | name   | price |
| --: | ------ | ----: |
| 101 | Laptop | 60000 |
| 102 | Mouse  |  1500 |

### Orders

|   id | customer_id | total |
| ---: | ----------: | ----: |
| 1001 |           1 | 61500 |
| 1002 |           2 |  1500 |

The relationships between these tables are what make a relational database powerful.

---

# 4. Rows and Columns

A table contains:

```text
Columns → define the type of information
Rows    → contain actual records
```

For example:

```text
customers
--------------------------------
id | name      | email
--------------------------------
1  | Bhupendra | ...
2  | Rahul     | ...
```

Here:

```text
id
name
email
```

are columns.

Each customer record is a row.

---

# 5. Primary Key

A primary key uniquely identifies a record.

Example:

```text
customers

id | name
---|---------
1  | Bhupendra
2  | Rahul
3  | Amit
```

Here:

```text
id
```

is the primary key.

It should uniquely identify each customer.

Conceptually:

```text
Customer
   |
   └── id → unique identifier
```

---

# 6. Foreign Key

A foreign key creates a relationship between tables.

Example:

```text
customers

id | name
---|---------
1  | Bhupendra
2  | Rahul
```

and:

```text
orders

id   | customer_id | total
-----|-------------|------
1001 | 1           | 61500
1002 | 2           | 1500
```

Here:

```text
orders.customer_id
```

references:

```text
customers.id
```

So:

```text
Customer 1
   ↓
Order 1001
```

---

# 7. One-to-Many Relationship

One customer can have multiple orders.

```text
Customer
   │
   ├── Order 1001
   ├── Order 1002
   └── Order 1003
```

This is:

```text
ONE customer
      ↓
MANY orders
```

The foreign key normally lives on the **many side**:

```text
orders.customer_id
```

---

# 8. Many-to-Many Relationship

Suppose an order contains multiple products:

```text
Order 1001
   │
   ├── Laptop
   ├── Mouse
   └── Keyboard
```

And a product can appear in many orders.

That's a:

```text
Many ↔ Many
```

relationship.

We normally introduce a junction table:

```text
order_items
```

Example:

| order_id | product_id | quantity |
| -------: | ---------: | -------: |
|     1001 |        101 |        1 |
|     1001 |        102 |        2 |
|     1002 |        101 |        1 |

Now:

```text
orders
   ↓
order_items
   ↓
products
```

This database design pattern is extremely important in e-commerce.

---

# 9. Database Normalization

Normalization means organizing data to reduce unnecessary duplication and improve data integrity.

Bad design:

```text
orders

order_id | customer_name | customer_email | product_name
```

If the same customer has 100 orders, their name and email may be repeated 100 times.

Instead:

```text
customers
```

stores customer information.

```text
orders
```

stores order information.

```text
products
```

stores product information.

And relationships connect them.

```text
customers
    ↓
orders
    ↓
order_items
    ↓
products
```

---

# 10. Transactions

A transaction groups multiple database operations into one logical unit.

For example, placing an order might require:

```text
1. Create order
2. Create order items
3. Reduce inventory
4. Record payment
```

What happens if step 3 succeeds but step 4 fails?

We don't want half of the operation saved.

We want:

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

This is where database transactions become important.

---

# 11. ACID

Transactions are commonly discussed using ACID:

| Property    | Meaning                                            |
| ----------- | -------------------------------------------------- |
| Atomicity   | All operations succeed or none do                  |
| Consistency | Data remains valid                                 |
| Isolation   | Concurrent transactions don't improperly interfere |
| Durability  | Committed data persists                            |

For an e-commerce system, this is critical.

---

# 12. Where Your Advanced Python Knowledge Fits

This is why we didn't need another large project in Part 3.

Your previous concepts will now start appearing naturally.

For example:

```text
Dataclasses
     ↓
Database models / data structures

Type hints
     ↓
Database functions / services

Logging
     ↓
Database errors / transactions

Datetime
     ↓
created_at / updated_at

defaultdict / Counter
     ↓
Data aggregation

Context managers
     ↓
Database connections / transactions

Exceptions
     ↓
Database error handling
```

So Part 4 is where we'll **apply**, rather than simply demonstrate, many of the concepts from Part 3.

---

# Practical E-Commerce Database

For our upcoming project, we'll eventually work toward this structure:

```text
Customer
   │
   │ 1:N
   ↓
Order
   │
   │ 1:N
   ↓
Order Item
   │
   │ N:1
   ↓
Product
   │
   ↓
Category
```

And we'll gradually implement:

```text
customers
products
categories
orders
order_items
payments
```

rather than trying to build everything at once.

---

# Lesson 01 Exercise

Before moving to SQL, design the following database on paper/code:

### Customers

```text
id
name
email
phone
created_at
```

### Products

```text
id
name
price
category_id
stock
created_at
```

### Categories

```text
id
name
```

### Orders

```text
id
customer_id
status
total
created_at
```

### Order Items

```text
id
order_id
product_id
quantity
price
```

Then identify:

1. Primary key of every table.
2. Foreign keys.
3. One-to-many relationships.
4. Why `order_items` is required.
5. Why `customer_id` belongs in `orders`.
6. Why `product_id` belongs in `order_items`.

Once you've worked through that, we'll move into **Lesson 02 – SQL Fundamentals**, where you'll start writing actual SQL against this model.
