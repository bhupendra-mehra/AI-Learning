# SQL Subqueries, CTEs, Window Functions & Advanced Queries

## 03. Subqueries

A **subquery** is a query nested inside another SQL query.

```sql
SELECT value AS price
FROM catalog_product_entity_decimal
WHERE value > (
    SELECT AVG(value)
    FROM catalog_product_entity_decimal
    WHERE attribute_id = 77
);
```

---

## 03. Subquery with `WHERE` and `IN`

```sql
SELECT entity_id, email
FROM customer_entity
WHERE entity_id IN (
    SELECT customer_id
    FROM sales_order so
);
```

---

## 04. `NOT IN`

```sql
SELECT entity_id, email
FROM customer_entity
WHERE entity_id NOT IN (
    SELECT customer_id
    FROM sales_order so
);
```

---

## 05. `EXISTS`

`EXISTS` checks whether the subquery returns at least one row.

```sql
SELECT entity_id, email
FROM customer_entity ce
WHERE EXISTS (
    SELECT 1
    FROM sales_order so
    WHERE so.customer_id = ce.entity_id
);
```

---

## 06. `NOT EXISTS`

`NOT EXISTS` checks whether the subquery returns no rows.

```sql
SELECT entity_id, email
FROM customer_entity ce
WHERE NOT EXISTS (
    SELECT 1
    FROM sales_order so
    WHERE so.customer_id = ce.entity_id
);
```

---

# 07. `WITH` — CTE

**CTE (Common Table Expression):** A CTE allows us to create a temporary named result inside a query.

```sql
WITH expensive_orders AS (
    SELECT
        increment_id,
        grand_total
    FROM sales_order
    WHERE grand_total > 10000
)
SELECT COUNT(*)
FROM expensive_orders;
```

---

## 08. Real-World Example — Customers Who Spent More Than 50,000

```sql
WITH customer_sales AS (
    SELECT
        customer_id,
        SUM(grand_total) AS total_spent
    FROM sales_order
    GROUP BY customer_id
)
SELECT
    ce.firstname,
    ce.email,
    cs.total_spent
FROM customer_sales cs
JOIN customer_entity ce
    ON ce.entity_id = cs.customer_id
WHERE cs.total_spent > 50000;
```

---

# 09. Multiple CTEs

Multiple CTEs can be defined within the same query.

```sql
WITH customer_sales AS (
    SELECT
        customer_id,
        SUM(grand_total) AS total_spent
    FROM sales_order
    GROUP BY customer_id
),
top_customers AS (
    SELECT *
    FROM customer_sales
    WHERE total_spent > 50000
)
SELECT
    ce.firstname,
    tc.total_spent
FROM top_customers tc
JOIN customer_entity ce
    ON ce.entity_id = tc.customer_id;
```

---

# 10. Window Functions

A **window function** performs a calculation across related rows **without collapsing them into one row per group**.

### `GROUP BY` Example

```sql
SELECT
    customer_id,
    SUM(grand_total)
FROM sales_order so
GROUP BY customer_id;
```

With `GROUP BY`, multiple orders belonging to a customer are combined into a single row.

### Window Function Example

```sql
SELECT
    entity_id,
    so.customer_id,
    grand_total,
    SUM(grand_total) OVER (
        PARTITION BY so.customer_id
    ) AS customer_total
FROM sales_order so
WHERE so.customer_id IS NOT NULL
ORDER BY entity_id ASC;
```

Here, the individual orders remain visible while `customer_total` shows the customer's total spending.

---

# 11. `ROW_NUMBER()`

`ROW_NUMBER()` assigns a unique sequential number to each row within a partition.

```sql
SELECT
    entity_id,
    customer_id,
    grand_total,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id
        ORDER BY grand_total DESC
    ) AS order_rank
FROM sales_order
WHERE customer_id IS NOT NULL;
```

This can be useful for finding the **highest-value order for each customer**.

---

# 12. `RANK()`

`RANK()` assigns the same rank to rows with the same value, but creates gaps after a tie.

```sql
SELECT
    entity_id,
    customer_id,
    grand_total,
    RANK() OVER (
        ORDER BY grand_total DESC
    ) AS sales_rank
FROM sales_order
WHERE customer_id IS NOT NULL;
```

For example:

```text
grand_total    rank
-----------    ----
10000           1
9000            2
9000            2
8000            4
```

---

# 13. `DENSE_RANK()`

`DENSE_RANK()` also assigns the same rank to tied values, but **does not create a gap after a tie**.

```sql
SELECT
    entity_id,
    customer_id,
    grand_total,
    DENSE_RANK() OVER (
        ORDER BY grand_total DESC
    ) AS sales_rank
FROM sales_order
WHERE customer_id IS NOT NULL;
```

Example:

```text
grand_total    rank
-----------    ----
10000           1
9000            2
9000            2
8000            3
```

---

# 14. `LAG()`

`LAG()` allows us to access a value from a **previous row**.

```sql
SELECT
    entity_id,
    customer_id,
    grand_total,
    LAG(grand_total) OVER (
        PARTITION BY customer_id
        ORDER BY entity_id
    ) AS previous_order_amount
FROM sales_order
WHERE customer_id IS NOT NULL;
```

### Real-World Use Case

Useful for comparing a customer's current order with their previous order.

---

# 15. `LEAD()`

`LEAD()` allows us to access a value from the **next row**.

```sql
SELECT
    entity_id,
    customer_id,
    grand_total,
    LEAD(grand_total) OVER (
        PARTITION BY customer_id
        ORDER BY entity_id
    ) AS next_order_amount
FROM sales_order
WHERE customer_id IS NOT NULL;
```

### Real-World Use Case

Useful for comparing an order with a customer's next order.

---

# 16. `CASE`

`CASE` provides conditional logic in SQL.

```sql
SELECT
    entity_id,
    grand_total,
    CASE
        WHEN grand_total >= 5000 THEN 'High Value'
        WHEN grand_total >= 1000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS order_type
FROM sales_order so;
```

---

# 17. `CASE` with Status

```sql
SELECT
    entity_id,
    grand_total,
    CASE
        WHEN so.status = 'complete' THEN 'Successful'
        WHEN so.status = 'processing' THEN 'In Progress'
        WHEN so.status = 'pending' THEN 'Waiting'
        WHEN so.status = 'closed' THEN 'Completed'
        WHEN so.status = 'canceled' THEN 'Cancelled'
        ELSE 'Other'
    END AS status_group
FROM sales_order so;
```

---

# 18. String Functions

Common SQL string functions:

* `UPPER()` — Converts text to uppercase
* `LOWER()` — Converts text to lowercase
* `CONCAT()` — Combines strings
* `LENGTH()` — Returns string length
* `TRIM()` — Removes leading/trailing spaces
* `SUBSTRING()` — Extracts part of a string
* `REPLACE()` — Replaces part of a string

### `UPPER()`

```sql
SELECT UPPER(firstname)
FROM customer_entity ce;
```

### `LOWER()`

```sql
SELECT LOWER(firstname)
FROM customer_entity ce;
```

### `CONCAT()`

```sql
SELECT CONCAT(firstname, " ", ce.lastname)
FROM customer_entity ce;
```

### `LENGTH()`

```sql
SELECT
    UPPER(firstname),
    LENGTH(firstname)
FROM customer_entity ce;
```

### `TRIM()`

```sql
SELECT TRIM(firstname)
FROM customer_entity ce;
```

### `REPLACE()`

```sql
SELECT
    firstname,
    REPLACE(firstname, "A", "a")
FROM customer_entity ce;
```

---

# 19. Date and Time Functions

Common MySQL date and time functions:

* `NOW()` — Current date and time
* `CURDATE()` — Current date
* `DATE()` — Extracts date portion
* `YEAR()` — Extracts year
* `MONTH()` — Extracts month
* `DAY()` — Extracts day
* `DATEDIFF()` — Difference between two dates
* `DATE_ADD()` — Adds time to a date
* `DATE_SUB()` — Subtracts time from a date

### `NOW()`

```sql
SELECT NOW();
```

### `CURDATE()`

```sql
SELECT CURDATE();
```

### Extract Year and Month

```sql
SET SESSION sql_mode = (
    SELECT REPLACE(
        @@sql_mode,
        'ONLY_FULL_GROUP_BY',
        ''
    )
);

SELECT
    YEAR(created_at) AS year,
    MONTH(created_at) AS month
FROM sales_order
GROUP BY MONTH(created_at)
ORDER BY created_at DESC;
```

> **Note:** Disabling `ONLY_FULL_GROUP_BY` is generally better avoided in production queries. Prefer writing the `GROUP BY` so that all non-aggregated selected columns are handled correctly.

---

# 20. Orders Per Month

```sql
SELECT
    YEAR(created_at) AS year,
    MONTH(created_at) AS month,
    COUNT(*) AS order_count
FROM sales_order
GROUP BY
    YEAR(created_at),
    MONTH(created_at)
ORDER BY
    year,
    month;
```

### Real-World Use Case

This type of query can be used for an e-commerce dashboard to show monthly order volume.

---

# 21. `DATEDIFF()`

`DATEDIFF()` returns the difference between two dates.

```sql
SELECT DATEDIFF(
    '2026-09-15',
    '2026-09-01'
) AS days_difference;
```

**Result:**

```text
days_difference
---------------
14
```

---

# 22. Conditional Aggregation

Conditional aggregation is useful for creating **dashboard and reporting queries**.

### Order Status Summary

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

FROM sales_order;
```

---

## 23. Conditional Revenue Aggregation

```sql
SELECT
    SUM(grand_total) AS total_revenue,

    SUM(
        CASE
            WHEN status = 'complete'
            THEN grand_total
            ELSE 0
        END
    ) AS completed_revenue,

    SUM(
        CASE
            WHEN status = 'pending'
            THEN grand_total
            ELSE 0
        END
    ) AS pending_revenue

FROM sales_order;
```

### Real-World Use Case

This can be used to build an e-commerce dashboard showing:

* Total revenue
* Completed revenue
* Pending revenue

---

# 24. Customer Segmentation with `CASE`

```sql
SELECT
    c.firstname,
    SUM(o.grand_total) AS total_spent,

    CASE
        WHEN SUM(o.grand_total) >= 1000
            THEN 'VIP'

        WHEN SUM(o.grand_total) >= 500
            THEN 'Premium'

        ELSE 'Regular'
    END AS customer_segment

FROM customer_entity c

JOIN sales_order o
    ON c.entity_id = o.customer_id

GROUP BY
    c.entity_id,
    c.firstname;
```

### Logic

```text
Total Spent >= 1000  → VIP
Total Spent >= 500   → Premium
Otherwise            → Regular
```

---

# 25. Top Customer Per Category

This is a more advanced real-world Magento query combining:

* CTEs
* Multiple `JOIN`s
* Aggregation
* `GROUP BY`
* Window functions
* `ROW_NUMBER()`

```sql
WITH customer_category_sales AS (
    SELECT
        c.entity_id AS customer_id,
        CONCAT(c.firstname, " ", c.lastname) AS customer_name,
        cat.entity_id AS category_id,

        SUM(
            oi.qty_ordered * oi.price
        ) AS total_spent

    FROM customer_entity c

    JOIN sales_order o
        ON c.entity_id = o.customer_id

    JOIN sales_order_item oi
        ON o.entity_id = oi.order_id

    JOIN catalog_product_entity p
        ON oi.product_id = p.entity_id

    JOIN catalog_category_product cat
        ON p.entity_id = cat.product_id

    GROUP BY
        c.entity_id,
        c.firstname,
        c.lastname,
        cat.entity_id
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
    category_id,
    customer_name,
    total_spent
FROM ranked_customers
WHERE customer_rank = 1;
```

### What This Query Does

The query first calculates how much each customer has spent within each category:

```text
Customer → Category → Total Spent
```

Then `ROW_NUMBER()` ranks customers separately within each category:

```text
Category  Customer       Total Spent   Rank
--------  -------------  ------------  ----
10        John Smith     15000         1
10        David Brown    12000         2
10        Mike Jones      9000         3

20        David Brown    18000         1
20        John Smith     14000         2
20        Mike Jones     7000          3
```

Finally:

```sql
WHERE customer_rank = 1
```

returns the top-spending customer for each category.
