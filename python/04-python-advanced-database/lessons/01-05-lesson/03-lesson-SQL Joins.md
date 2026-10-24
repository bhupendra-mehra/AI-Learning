# Lesson 03 — SQL Joins

This is one of the **most important SQL lessons** for your Magento/backend background.

In the previous lesson, we queried one table at a time.

In real applications, information is distributed across multiple tables:

```text
customers
    ↓
orders
    ↓
order_items
    ↓
products
    ↓
categories
```

A **JOIN** allows us to combine related data from these tables.

---

# 1. Why Do We Need JOINs?

Suppose we have:

### customers

| id | name      | email                                                 |
| -: | --------- | ----------------------------------------------------- |
|  1 | Bhupendra | [bhupendra@example.com](mailto:bhupendra@example.com) |
|  2 | Amit      | [amit@example.com](mailto:amit@example.com)           |
|  3 | Rahul     | [rahul@example.com](mailto:rahul@example.com)         |

### orders

|   id | customer_id | status     | total_amount |
| ---: | ----------: | ---------- | -----------: |
| 1001 |           1 | complete   |        62000 |
| 1002 |           2 | processing |        18000 |
| 1003 |           1 | pending    |         3000 |

The `orders` table doesn't contain the customer's name.

It only contains:

```text
customer_id
```

We can connect:

```text
orders.customer_id
        ↓
customers.id
```

using a JOIN.

---

# 2. INNER JOIN

The most commonly used JOIN is:

```sql
SELECT
    customers.name,
    orders.id,
    orders.total_amount
FROM customers
INNER JOIN orders
    ON customers.id = orders.customer_id;
```

Result:

| name      | order id | total |
| --------- | -------: | ----: |
| Bhupendra |     1001 | 62000 |
| Amit      |     1002 | 18000 |
| Bhupendra |     1003 |  3000 |

### Meaning

`INNER JOIN` returns only records that have a match in **both tables**.

Think:

```text
Customers ∩ Orders
```

---

# 3. JOIN Condition

This is the most important part:

```sql
ON customers.id = orders.customer_id
```

We're telling SQL:

> Match the customer's primary key with the order's foreign key.

Database relationship:

```text
customers.id
     ↑
     │
orders.customer_id
```

---

# 4. INNER JOIN Real-World Example

Find all orders along with customer information:

```sql
SELECT
    orders.id AS order_id,
    customers.name AS customer_name,
    customers.email,
    orders.status,
    orders.total_amount
FROM orders
INNER JOIN customers
    ON orders.customer_id = customers.id;
```

This is the kind of query you might use for:

* order reports
* admin dashboards
* customer order history
* exports
* analytics

---

# 5. Table Aliases

Long table names can make queries difficult to read.

Instead:

```sql
SELECT
    o.id,
    c.name,
    o.total_amount
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.id;
```

You can also omit `AS`:

```sql
FROM orders o
INNER JOIN customers c
```

I recommend becoming comfortable with aliases because you'll use them constantly in real projects.

---

# 6. LEFT JOIN

Now suppose we have:

```text
customers
```

with:

| id | name      |
| -: | --------- |
|  1 | Bhupendra |
|  2 | Amit      |
|  3 | Rahul     |
|  4 | Neha      |

But Rahul and Neha have never placed an order.

If we use:

```sql
INNER JOIN
```

Rahul and Neha disappear.

But what if the requirement is:

> Show **all customers**, including customers who have never ordered.

Use:

```sql
SELECT
    c.name,
    o.id AS order_id,
    o.total_amount
FROM customers c
LEFT JOIN orders o
    ON c.id = o.customer_id;
```

Result:

| name      | order_id | total |
| --------- | -------: | ----: |
| Bhupendra |     1001 | 62000 |
| Amit      |     1002 | 18000 |
| Bhupendra |     1003 |  3000 |
| Rahul     |     NULL |  NULL |
| Neha      |     NULL |  NULL |

---

# 7. INNER JOIN vs LEFT JOIN

Remember this visually:

### INNER JOIN

```text
Customers       Orders

   █████████████
       MATCH
```

Only matching records.

### LEFT JOIN

```text
Customers              Orders

████████████████
       │
       └──── matching orders
       
Customers without orders
are still included
```

The **left table is always preserved**.

---

# 8. Find Customers Without Orders

This is a very useful real-world query.

```sql
SELECT
    c.id,
    c.name
FROM customers c
LEFT JOIN orders o
    ON c.id = o.customer_id
WHERE o.id IS NULL;
```

Meaning:

> Give me customers for whom no matching order exists.

This is useful for:

* inactive customer analysis
* marketing campaigns
* abandoned customer segmentation
* CRM reports

---

# 9. RIGHT JOIN

`RIGHT JOIN` is essentially the reverse perspective of `LEFT JOIN`.

```sql
SELECT
    c.name,
    o.id AS order_id
FROM customers c
RIGHT JOIN orders o
    ON c.id = o.customer_id;
```

It preserves all records from the **right-side table**.

In practice, many developers prefer rewriting the query using `LEFT JOIN` because it is often easier to read.

For example:

```sql
FROM orders o
LEFT JOIN customers c
    ON o.customer_id = c.id
```

---

# 10. FULL OUTER JOIN

A `FULL OUTER JOIN` returns:

* matching records
* unmatched records from the left
* unmatched records from the right

Conceptually:

```text
LEFT only
   +
MATCHING
   +
RIGHT only
```

Example:

```sql
SELECT
    c.name,
    o.id
FROM customers c
FULL OUTER JOIN orders o
    ON c.id = o.customer_id;
```

### Important

Database support differs.

For example, PostgreSQL supports `FULL OUTER JOIN`, while MySQL does not provide it directly.

We'll focus primarily on JOINs you'll commonly encounter in Magento/MySQL environments.

---

# 11. Joining Three Tables

Now things become more interesting.

We have:

```text
customers
      ↓
orders
      ↓
order_items
```

Suppose:

### order_items

| id | order_id | product_id | quantity | unit_price |
| -: | -------: | ---------: | -------: | ---------: |
|  1 |     1001 |        101 |        1 |      60000 |
|  2 |     1001 |        102 |        1 |       2000 |
|  3 |     1002 |        104 |        1 |      15000 |

We can query:

> Which customer purchased which products?

```sql
SELECT
    c.name AS customer_name,
    o.id AS order_id,
    oi.product_id,
    oi.quantity,
    oi.unit_price
FROM customers c
INNER JOIN orders o
    ON c.id = o.customer_id
INNER JOIN order_items oi
    ON o.id = oi.order_id;
```

Now we're joining **three tables**.

---

# 12. Joining Four Tables

Add `products`.

```sql
SELECT
    c.name AS customer_name,
    o.id AS order_id,
    p.name AS product_name,
    oi.quantity,
    oi.unit_price
FROM customers c

INNER JOIN orders o
    ON c.id = o.customer_id

INNER JOIN order_items oi
    ON o.id = oi.order_id

INNER JOIN products p
    ON oi.product_id = p.id;
```

Result could look like:

| customer  | order | product        | quantity | price |
| --------- | ----: | -------------- | -------: | ----: |
| Bhupendra |  1001 | Dell Laptop    |        1 | 60000 |
| Bhupendra |  1001 | Wireless Mouse |        1 |  2000 |
| Amit      |  1002 | Monitor        |        1 | 15000 |

This is a **real e-commerce query**.

---

# 13. Joining Five Tables

Now include categories.

```sql
SELECT
    c.name AS customer_name,
    o.id AS order_id,
    p.name AS product_name,
    cat.name AS category_name,
    oi.quantity,
    oi.unit_price
FROM customers c

INNER JOIN orders o
    ON c.id = o.customer_id

INNER JOIN order_items oi
    ON o.id = oi.order_id

INNER JOIN products p
    ON oi.product_id = p.id

INNER JOIN categories cat
    ON p.category_id = cat.id;
```

We have now traversed:

```text
Customer
   ↓
Order
   ↓
Order Item
   ↓
Product
   ↓
Category
```

This is exactly why understanding database relationships from **Lesson 01** was important.

---

# 14. JOIN + WHERE

We can filter joined data.

Example:

> Show orders placed by Bhupendra.

```sql
SELECT
    o.id,
    c.name,
    o.total_amount
FROM orders o
INNER JOIN customers c
    ON o.customer_id = c.id
WHERE c.name = 'Bhupendra';
```

---

# 15. JOIN + ORDER BY

Find the largest orders:

```sql
SELECT
    o.id AS order_id,
    c.name AS customer_name,
    o.total_amount
FROM orders o
INNER JOIN customers c
    ON o.customer_id = c.id
ORDER BY o.total_amount DESC;
```

---

# 16. JOIN + GROUP BY

Now let's calculate:

> How many orders has each customer placed?

```sql
SELECT
    c.id,
    c.name,
    COUNT(o.id) AS order_count
FROM customers c
LEFT JOIN orders o
    ON c.id = o.customer_id
GROUP BY c.id, c.name;
```

Possible result:

| id | name      | order_count |
| -: | --------- | ----------: |
|  1 | Bhupendra |           2 |
|  2 | Amit      |           1 |
|  3 | Rahul     |           0 |
|  4 | Neha      |           0 |

Notice why we used `LEFT JOIN`.

We want customers with **zero orders** too.

---

# 17. JOIN + SUM

Suppose the requirement is:

> Calculate total order value for every customer.

```sql
SELECT
    c.id,
    c.name,
    COALESCE(SUM(o.total_amount), 0) AS total_spent
FROM customers c
LEFT JOIN orders o
    ON c.id = o.customer_id
GROUP BY c.id, c.name;
```

`COALESCE()` converts `NULL` into `0`.

So a customer with no orders gets:

```text
total_spent = 0
```

---

# 18. JOIN + HAVING

Now:

> Find customers who have spent more than ₹50,000.

```sql
SELECT
    c.id,
    c.name,
    SUM(o.total_amount) AS total_spent
FROM customers c
INNER JOIN orders o
    ON c.id = o.customer_id
GROUP BY c.id, c.name
HAVING SUM(o.total_amount) > 50000;
```

Notice:

```text
WHERE
```

cannot be used for:

```sql
SUM(o.total_amount)
```

because `SUM()` happens during grouping.

That's why we use:

```text
HAVING
```

---

# 19. Self JOIN

A **self join** joins a table to itself.

Example:

```text
employees
-----------------------
id
name
manager_id
```

Data:

| id | name  | manager_id |
| -: | ----- | ---------: |
|  1 | John  |       NULL |
|  2 | Amit  |          1 |
|  3 | Rahul |          1 |

We want:

```text
Employee | Manager
```

Query:

```sql
SELECT
    e.name AS employee,
    m.name AS manager
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.id;
```

Result:

| employee | manager |
| -------- | ------- |
| John     | NULL    |
| Amit     | John    |
| Rahul    | John    |

The same table is referenced twice using aliases.

---

# 20. JOIN Performance — Important for Magento

A JOIN can become expensive when tables contain millions of rows.

For example:

```text
sales_order
sales_order_item
customer_entity
catalog_product_entity
```

Magento databases can contain a very large number of records.

Indexes become extremely important.

For example:

```text
orders.customer_id
order_items.order_id
order_items.product_id
products.category_id
```

should generally have appropriate indexes/constraints according to the schema and query patterns.

We'll study **indexing and query performance in Lesson 08**.

---

# 21. A Common JOIN Mistake

Suppose:

```sql
SELECT *
FROM customers c
JOIN orders o;
```

There is no proper relationship condition.

This can create a **Cartesian product / cross join-like result**, where every customer can be combined with every order.

For example:

```text
3 customers × 1000 orders
= 3000 rows
```

This can become disastrous with large tables.

Always carefully define:

```sql
ON c.id = o.customer_id
```

---

# 22. JOIN Mental Model

When writing a JOIN, ask three questions:

### 1. What information do I need?

Example:

```text
Customer name
Order number
Product name
```

### 2. Which tables contain that information?

```text
customers → customer name
orders → order number
products → product name
```

### 3. How are those tables connected?

```text
customers.id
      ↓
orders.customer_id

orders.id
      ↓
order_items.order_id

order_items.product_id
      ↓
products.id
```

Then construct the JOIN.

---

# 23. Real-World Magento Use Case

Imagine support receives:

> "Customer Bhupendra says he purchased a Dell Laptop but cannot find the order."

A simplified investigation might be:

```sql
SELECT
    c.email,
    o.id AS order_id,
    o.status,
    p.name AS product_name,
    oi.quantity
FROM customers c
JOIN orders o
    ON c.id = o.customer_id
JOIN order_items oi
    ON o.id = oi.order_id
JOIN products p
    ON oi.product_id = p.id
WHERE c.email = 'bhupendra@example.com'
AND p.name = 'Dell Laptop';
```

This gives you a complete path:

```text
Customer
   ↓
Order
   ↓
Order Item
   ↓
Product
```

That is the kind of database thinking you should develop as a senior Magento engineer.

---

# 24. JOIN Cheat Sheet

| JOIN              | Returns                             |
| ----------------- | ----------------------------------- |
| `INNER JOIN`      | Matching rows from both tables      |
| `LEFT JOIN`       | All left rows + matching right rows |
| `RIGHT JOIN`      | All right rows + matching left rows |
| `FULL OUTER JOIN` | All rows from both sides            |
| `SELF JOIN`       | Table joined with itself            |

For your Magento/MySQL work, focus especially on:

```text
INNER JOIN
LEFT JOIN
SELF JOIN
```

---

# 25. Practical Exercise

Use these tables.

### customers

| id | name      |
| -: | --------- |
|  1 | Bhupendra |
|  2 | Amit      |
|  3 | Rahul     |
|  4 | Neha      |

### orders

|   id | customer_id | status     | total_amount |
| ---: | ----------: | ---------- | -----------: |
| 1001 |           1 | complete   |        62000 |
| 1002 |           2 | processing |        18000 |
| 1003 |           1 | pending    |         3000 |

### products

|  id | category_id | name     | price |
| --: | ----------: | -------- | ----: |
| 101 |           2 | Laptop   | 60000 |
| 102 |           3 | Mouse    |  2000 |
| 103 |           3 | Keyboard |  3000 |
| 104 |           1 | Monitor  | 15000 |

### order_items

| id | order_id | product_id | quantity | unit_price |
| -: | -------: | ---------: | -------: | ---------: |
|  1 |     1001 |        101 |        1 |      60000 |
|  2 |     1001 |        102 |        1 |       2000 |
|  3 |     1002 |        104 |        1 |      15000 |
|  4 |     1003 |        103 |        1 |       3000 |

---

## Questions

### Q1

Display:

```text
customer name
order id
order status
```

Use `INNER JOIN`.

### Q2

Display **all customers**, including customers who have never placed an order.

Use `LEFT JOIN`.

### Q3

Find customers who have never placed an order.

### Q4

Display:

```text
customer name
order id
product name
quantity
```

Use three JOINs after `customers`.

### Q5

Display:

```text
customer
product
category
quantity
price
```

Join all relevant tables.

### Q6

Find the total number of orders for each customer.

Include customers with zero orders.

### Q7

Find total amount spent by each customer.

### Q8

Find customers whose total spending is greater than ₹50,000.

Use:

```text
GROUP BY
HAVING
```

### Q9

Find all orders containing the product `Laptop`.

### Q10 — Senior-level scenario

A business analyst asks:

> **"Show the top 3 customers by total spending, along with their email addresses."**

Write the SQL query using:

```text
JOIN
GROUP BY
SUM
ORDER BY
LIMIT
```

---

## 🎯 Lesson 03 Challenge

Write one query that produces this report:

```text
Customer Name
Customer Email
Order ID
Order Status
Product Name
Category
Quantity
Unit Price
```

The data should come from:

```text
customers
orders
order_items
products
categories
```

You'll need **four JOINs**.

This is the most important exercise in this lesson because it combines the database relationships from Lesson 01 with the SQL concepts from Lessons 02 and 03.

Once you're comfortable with this, **Lesson 04 — Advanced SQL** will cover **subqueries, CTEs, window functions, CASE, date functions, string functions, and conditional aggregation**.
