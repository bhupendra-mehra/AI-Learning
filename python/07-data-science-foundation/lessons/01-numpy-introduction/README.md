# Lesson 01 — NumPy Introduction and Arrays

## 1. Learning Objectives

By completing this lesson, I will be able to:

- Understand what NumPy is and why it is used in data science.
- Understand the difference between Python lists and NumPy arrays.
- Create one-dimensional and multidimensional arrays.
- Inspect array dimensions, shapes, sizes, and data types.
- Create arrays containing zeros, ones, sequences, and evenly spaced values.
- Perform basic mathematical operations on arrays.
- Calculate totals, averages, minimums, and maximums.
- Use NumPy for practical sales data calculations.

## 2. Prerequisites

- Python variables, lists, and loops.
- Python functions and basic mathematical operations.
- A Python virtual environment.
- Basic Git and GitHub knowledge.

## 3. What Is NumPy?

NumPy stands for Numerical Python. It is a Python library designed for numerical computing and efficient operations on arrays.

Its primary data structure is the `ndarray`, which represents an array with one or more dimensions.

NumPy is useful for:

- Numerical calculations.
- Data analysis and statistics.
- Scientific computing.
- Preparing data for machine learning.
- Processing large collections of numerical values.

### Example

A sales dataset might contain:

```python
sales = [100, 200, 300, 400]
```

Using NumPy:

```python
import numpy as np

sales = np.array([100, 200, 300, 400])

print(sales)
```

Output:

```text
[100 200 300 400]
```

## 4. Installation and Setup

Navigate to the Part 7 directory:

```bash
cd python/07-data-science-foundation
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

If the environment does not exist:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install NumPy:

```bash
python -m pip install numpy
```

Verify the installation:

```bash
python -c "import numpy as np; print(np.__version__)"
```

## 5. Python Lists vs NumPy Arrays

### Python list

```python
sales = [100, 200, 300, 400]

updated_sales = []

for amount in sales:
    updated_sales.append(amount * 1.10)

print(updated_sales)
```

Output:

```text
[110.0, 220.00000000000003, 330.0, 440.00000000000006]
```

### NumPy array

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

NumPy performs the multiplication element by element without requiring an explicit Python loop.

This is called vectorized computation. It can be more efficient for large numerical datasets.

## 6. Creating NumPy Arrays

### 6.1 Create an array using `np.array()`

```python
import numpy as np

sales = np.array([100, 200, 300, 400])

print(sales)
```

### 6.2 One-dimensional array

```python
sales = np.array([100, 200, 300])
print(sales.ndim)
```

Output:

```text
1
```

A one-dimensional array has one axis.

### 6.3 Two-dimensional array

```python
monthly_sales = np.array([
    [100, 200, 300],
    [400, 500, 600],
])

print(monthly_sales)
print(monthly_sales.ndim)
```

Output:

```text
[[100 200 300]
 [400 500 600]]
2
```

A two-dimensional array has rows and columns.

## 7. Understanding Array Properties

```python
import numpy as np

sales = np.array([
    [100, 200, 300],
    [400, 500, 600],
])

print("Dimensions:", sales.ndim)
print("Shape:", sales.shape)
print("Total elements:", sales.size)
print("Data type:", sales.dtype)
```

Expected output:

```text
Dimensions: 2
Shape: (2, 3)
Total elements: 6
Data type: int64
```

The precise integer data type can vary by platform and NumPy configuration.

| Property | Meaning |
|---|---|
| `ndim` | Number of dimensions or axes |
| `shape` | Number of elements along each axis |
| `size` | Total number of elements |
| `dtype` | Data type used for array elements |

## 8. Useful Array Creation Functions

### `np.zeros()`

Creates an array filled with zeros.

```python
print(np.zeros(5))
```

### `np.ones()`

Creates an array filled with ones.

```python
print(np.ones(4))
```

### `np.arange()`

Creates a sequence using a start, stop, and optional step. The stop value is excluded.

```python
print(np.arange(1, 11))
print(np.arange(0, 10, 2))
```

Output:

```text
[ 1  2  3  4  5  6  7  8  9 10]
[0 2 4 6 8]
```

### `np.linspace()`

Creates a specified number of evenly spaced values between two endpoints.

```python
print(np.linspace(0, 100, 5))
```

Output:

```text
[  0.  25.  50.  75. 100.]
```

## 9. Basic Mathematical Operations

```python
import numpy as np

sales = np.array([1200, 1500, 900, 1800, 2100])

print("Increased by 15%:", sales * 1.15)
print("Reduced by 10%:", sales * 0.90)
print("Sales plus 500:", sales + 500)
print("Difference from 1000:", sales - 1000)
```

These operations apply to every element in the array.

## 10. Basic Statistics

```python
import numpy as np

sales = np.array([1200, 1500, 900, 1800, 2100])

print("Total:", np.sum(sales))
print("Average:", np.mean(sales))
print("Minimum:", np.min(sales))
print("Maximum:", np.max(sales))
```

Expected output:

```text
Total: 7500
Average: 1500.0
Minimum: 900
Maximum: 2100
```

These calculations are useful for summarizing sales, prices, quantities, and other numerical datasets.

## 11. Complete Practical Exercise

Create the file:

`lessons/01-numpy-introduction/lesson01_numpy.py`

```python
import numpy as np

sales = np.array([1200, 1500, 900, 1800, 2100])

print("Sales:", sales)
print("Number of values:", sales.size)
print("Shape:", sales.shape)
print("Dimensions:", sales.ndim)
print("Data type:", sales.dtype)

print("Total sales:", np.sum(sales))
print("Average sales:", np.mean(sales))
print("Minimum sales:", np.min(sales))
print("Maximum sales:", np.max(sales))

updated_sales = sales * 1.15

print("Sales after 15% increase:", updated_sales)
```

Run the script:

```bash
python lessons/01-numpy-introduction/lesson01_numpy.py
```

## 12. Homework

Create a separate Python file named `homework.py`.

Given these product prices:

```python
prices = np.array([499, 799, 1299, 1599, 2499])
```

Complete these tasks:

1. Print the number of products.
2. Print the array shape and dimensions.
3. Calculate the total price.
4. Calculate the average price.
5. Find the cheapest product price.
6. Find the most expensive product price.
7. Apply a 10% discount to every price.
8. Create an array containing ten zeros.
9. Create a sequence of even numbers from 2 through 20.
10. Create five evenly spaced values between 10 and 50.

Import NumPy before running the homework.

## 13. Common Mistakes

### NumPy is not installed

Error:

```text
ModuleNotFoundError: No module named 'numpy'
```

Solution:

```bash
python -m pip install numpy
```

Make sure the correct virtual environment is active.

### Incorrect array creation

Incorrect:

```python
np.array(100, 200, 300)
```

Correct:

```python
np.array([100, 200, 300])
```

### Confusing shape and size

For an array with shape `(2, 3)`:

- `shape` returns `(2, 3)`.
- `size` returns `6`.
- `ndim` returns `2`.

### Incorrect `arange()` stop value

```python
np.arange(1, 11)
```

Produces values from 1 through 10, not 11, because the stop value is excluded.

## 14. Completion Checklist

- [ ] NumPy installed in the Part 7 environment.
- [ ] Understood Python lists vs NumPy arrays.
- [ ] Created one-dimensional and two-dimensional arrays.
- [ ] Understood `ndim`, `shape`, `size`, and `dtype`.
- [ ] Practiced `zeros()`, `ones()`, `arange()`, and `linspace()`.
- [ ] Performed mathematical and statistical operations.
- [ ] Completed the practical exercise.
- [ ] Completed the homework.
- [ ] Committed lesson code and documentation to GitHub.

## 15. Next Lesson

**Lesson 02 — Array Indexing, Slicing and Shapes**

Topics include selecting individual elements, accessing rows and columns, slicing arrays, reshaping arrays, and understanding how array views and copies behave.
