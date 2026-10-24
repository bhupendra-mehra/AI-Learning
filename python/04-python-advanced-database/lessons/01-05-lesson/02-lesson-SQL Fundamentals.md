# Lesson 02 — SQL Fundamentals

Now we move from **database concepts → actually working with a database**.

For this lesson, we'll use a simple **e-commerce database** so the SQL examples are directly relevant to your Magento/backend experience.

---

## 1. What is SQL?

**SQL (Structured Query Language)** is used to communicate with relational databases.

With SQL, we can:

```text
CREATE   → create database structures
INSERT   → add data
SELECT   → read data
UPDATE   → modify data
DELETE   → remove data
```

And later:

```text
JOIN
GROUP BY
HAVING
SUBQUERY
CTE
WINDOW FUNCTIONS
```

---

# 2. SQL vs Database

Don't confuse these two.

### Database

The database stores the data.

Example:

```text
MySQL
PostgreSQL
MariaDB
```

### SQL

SQL is the language used to work with that database.

For example:

```sql
SELECT * FROM products;
```

This asks the database:

> Give me all products.

---

# 3. Our E-commerce Database

We'll use:

```text
customers
categories
products
orders
order_items
```

Example data:

### customers

| id | name      | email                                                 |
| -: | --------- | ----------------------------------------------------- |
|  1 | Bhupendra | [bhupendra@example.com](mailto:bhupendra@example.com) |
|  2 | Amit      | [amit@example.com](mailto:amit@example.com)           |
|  3 | Rahul     | [rahul@example.com](mailto:rahul@example.com)         |

### categories

| id | name        |
| -: | ----------- |
|  1 | Electronics |
|  2 | Laptops     |
|  3 | Accessories |

### products

|  id | category_id | name           | price |
| --: | ----------: | -------------- | ----: |
| 101 |           2 | Dell Laptop    | 60000 |
| 102 |           3 | Wireless Mouse |  2000 |
| 103 |           3 | Keyboard       |  3000 |
| 104 |           1 | Monitor        | 15000 |

### orders

|   id | customer_id | status     | total_amount |
| ---: | ----------: | ---------- | -----------: |
| 1001 |           1 | complete   |        62000 |
| 1002 |           2 | processing |        18000 |
| 1003 |           1 | pending    |         3000 |

---

# 4. SELECT — Reading Data

The most commonly used SQL command is:

```sql
SELECT * FROM products;
```

`*` means:

> Select all columns.

Result:

```text
101 | 2 | Dell Laptop    | 60000
102 | 3 | Wireless Mouse | 2000
103 | 3 | Keyboard       | 3000
104 | 1 | Monitor        | 15000
```

---

## Select Specific Columns

Instead of:

```sql
SELECT * FROM products;
```

use:

```sql
SELECT name, price
FROM products;
```

Result:

| name           | price |
| -------------- | ----: |
| Dell Laptop    | 60000 |
| Wireless Mouse |  2000 |
| Keyboard       |  3000 |
| Monitor        | 15000 |

### Real-world use

In an API, if you only need:

```text
product name
price
```

there is no reason to retrieve 20 other columns.

This becomes important for **database performance**.

---

# 5. INSERT — Adding Data

Add a new product:

```sql
INSERT INTO products
(category_id, name, price)
VALUES
(3, 'USB Cable', 500);
```

Now the database contains the new product.

---

## Insert Multiple Rows

```sql
INSERT INTO products
(category_id, name, price)
VALUES
(3, 'Webcam', 3500),
(3, 'Headphones', 5000),
(1, 'Tablet', 25000);
```

This is generally better than executing separate statements repeatedly when inserting a batch of data.

---

# 6. UPDATE — Modifying Data

Suppose the laptop price changes:

```sql
UPDATE products
SET price = 65000
WHERE id = 101;
```

Now:

```text
Dell Laptop
₹60,000 → ₹65,000
```

### ⚠️ Very Important

Never casually execute:

```sql
UPDATE products
SET price = 65000;
```

That updates **every product**.

Always think about your `WHERE` condition.

---

# 7. DELETE — Removing Data

```sql
DELETE FROM products
WHERE id = 104;
```

This removes product `104`.

Again, be careful.

This:

```sql
DELETE FROM products;
```

means:

> Delete all rows.

---

# 8. WHERE — Filtering Data

Suppose we want products costing more than ₹10,000:

```sql
SELECT *
FROM products
WHERE price > 10000;
```

Result:

```text
Dell Laptop
Monitor
```

---

## Common Operators

| Operator | Meaning       |
| -------- | ------------- |
| `=`      | equal         |
| `!=`     | not equal     |
| `>`      | greater than  |
| `<`      | less than     |
| `>=`     | greater/equal |
| `<=`     | less/equal    |

Example:

```sql
SELECT *
FROM products
WHERE price >= 5000;
```

---

# 9. Multiple Conditions

Use `AND`:

```sql
SELECT *
FROM products
WHERE price > 2000
AND category_id = 3;
```

Both conditions must be true.

Use `OR`:

```sql
SELECT *
FROM products
WHERE category_id = 2
OR category_id = 3;
```

---

## IN

Instead of:

```sql
WHERE category_id = 2
OR category_id = 3
```

we can write:

```sql
WHERE category_id IN (2, 3);
```

Much cleaner.

---

# 10. DISTINCT

Suppose we want to know which categories contain products:

```sql
SELECT DISTINCT category_id
FROM products;
```

Without `DISTINCT`, you might get:

```text
2
3
3
1
```

With `DISTINCT`:

```text
1
2
3
```

Each value appears once.

---

# 11. ORDER BY

Sort products by price:

```sql
SELECT name, price
FROM products
ORDER BY price;
```

Default is ascending:

```text
2000
3000
15000
60000
```

Descending:

```sql
SELECT name, price
FROM products
ORDER BY price DESC;
```

Result:

```text
60000
15000
3000
2000
```

---

# 12. LIMIT

Suppose we only want the top 2 expensive products:

```sql
SELECT name, price
FROM products
ORDER BY price DESC
LIMIT 2;
```

Result:

| name        | price |
| ----------- | ----: |
| Dell Laptop | 60000 |
| Monitor     | 15000 |

### Real-world use

This is commonly used for:

* product listing
* pagination
* latest orders
* top products
* API responses

---

# 13. Aggregate Functions

SQL can calculate values for us.

Common aggregate functions:

```text
COUNT()
SUM()
AVG()
MIN()
MAX()
```

---

## COUNT

How many products?

```sql
SELECT COUNT(*)
FROM products;
```

Result:

```text
4
```

---

## SUM

Total product prices:

```sql
SELECT SUM(price)
FROM products;
```

---

## AVG

Average product price:

```sql
SELECT AVG(price)
FROM products;
```

---

## MIN

Cheapest product:

```sql
SELECT MIN(price)
FROM products;
```

---

## MAX

Most expensive product:

```sql
SELECT MAX(price)
FROM products;
```

---

# 14. Aliases

Instead of getting:

```text
COUNT(*)
```

we can give it a meaningful name.

```sql
SELECT COUNT(*) AS total_products
FROM products;
```

Result:

```text
total_products
--------------
4
```

Another example:

```sql
SELECT
    AVG(price) AS average_price,
    MAX(price) AS highest_price,
    MIN(price) AS lowest_price
FROM products;
```

---

# 15. GROUP BY

This is extremely important.

Suppose we want:

> How many products does each category have?

We can write:

```sql
SELECT category_id, COUNT(*) AS product_count
FROM products
GROUP BY category_id;
```

Result:

| category_id | product_count |
| ----------: | ------------: |
|           1 |             1 |
|           2 |             1 |
|           3 |             2 |

Think of `GROUP BY` as:

> Put rows into groups and calculate something for each group.

---

# 16. GROUP BY + SUM

Suppose we want total product value by category:

```sql
SELECT
    category_id,
    SUM(price) AS total_price
FROM products
GROUP BY category_id;
```

Result conceptually:

```text
Category 1 → 15000
Category 2 → 60000
Category 3 → 5000
```

---

# 17. HAVING

Here's an important distinction:

### WHERE

Filters individual rows **before grouping**.

### HAVING

Filters groups **after grouping**.

Example:

> Show categories having more than one product.

```sql
SELECT
    category_id,
    COUNT(*) AS product_count
FROM products
GROUP BY category_id
HAVING COUNT(*) > 1;
```

Result:

```text
category_id | product_count
------------|--------------
3           | 2
```

---

# 18. WHERE vs HAVING

Remember this:

```text
WHERE
 ↓
Filter rows
 ↓
GROUP BY
 ↓
Create groups
 ↓
HAVING
 ↓
Filter groups
```

Example:

```sql
SELECT
    category_id,
    COUNT(*) AS product_count
FROM products
WHERE price > 1000
GROUP BY category_id
HAVING COUNT(*) >= 2;
```

Meaning:

1. Ignore products costing ₹1,000 or less.
2. Group remaining products by category.
3. Keep only categories containing at least 2 products.

---

# 19. Real-World E-commerce Queries

Now let's make these practical.

### Find pending orders

```sql
SELECT *
FROM orders
WHERE status = 'pending';
```

### Find completed orders

```sql
SELECT *
FROM orders
WHERE status = 'complete';
```

### Find orders above ₹50,000

```sql
SELECT *
FROM orders
WHERE total_amount > 50000;
```

### Find the latest 10 orders

```sql
SELECT *
FROM orders
ORDER BY id DESC
LIMIT 10;
```

### Count orders by status

```sql
SELECT
    status,
    COUNT(*) AS order_count
FROM orders
GROUP BY status;
```

Possible result:

| status     | order_count |
| ---------- | ----------: |
| complete   |           1 |
| processing |           1 |
| pending    |           1 |

---

# 20. SQL Execution Order

This is worth understanding early.

When you write:

```sql
SELECT category_id, COUNT(*)
FROM products
WHERE price > 1000
GROUP BY category_id
HAVING COUNT(*) > 1
ORDER BY category_id
LIMIT 10;
```

Conceptually SQL processes it approximately as:

```text
FROM
 ↓
WHERE
 ↓
GROUP BY
 ↓
HAVING
 ↓
SELECT
 ↓
ORDER BY
 ↓
LIMIT
```

This becomes extremely useful when we reach **advanced SQL and query optimization**.

---

# 21. Magento Connection

You will see queries conceptually similar to:

```sql
SELECT *
FROM sales_order
WHERE customer_id = 10;
```

or:

```sql
SELECT
    status,
    COUNT(*)
FROM sales_order
GROUP BY status;
```

In Magento, however, you should generally use Magento's resource models/collections or service contracts appropriately rather than directly querying tables everywhere.

Understanding SQL underneath those abstractions is still essential for:

* debugging
* performance optimization
* reports
* database investigation
* identifying slow queries
* understanding Magento collections
* writing custom modules
* API/data integrations

---

# 22. Practical Exercise

Use the following data:

### products

```text
101 | Electronics | Laptop    | 60000
102 | Accessories | Mouse     | 2000
103 | Accessories | Keyboard  | 3000
104 | Electronics | Monitor   | 15000
105 | Accessories | Webcam    | 5000
```

Write SQL for each requirement.

### Q1

Get all products.

```sql
SELECT ...
```

### Q2

Get only:

```text
name
price
```

### Q3

Find products costing more than ₹5,000.

### Q4

Find products belonging to category `Accessories`.

### Q5

Find products costing between ₹2,000 and ₹10,000.

### Q6

Sort products from highest price to lowest.

### Q7

Return only the 3 most expensive products.

### Q8

Find the cheapest product.

### Q9

Find the most expensive product.

### Q10

Find the average product price.

### Q11

Count total products.

### Q12

Count products by category.

Expected concept:

```text
category
   ↓
COUNT(products)
```

### Q13

Find categories containing more than 1 product.

You must use:

```sql
GROUP BY
HAVING
```

### Q14 — Real-world scenario

An e-commerce manager asks:

> "Give me the number of products costing more than ₹3,000 in each category, but only show categories having at least 2 such products."

Try to solve this using:

```text
WHERE
GROUP BY
HAVING
COUNT()
```

---

## 🎯 Lesson 02 Practical Challenge

Finally, write a query for:

> **Find the top 3 most expensive products in the Accessories category.**

Your query should use:

```text
WHERE
ORDER BY
LIMIT
```

Send me your **Q1–Q14 answers + practical challenge**. I'll review them, correct anything that needs improvement, and then we'll proceed to **Lesson 03 — SQL Joins**, where we'll start combining `customers`, `orders`, `order_items`, `products`, and `categories`—the part that becomes especially useful for Magento database work.
