# Lesson 04 — Advanced SQL

We now move from basic SQL and JOINs into **advanced SQL techniques used in real applications, reporting, analytics, and backend systems**.

For this lesson, we'll continue using our e-commerce database:

```text
customers
orders
order_items
products
categories
```

---

# 1. What You'll Learn

By the end of this lesson, you'll understand:

```text
01  Subqueries
02  Common Table Expressions (CTEs)
03  Window Functions
04  CASE expressions
05  String Functions
06  Date/Time Functions
07  Conditional Aggregation
08  Combining these techniques
```

These are especially useful for:

* Magento reporting
* e-commerce analytics
* customer segmentation
* sales reports
* data extraction
* backend services
* ETL pipelines
* AI/data preparation

---

# 2. Subqueries

A **subquery** is a SQL query inside another SQL query.

Example requirement:

> Find products that are more expensive than the average product price.

First, find the average:

```sql
SELECT AVG(price)
FROM products;
```

Then use that result:

```sql
SELECT name, price
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
);
```

The inner query:

```sql
SELECT AVG(price)
FROM products
```

runs conceptually first and produces a value.

The outer query uses that value.

---

# 3. Subquery with WHERE

Example:

> Find customers who have placed at least one order.

```sql
SELECT name
FROM customers
WHERE id IN (
    SELECT customer_id
    FROM orders
);
```

The inner query gives:

```text
1
2
```

The outer query finds those customers.

---

# 4. NOT IN

Find customers who have never placed an order:

```sql
SELECT name
FROM customers
WHERE id NOT IN (
    SELECT customer_id
    FROM orders
);
```

This can work, but there is an important real-world caveat:

**`NULL` values can make `NOT IN` behave unexpectedly.**

A safer/common alternative is `NOT EXISTS`, which we'll see next.

---

# 5. EXISTS

`EXISTS` asks:

> Does at least one matching row exist?

Example:

```sql
SELECT
    c.name,
    c.email
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.id
);
```

Meaning:

> Return the customer if at least one order exists for that customer.

---

# 6. NOT EXISTS

Find customers with no orders:

```sql
SELECT
    c.name,
    c.email
FROM customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.id
);
```

This is a very useful pattern.

---

# 7. Correlated Subquery

Notice this:

```sql
WHERE o.customer_id = c.id
```

The inner query references the outer query's `c.id`.

That's a **correlated subquery**.

Conceptually:

```text
Customer 1
   ↓
Check orders for Customer 1

Customer 2
   ↓
Check orders for Customer 2

Customer 3
   ↓
Check orders for Customer 3
```

Correlated queries can be useful, but on large datasets they may be expensive. Later, we'll learn how JOINs and window functions can sometimes provide better alternatives.

---

# 8. Common Table Expressions — CTE

A CTE allows us to create a temporary named result inside a query.

Syntax:

```sql
WITH name AS (
    SELECT ...
)
SELECT ...
FROM name;
```

Example:

```sql
WITH expensive_products AS (
    SELECT
        name,
        price
    FROM products
    WHERE price > 10000
)
SELECT *
FROM expensive_products;
```

Think of it as:

```text
Complex query
     ↓
Give result a name
     ↓
Use that result
```

---

# 9. Why CTEs Are Useful

Imagine this complicated query:

```sql
SELECT ...
FROM (
    SELECT ...
    FROM ...
    JOIN ...
    GROUP BY ...
) AS customer_sales;
```

A CTE can make it easier to read:

```sql
WITH customer_sales AS (
    SELECT
        customer_id,
        SUM(total_amount) AS total_spent
    FROM orders
    GROUP BY customer_id
)
SELECT *
FROM customer_sales;
```

This becomes much easier to maintain.

---

# 10. Real-World CTE Example

Requirement:

> Find customers who have spent more than ₹50,000.

```sql
WITH customer_sales AS (
    SELECT
        customer_id,
        SUM(total_amount) AS total_spent
    FROM orders
    GROUP BY customer_id
)
SELECT
    c.name,
    c.email,
    cs.total_spent
FROM customer_sales cs
JOIN customers c
    ON c.id = cs.customer_id
WHERE cs.total_spent > 50000;
```

We first calculate:

```text
customer → total spending
```

Then join it with customer information.

---

# 11. Multiple CTEs

You can define multiple CTEs.

```sql
WITH customer_sales AS (
    SELECT
        customer_id,
        SUM(total_amount) AS total_spent
    FROM orders
    GROUP BY customer_id
),
top_customers AS (
    SELECT *
    FROM customer_sales
    WHERE total_spent > 50000
)
SELECT
    c.name,
    tc.total_spent
FROM top_customers tc
JOIN customers c
    ON c.id = tc.customer_id;
```

This makes complex analytical queries much easier to understand.

---

# 12. Window Functions

This is one of the most important advanced SQL concepts.

A window function performs a calculation across related rows **without collapsing them into one row per group**.

Compare:

### GROUP BY

```sql
SELECT
    customer_id,
    SUM(total_amount)
FROM orders
GROUP BY customer_id;
```

This produces one row per customer.

### Window Function

```sql
SELECT
    id,
    customer_id,
    total_amount,
    SUM(total_amount) OVER (
        PARTITION BY customer_id
    ) AS customer_total
FROM orders;
```

Now every order remains visible.

Example:

| order | customer | amount | customer_total |
| ----: | -------: | -----: | -------------: |
|  1001 |        1 |  62000 |          65000 |
|  1003 |        1 |   3000 |          65000 |
|  1002 |        2 |  18000 |          18000 |

This is a major difference.

---

# 13. PARTITION BY

Think of:

```sql
PARTITION BY customer_id
```

as:

> Create a logical group for each customer, but don't merge the rows.

Example:

```text
Customer 1
 ├── Order 1001
 └── Order 1003

Customer 2
 └── Order 1002
```

Then:

```sql
SUM(...) OVER (PARTITION BY customer_id)
```

calculates the total separately for each customer.

---

# 14. ROW_NUMBER()

Suppose we want to number each customer's orders.

```sql
SELECT
    id,
    customer_id,
    total_amount,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id
        ORDER BY total_amount DESC
    ) AS order_rank
FROM orders;
```

Result conceptually:

| order | customer | amount | rank |
| ----: | -------: | -----: | ---: |
|  1001 |        1 |  62000 |    1 |
|  1003 |        1 |   3000 |    2 |
|  1002 |        2 |  18000 |    1 |

---

# 15. RANK()

`RANK()` handles ties differently.

```sql
SELECT
    id,
    total_amount,
    RANK() OVER (
        ORDER BY total_amount DESC
    ) AS sales_rank
FROM orders;
```

If two orders have the same amount:

```text
1001 → 62000 → Rank 1
1004 → 62000 → Rank 1
1002 → 18000 → Rank 3
```

Notice the gap.

---

# 16. DENSE_RANK()

`DENSE_RANK()` doesn't create a gap after a tie.

```text
RANK:
1
1
3

DENSE_RANK:
1
1
2
```

Useful when creating rankings such as:

* top customers
* top products
* sales rankings
* category rankings

---

# 17. LAG()

`LAG()` lets us access a previous row.

Example:

```sql
SELECT
    id,
    customer_id,
    total_amount,
    LAG(total_amount) OVER (
        PARTITION BY customer_id
        ORDER BY id
    ) AS previous_order_amount
FROM orders;
```

Result conceptually:

| order | amount | previous |
| ----: | -----: | -------: |
|  1001 |  62000 |     NULL |
|  1003 |   3000 |    62000 |

This is useful for:

* comparing previous purchases
* sales trends
* month-over-month analysis
* customer behavior

---

# 18. LEAD()

`LEAD()` looks at the next row.

```sql
SELECT
    id,
    total_amount,
    LEAD(total_amount) OVER (
        ORDER BY id
    ) AS next_order_amount
FROM orders;
```

Think:

```text
LAG  → previous
LEAD → next
```

---

# 19. CASE

`CASE` is SQL's conditional logic.

Example:

```sql
SELECT
    id,
    total_amount,
    CASE
        WHEN total_amount >= 50000 THEN 'High Value'
        WHEN total_amount >= 10000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS order_type
FROM orders;
```

Result:

| order | amount | order_type   |
| ----: | -----: | ------------ |
|  1001 |  62000 | High Value   |
|  1002 |  18000 | Medium Value |
|  1003 |   3000 | Low Value    |

This is similar conceptually to Python:

```python
if amount >= 50000:
    ...
elif amount >= 10000:
    ...
else:
    ...
```

---

# 20. CASE with Status

```sql
SELECT
    id,
    status,
    CASE
        WHEN status = 'complete' THEN 'Successful'
        WHEN status = 'processing' THEN 'In Progress'
        WHEN status = 'pending' THEN 'Waiting'
        ELSE 'Other'
    END AS status_group
FROM orders;
```

Very useful for reporting.

---

# 21. String Functions

SQL also provides functions for manipulating text.

Common functions include:

```text
UPPER()
LOWER()
CONCAT()
LENGTH()
TRIM()
SUBSTRING()
REPLACE()
```

---

## UPPER

```sql
SELECT UPPER(name)
FROM customers;
```

---

## LOWER

```sql
SELECT LOWER(email)
FROM customers;
```

Useful for normalized comparisons and data processing.

---

## CONCAT

```sql
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name
FROM customers;
```

Result:

```text
Bhupendra Mehra
```

---

## TRIM

```sql
SELECT TRIM(name)
FROM customers;
```

Removes leading/trailing whitespace.

---

## REPLACE

```sql
SELECT
    REPLACE(email, '@example.com', '@company.com')
FROM customers;
```

Useful for data transformation, although you should be careful when changing production data.

---

# 22. Date and Time Functions

E-commerce systems depend heavily on dates.

Example:

```text
created_at
updated_at
order_date
payment_date
```

Common SQL functions vary somewhat by database, but in MySQL you'll frequently encounter:

```text
NOW()
CURDATE()
DATE()
YEAR()
MONTH()
DAY()
DATEDIFF()
DATE_ADD()
DATE_SUB()
```

---

# 23. Current Date/Time

```sql
SELECT NOW();
```

Returns the current date and time.

Current date:

```sql
SELECT CURDATE();
```

---

# 24. Extract Year/Month

```sql
SELECT
    YEAR(created_at) AS year,
    MONTH(created_at) AS month
FROM orders;
```

Useful for reports such as:

```text
2026
August
```

---

# 25. Orders Per Month

A typical analytics query:

```sql
SELECT
    YEAR(created_at) AS year,
    MONTH(created_at) AS month,
    COUNT(*) AS order_count
FROM orders
GROUP BY
    YEAR(created_at),
    MONTH(created_at)
ORDER BY
    year,
    month;
```

This gives:

```text
Year | Month | Orders
2026 | 07    | 150
2026 | 08    | 230
2026 | 09    | 190
```

---

# 26. DATEDIFF()

Find the number of days between two dates:

```sql
SELECT
    DATEDIFF('2026-09-15', '2026-09-01') AS days_difference;
```

Result:

```text
14
```

Real-world use cases:

* delivery time
* customer inactivity
* subscription duration
* order aging

---

# 27. Conditional Aggregation

This is extremely useful for dashboards.

Suppose we want:

```text
Total Orders
Completed Orders
Pending Orders
```

We could write:

```sql
SELECT
    COUNT(*) AS total_orders,

    SUM(
        CASE
            WHEN status = 'complete' THEN 1
            ELSE 0
        END
    ) AS completed_orders,

    SUM(
        CASE
            WHEN status = 'pending' THEN 1
            ELSE 0
        END
    ) AS pending_orders

FROM orders;
```

Result:

```text
total_orders | completed_orders | pending_orders
-------------|------------------|---------------
1000         | 700              | 100
```

This technique is called **conditional aggregation**.

---

# 28. Conditional Revenue

We can do the same with money.

```sql
SELECT
    SUM(total_amount) AS total_revenue,

    SUM(
        CASE
            WHEN status = 'complete'
            THEN total_amount
            ELSE 0
        END
    ) AS completed_revenue,

    SUM(
        CASE
            WHEN status = 'pending'
            THEN total_amount
            ELSE 0
        END
    ) AS pending_revenue

FROM orders;
```

This is very useful for e-commerce dashboards.

---

# 29. Combining JOIN + CASE + GROUP BY

Now let's create something closer to a real business report.

> Show each customer and categorize their total spending.

```sql
SELECT
    c.name,
    SUM(o.total_amount) AS total_spent,

    CASE
        WHEN SUM(o.total_amount) >= 100000
            THEN 'VIP'

        WHEN SUM(o.total_amount) >= 50000
            THEN 'Premium'

        ELSE 'Regular'
    END AS customer_segment

FROM customers c

JOIN orders o
    ON c.id = o.customer_id

GROUP BY
    c.id,
    c.name;
```

Result:

| customer  | total spent | segment |
| --------- | ----------: | ------- |
| Bhupendra |       65000 | Premium |
| Amit      |       18000 | Regular |

This is a real-world customer segmentation query.

---

# 30. Advanced Example — Top Customer Per Category

Now combine several concepts.

Suppose we want to determine the highest-spending customer in each product category.

The general approach is:

```text
JOIN
   ↓
GROUP BY
   ↓
calculate customer/category spending
   ↓
ROW_NUMBER()
   ↓
select rank = 1
```

Example:

```sql
WITH customer_category_sales AS (
    SELECT
        c.id AS customer_id,
        c.name AS customer_name,
        cat.id AS category_id,
        cat.name AS category_name,
        SUM(oi.quantity * oi.unit_price) AS total_spent
    FROM customers c

    JOIN orders o
        ON c.id = o.customer_id

    JOIN order_items oi
        ON o.id = oi.order_id

    JOIN products p
        ON oi.product_id = p.id

    JOIN categories cat
        ON p.category_id = cat.id

    GROUP BY
        c.id,
        c.name,
        cat.id,
        cat.name
),

ranked_customers AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY category_id
            ORDER BY total_spent DESC
        ) AS customer_rank
    FROM customer_category_sales
)

SELECT
    category_name,
    customer_name,
    total_spent
FROM ranked_customers
WHERE customer_rank = 1;
```

This is the type of SQL you'll encounter when moving into **analytics/data engineering**.

---

# 31. Advanced SQL Mental Model

At this point, think of SQL as a set of building blocks:

```text
FILTER
  ↓
WHERE

CONNECT
  ↓
JOIN

GROUP
  ↓
GROUP BY

FILTER GROUPS
  ↓
HAVING

CONDITIONAL LOGIC
  ↓
CASE

CALCULATE ACROSS ROWS
  ↓
WINDOW FUNCTIONS

BUILD COMPLEX QUERIES
  ↓
CTE

TRANSFORM DATA
  ↓
STRING / DATE FUNCTIONS
```

---

# 32. Which Concepts Matter Most for Your Career?

Given your Magento/backend + future AI/data direction, prioritize them like this:

### 🔴 Must Know

```text
JOIN
GROUP BY
HAVING
CASE
Subqueries
CTE
Window Functions
Date Functions
```

### 🟠 Very Useful

```text
EXISTS
NOT EXISTS
Conditional Aggregation
String Functions
LAG / LEAD
```

### 🟢 Later / Situational

```text
Complex recursive CTEs
Database-specific advanced functions
```

You don't need to memorize every SQL function. You need to understand **how to solve a data problem using SQL**.

---

# 33. Practical Exercise

Use our e-commerce tables.

### Q1 — Subquery

Find products whose price is greater than the average product price.

---

### Q2 — EXISTS

Find customers who have at least one order.

Use:

```sql
EXISTS
```

---

### Q3 — NOT EXISTS

Find customers who have never placed an order.

Use:

```sql
NOT EXISTS
```

---

### Q4 — CTE

Create a CTE called:

```text
customer_sales
```

that calculates:

```text
customer_id
total_spent
```

Then return customers whose spending is greater than ₹50,000.

---

### Q5 — CASE

Classify orders:

```text
>= 50000 → High
>= 10000 → Medium
< 10000  → Low
```

---

### Q6 — Window Function

Display every order along with the customer's total spending.

Use:

```sql
SUM() OVER (
    PARTITION BY customer_id
)
```

---

### Q7 — ROW_NUMBER

Number each customer's orders based on highest order value.

Use:

```sql
ROW_NUMBER()
```

---

### Q8 — LAG

Show each customer's current order amount and their previous order amount.

Use:

```sql
LAG()
```

---

### Q9 — Date Analysis

Find the number of orders for each month.

Use:

```text
YEAR()
MONTH()
COUNT()
GROUP BY
```

---

### Q10 — Conditional Aggregation

Return:

```text
total_orders
completed_orders
processing_orders
pending_orders
```

in **one row**.

---

# 🎯 Final Lesson Challenge

Build an **E-commerce Customer Analytics Report** using SQL.

The final output should contain:

```text
Customer Name
Customer Email
Total Orders
Total Spent
Average Order Value
Customer Segment
```

Customer segment:

```text
Total Spent >= 100000 → VIP
Total Spent >= 50000  → Premium
Otherwise             → Regular
```

Your query should demonstrate:

```text
JOIN
GROUP BY
COUNT
SUM
AVG
CASE
```

### ⭐ Bonus

Add:

```text
Customer Rank
```

based on total spending using:

```sql
RANK() OVER (...)
```

---

## What comes next

After this lesson, we move to:

**Lesson 05 — Database Design**

We'll go deeper into:

```text
Entity Relationships
1:1
1:N
N:N
Normalization
Indexes
Constraints
Schema Design
E-commerce Database Architecture
```

And importantly, we'll start thinking about **how to design a database before writing the code**, which is a key senior-engineering skill.
