# Lesson 03 — Vectorized Operations, Statistics and Broadcasting

## 1. Learning Objectives

By completing this lesson, I will be able to:

- Perform vectorized arithmetic on NumPy arrays.
- Apply mathematical operations to every element without explicit loops.
- Understand broadcasting rules and combine arrays of compatible shapes.
- Calculate totals, averages, minimums, maximums, and standard deviations.
- Perform aggregations along rows and columns using the `axis` parameter.
- Calculate cumulative sums and differences.
- Apply discounts, tax rates, and sales calculations to arrays.
- Identify and resolve common broadcasting and shape-mismatch errors.

## 2. Prerequisites

- Lesson 01: NumPy Introduction and Arrays.
- Lesson 02: Array Indexing, Slicing and Shapes.
- Basic Python arithmetic and functions.
- NumPy installed in the Part 7 virtual environment.

## 3. What Is Vectorization?

Vectorization means applying an operation to an entire array without writing an explicit Python loop for each element.

Consider product sales:

```python
sales = [100, 200, 300, 400]
```

Using a Python loop:

```python
sales = [100, 200, 300, 400]

updated_sales = []

for amount in sales:
    updated_sales.append(amount * 1.10)

print(updated_sales)
```

Using NumPy:

```python
import numpy as np

sales = np.array([100, 200, 300, 400])

updated_sales = sales * 1.10

print(updated_sales)
```

Output:

```text
[110. 220. 330. 440.]
```

NumPy applies the multiplication to every element.

Vectorized operations are often faster and more concise than Python loops for large numerical arrays.

## 4. Vectorized Arithmetic Operations

NumPy supports arithmetic operations directly on arrays.

### 4.1 Addition

```python
import numpy as np

sales = np.array([100, 200, 300])

print(sales + 50)
```

Output:

```text
[150 250 350]
```

Adds 50 to every element.

### 4.2 Subtraction

```python
print(sales - 20)
```

Output:

```text
[ 80 180 280]
```

Subtracts 20 from every element.

### 4.3 Multiplication

```python
print(sales * 2)
```

Output:

```text
[200 400 600]
```

Multiplies every element by two.

### 4.4 Division

```python
print(sales / 2)
```

Output:

```text
[ 50. 100. 150.]
```

Ordinary division produces floating-point results.

### 4.5 Powers

```python
print(sales ** 2)
```

Output:

```text
[ 10000  40000  90000]
```

Raises each element to the power of two.

### 4.6 Operations between two arrays

```python
prices = np.array([100, 200, 300])
quantities = np.array([2, 3, 4])

revenue = prices * quantities

print(revenue)
```

Output:

```text
[ 200  600 1200]
```

Corresponding elements are multiplied.

The arrays must have compatible shapes for the operation to work.

## 5. Practical Example — Revenue, Discount and Tax

Suppose an online store has three products.

```python
import numpy as np

prices = np.array([1000, 2000, 3000])
quantities = np.array([2, 3, 1])

revenue = prices * quantities
discount = revenue * 0.10
net_before_tax = revenue - discount
tax = net_before_tax * 0.18
total_after_tax = net_before_tax + tax

print("Revenue:", revenue)
print("Discount:", discount)
print("Net before tax:", net_before_tax)
print("Tax:", tax)
print("Total after tax:", total_after_tax)
```

Output:

```text
Revenue: [2000 6000 3000]
Discount: [200. 600. 300.]
Net before tax: [1800. 5400. 2700.]
Tax: [324. 972. 486.]
Total after tax: [2124. 6372. 3186.]
```

This example uses a simplified calculation with a uniform discount and tax rate. Actual tax treatment depends on the product and applicable tax rules.

## 6. What Is Broadcasting?

Broadcasting allows NumPy to perform operations between arrays with different but compatible shapes.

For example:

```python
import numpy as np

sales = np.array([100, 200, 300])

print(sales + 10)
```

Output:

```text
[110 210 310]
```

The scalar `10` is applied to each element. NumPy does not require you to create a separate array containing three tens.

### 6.1 Broadcasting a scalar

```python
prices = np.array([100, 200, 300])

print(prices * 1.18)
```

Output:

```text
[118. 236. 354.]
```

The same multiplier is applied to every price.

### 6.2 Broadcasting a one-dimensional array across rows

```python
sales = np.array([
    [100, 200, 300],
    [400, 500, 600],
])

adjustments = np.array([10, 20, 30])

print(sales + adjustments)
```

Output:

```text
[[110 220 330]
 [410 520 630]]
```

The adjustments are applied to each row.

The shapes are:

- `sales`: `(2, 3)`
- `adjustments`: `(3,)`

NumPy treats the one-dimensional array as compatible with each row.

### 6.3 Broadcasting across columns

```python
sales = np.array([
    [100, 200, 300],
    [400, 500, 600],
])

monthly_adjustments = np.array([10, 20])

adjusted_sales = sales + monthly_adjustments[:, np.newaxis]

print(adjusted_sales)
```

Output:

```text
[[110 210 310]
 [420 520 620]]
```

Here, the adjustments have been reshaped to `(2, 1)`, allowing each row to receive its own adjustment.

`np.newaxis` adds a new dimension.

### 6.4 Broadcasting rules

NumPy compares array dimensions from right to left.

Two dimensions are compatible when:

- They are equal, or
- One of them is `1`.

Missing dimensions are treated as having size `1`.

Examples:

| Shape A  | Shape B  | Result       |
| -------- | -------- | ------------ |
| `(2, 3)` | `(3,)`   | `(2, 3)`     |
| `(2, 3)` | `(2, 1)` | `(2, 3)`     |
| `(4, 1)` | `(1, 3)` | `(4, 3)`     |
| `(2, 3)` | `(2,)`   | Incompatible |

### 6.5 Common broadcasting error

Incorrect:

```python
sales = np.array([
    [100, 200, 300],
    [400, 500, 600],
])

adjustments = np.array([10, 20])

print(sales + adjustments)
```

This raises a `ValueError` because the last dimensions, `3` and `2`, are neither equal nor `1`.

Correct:

```python
print(sales + adjustments[:, np.newaxis])
```

Understanding shapes helps prevent these errors.

## 7. Statistical Functions

NumPy provides functions for summarizing numerical data.

```python
import numpy as np

sales = np.array([1200, 1500, 900, 1800, 2100])

print("Total:", np.sum(sales))
print("Mean:", np.mean(sales))
print("Median:", np.median(sales))
print("Minimum:", np.min(sales))
print("Maximum:", np.max(sales))
print("Standard deviation:", np.std(sales))
print("Variance:", np.var(sales))
```

Expected output:

```text
Total: 7500
Mean: 1500.0
Median: 1500.0
Minimum: 900
Maximum: 2100
Standard deviation: 424.26406871192853
Variance: 180000.0
```

The exact displayed precision can vary with formatting.

### Actual use of each function

| Function          | Description                                             |
| ----------------- | ------------------------------------------------------- |
| `np.sum()`        | Adds values together.                                   |
| `np.mean()`       | Calculates the arithmetic average.                      |
| `np.median()`     | Returns the middle value after sorting.                 |
| `np.min()`        | Returns the smallest value.                             |
| `np.max()`        | Returns the largest value.                              |
| `np.std()`        | Measures the spread of values using standard deviation. |
| `np.var()`        | Measures spread using variance.                         |
| `np.percentile()` | Calculates a percentile, such as the 75th percentile.   |
| `np.argmax()`     | Returns the index of the maximum value.                 |
| `np.argmin()`     | Returns the index of the minimum value.                 |

By default, `np.std()` and `np.var()` calculate population statistics using `ddof=0`. Use `ddof=1` for the common sample-standard-deviation or sample-variance calculation.

## 8. Understanding the `axis` Parameter

The `axis` parameter determines which dimension is reduced during an aggregation.

Consider this sales dataset:

```python
import numpy as np

sales = np.array([
    [100, 200, 300],
    [400, 500, 600],
])
```

Each row represents a product, and each column represents a month.

### 8.1 Sum all values

```python
print(np.sum(sales))
```

Output:

```text
2100
```

### 8.2 Sum along `axis=0`

```python
print(np.sum(sales, axis=0))
```

Output:

```text
[500 700 900]
```

This calculates the total for each column:

- First month: 100 + 400 = 500
- Second month: 200 + 500 = 700
- Third month: 300 + 600 = 900

The row dimension is reduced.

### 8.3 Sum along `axis=1`

```python
print(np.sum(sales, axis=1))
```

Output:

```text
[ 600 1500]
```

This calculates the total for each row:

- First product: 100 + 200 + 300 = 600
- Second product: 400 + 500 + 600 = 1500

The column dimension is reduced.

### 8.4 Calculate averages along axes

```python
print(np.mean(sales, axis=0))
print(np.mean(sales, axis=1))
```

Output:

```text
[250. 350. 450.]
[200. 500.]
```

### Axis summary

| Expression               | Meaning              |
| ------------------------ | -------------------- |
| `np.sum(sales)`          | Sum every element.   |
| `np.sum(sales, axis=0)`  | Sum each column.     |
| `np.sum(sales, axis=1)`  | Sum each row.        |
| `np.mean(sales, axis=0)` | Average each column. |
| `np.mean(sales, axis=1)` | Average each row.    |

A useful way to remember it: the specified axis is the dimension being reduced.

## 9. Cumulative Calculations

Cumulative functions calculate a running total or product.

### 9.1 Cumulative sum

```python
sales = np.array([100, 200, 300, 400])

print(np.cumsum(sales))
```

Output:

```text


```

Each value is the total up to that position.

### 9.2 Cumulative product

```python
values = np.array([2, 3, 4])

print(np.cumprod(values))
```

Output:

```text
[ 2  6 24]
```

### 9.3 Differences between adjacent values

```python
sales = np.array([100, 150, 130, 200])

print(np.diff(sales))
```

Output:

```text
[ 50 -20  70]
```

This shows the change between consecutive observations.

These functions are useful for cumulative revenue, running totals, and period-to-period changes.

## 10. Additional Useful Operations

| Function            | Actual use                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------ |
| `np.add()`          | Element-wise addition.                                                                                 |
| `np.subtract()`     | Element-wise subtraction.                                                                              |
| `np.multiply()`     | Element-wise multiplication.                                                                           |
| `np.divide()`       | Element-wise division.                                                                                 |
| `np.round()`        | Rounds numerical values.                                                                               |
| `np.clip()`         | Restricts values to a specified range.                                                                 |
| `np.where()`        | Selects values based on a condition.                                                                   |
| `np.percentile()`   | Calculates a specified percentile.                                                                     |
| `np.cumsum()`       | Calculates cumulative sums.                                                                            |
| `np.diff()`         | Calculates adjacent differences.                                                                       |
| `np.broadcast_to()` | Presents an array as a specified broadcast-compatible shape; the returned view is typically read-only. |

Example:

```python
import numpy as np

sales = np.array([500, 1200, 1800, 2500])

categories = np.where(sales >= 1500, "High", "Low")
limited_sales = np.clip(sales, 600, 2000)

print(categories)
print(limited_sales)
```

Output:

```text
['Low' 'Low' 'High' 'High']
[ 600 1200 1800 2000]
```

## 11. Complete Practical Exercise

Create the file:

`lessons/03-numpy-statistics-broadcasting/lesson03_numpy.py`

```python
import numpy as np

# Product sales across three months.
sales = np.array([
    [1200, 1500, 1800],
    [900, 2100, 2500],
    [700, 1100, 1600],
])

print("Sales data:")
print(sales)

# Vectorized discount.
discounted_sales = sales * 0.90
print("\nSales after 10% discount:")
print(discounted_sales)

# Overall statistics.
print("\nTotal sales:", np.sum(sales))
print("Average sales:", np.mean(sales))
print("Minimum sales:", np.min(sales))
print("Maximum sales:", np.max(sales))

# Aggregate by month and by product.
print("\nMonthly totals:", np.sum(sales, axis=0))
print("Product totals:", np.sum(sales, axis=1))

# Broadcasting: apply a separate adjustment to each product.
adjustments = np.array([100, 200, 300])
adjusted_sales = sales + adjustments[:, np.newaxis]

print("\nAdjusted sales:")
print(adjusted_sales)

# Cumulative calculations.
monthly_totals = np.sum(sales, axis=0)

print("\nCumulative monthly sales:", np.cumsum(monthly_totals))
print("Month-to-month differences:", np.diff(monthly_totals))

# Classify individual sales values.
categories = np.where(sales >= 1500, "High", "Low")

print("\nSales categories:")
print(categories)
```

Run the script:

```bash
python lessons/03-numpy-statistics-broadcasting/lesson03_numpy.py
```

## 12. Homework

Create `homework.py` in the same lesson directory.

Use this dataset:

```python
import numpy as np

sales = np.array([
    [1200, 1500, 1800, 2000],
    [900, 2100, 2500, 2300],
    [700, 1100, 1600, 1900],
])
```

Complete these tasks:

1. Calculate the total sales across the complete dataset.
2. Calculate the average, minimum, and maximum values.
3. Calculate the total sales for each month using `axis=0`.
4. Calculate the total sales for each product using `axis=1`.
5. Apply a 15% discount to every element.
6. Add monthly adjustments of `[100, 200, 300, 400]` to each row.
7. Add product adjustments of `[50, 100, 150]`, applying a different adjustment to each row.
8. Calculate the cumulative sum of monthly totals.
9. Calculate the differences between consecutive monthly totals.
10. Use `np.where()` to classify sales of at least 1,800 as `"High"` and the remaining values as `"Low"`.
11. Calculate the 75th percentile of all sales values.
12. Explain in your own words why a `(3, 4)` array cannot directly be added to a `(3,)` array.

Try to complete the tasks before looking at the solution below.

### Homework solution

\<details>
\<summary>Show solution\</summary>

```python
import numpy as np

sales = np.array([
    [1200, 1500, 1800, 2000],
    [900, 2100, 2500, 2300],
    [700, 1100, 1600, 1900],
])

print("Total:", np.sum(sales))
print("Average:", np.mean(sales))
print("Minimum:", np.min(sales))
print("Maximum:", np.max(sales))

monthly_totals = np.sum(sales, axis=0)
product_totals = np.sum(sales, axis=1)

print("Monthly totals:", monthly_totals)
print("Product totals:", product_totals)

print("After 15% discount:", sales * 0.85)

monthly_adjustments = np.array([100, 200, 300, 400])
print("Monthly adjustments:", sales + monthly_adjustments)

product_adjustments = np.array([50, 100, 150])
print(
    "Product adjustments:",
    sales + product_adjustments[:, np.newaxis],
)

print("Cumulative monthly totals:", np.cumsum(monthly_totals))
print("Monthly differences:", np.diff(monthly_totals))

print("Sales categories:", np.where(sales >= 1800, "High", "Low"))
print("75th percentile:", np.percentile(sales, 75))
```

\</details>

## 13. Common Mistakes

### Using incompatible array shapes

Incorrect:

```python
sales = np.array([[100, 200, 300], [400, 500, 600]])
adjustments = np.array([10, 20])

print(sales + adjustments)
```

The final dimensions are 3 and 2, which are incompatible for broadcasting.

### Confusing `axis=0` and `axis=1`

For an array shaped `(2, 3)`:

- `axis=0` reduces the rows and produces three column totals.
- `axis=1` reduces the columns and produces two row totals.

### Using a Python loop when vectorization is straightforward

Instead of:

```python
updated = []

for value in sales:
    updated.append(value * 1.10)
```

Use:

```python
updated = sales * 1.10
```

Loops are still useful when operations require conditional or sequential logic that cannot be expressed cleanly with array operations.

### Confusing element-wise multiplication with matrix multiplication

```python
a * b
```

Performs element-wise multiplication for compatible arrays.

```python
a @ b
```

Performs matrix multiplication when the dimensions are appropriate.

## 14. Completion Checklist

- [x] Practiced vectorized arithmetic.
- [x] Applied operations between arrays and scalar values.
- [x] Understood broadcasting compatibility rules.
- [x] Used broadcasting across rows and columns.
- [x] Calculated statistical summaries.
- [x] Used `axis=0` and `axis=1`.
- [x] Practiced cumulative sums and differences.
- [x] Completed the practical exercise.
- [x] Completed the homework.
- [x] Committed lesson code and documentation to GitHub.

## Summary

Here's each topic in plain words, with one small example.

**1. Arrays**
A NumPy array is a grid of numbers, all of the same type. It's like a Python list, but faster and built for math.

```python
import numpy as np
a = np.array([10, 20, 30, 40])
print(a)          # [10 20 30 40]
```

**2. Indexing**
Indexing means picking out specific items from an array by their position (starting from 0), or by a condition.

```python
a = np.array([10, 20, 30, 40, 50])
print(a[1])        # 20  (second item)
print(a[1:4])      # [20 30 40]  (slice)
print(a[a > 25])   # [30 40 50]  (boolean filter)
```

**3. Vectorization**
Vectorization means doing an operation on the whole array at once, without writing a loop. It's shorter to write and much faster to run.

```python
prices = np.array([100, 200, 300])
print(prices * 1.18)   # [118. 236. 354.]  (add 18% tax to all)
```

With a plain list you'd need a `for` loop for the same thing.

**4. Broadcasting**
Broadcasting lets NumPy do math between arrays of different shapes by "stretching" the smaller one to fit the bigger one automatically.

```python
m = np.array([[1, 2, 3],
              [4, 5, 6]])
row = np.array([10, 20, 30])
print(m + row)
# [[11 22 33]
#  [14 25 36]]
```

The single row `[10, 20, 30]` was added to every row of the matrix.

**5. Statistics**
NumPy has built-in functions to summarize data quickly: average, middle value, spread, and so on.

```python
scores = np.array([60, 70, 80, 90, 100])
print(np.mean(scores))     # 80.0  (average)
print(np.median(scores))   # 80.0  (middle value)
print(np.std(scores))      # 14.14... (how spread out the values are)
print(np.max(scores))      # 100
```

**How they connect:** you store data in an **array**, pick parts with **indexing**, calculate on everything at once with **vectorization**, combine different shapes with **broadcasting**, and summarize the results with **statistics**.

If you'd like, I can turn these into a short quiz or a mini practice exercise using sales-style data.

## 15. Next Lesson

**Lesson 04 — Pandas Introduction, Series and DataFrames**

Topics include installing Pandas, creating Series and DataFrames, understanding indexes and columns, inspecting tabular data, and comparing Pandas with NumPy.
