# Lesson 02 — Array Indexing, Slicing and Shapes

## 1. Learning Objectives

By completing this lesson, I will be able to:

- Access individual elements in NumPy arrays.
- Use positive and negative indexing.
- Extract data using array slicing.
- Select rows and columns from two-dimensional arrays.
- Filter array elements using conditions.
- Understand array shapes and reshape arrays.
- Understand the difference between array views and copies.
- Apply indexing and slicing to practical sales data.

## 2. Prerequisites

- Lesson 01: NumPy Introduction and Arrays.
- Python lists, indexes, and slices.
- Basic understanding of one-dimensional and two-dimensional arrays.
- NumPy installed in the Part 7 virtual environment.

## 3. What Is Array Indexing?

Array indexing means accessing an individual element using its position.

NumPy uses zero-based indexing, which means the first element has index `0`.

```python
import numpy as np

sales = np.array([100, 200, 300, 400, 500])

print(sales[0])
print(sales[2])
print(sales[4])
```

Output:

```text
100
300
500
```

### Important points

- `sales[0]` accesses the first element.
- `sales[2]` accesses the third element.
- `sales[4]` accesses the fifth element.

The index is not the same as the element's position counted from one.

## 4. Negative Indexing

Negative indexing accesses elements from the end of an array.

```python
import numpy as np

sales = np.array([100, 200, 300, 400, 500])

print(sales[-1])
print(sales[-2])
print(sales[-5])
```

Output:

```text
500
400
100
```

| Index | Element |
|---|---:|
| `sales[0]` | 100 |
| `sales[1]` | 200 |
| `sales[-1]` | 500 |
| `sales[-2]` | 400 |

Negative indexing is useful when you need the last few observations in a dataset.

## 5. What Is Array Slicing?

Slicing extracts a range of elements from an array.

Syntax:

```python
array[start:stop:step]
```

- `start`: index where selection begins, inclusive.
- `stop`: index where selection ends, exclusive.
- `step`: interval between selected elements.

### Example 1: Basic slicing

```python
import numpy as np

sales = np.array([100, 200, 300, 400, 500, 600])

print(sales[1:4])
```

Output:

```text
[200 300 400]
```

The slice starts at index `1` and stops before index `4`.

### Example 2: Slice from the beginning

```python
print(sales[:3])
```

Output:

```text
[100 200 300]
```

### Example 3: Slice to the end

```python
print(sales[3:])
```

Output:

```text
[400 500 600]
```

### Example 4: Select every second element

```python
print(sales[::2])
```

Output:

```text
[100 300 500]
```

### Example 5: Reverse an array

```python
print(sales[::-1])
```

Output:

```text
[600 500 400 300 200 100]
```

## 6. Indexing Two-Dimensional Arrays

A two-dimensional array contains rows and columns.

```python
import numpy as np

monthly_sales = np.array([
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900],
])

print(monthly_sales)
```

Output:

```text
[[100 200 300]
 [400 500 600]
 [700 800 900]]
```

### 6.1 Access an individual element

Syntax:

```python
array[row_index, column_index]
```

Example:

```python
print(monthly_sales[0, 0])
print(monthly_sales[1, 2])
print(monthly_sales[2, 1])
```

Output:

```text
100
600
800
```

### 6.2 Access a complete row

```python
print(monthly_sales[0])
print(monthly_sales[1])
```

Output:

```text
[100 200 300]
[400 500 600]
```

### 6.3 Access a complete column

```python
print(monthly_sales[:, 0])
print(monthly_sales[:, 1])
print(monthly_sales[:, 2])
```

Output:

```text
[100 400 700]
[200 500 800]
[300 600 900]
```

The colon `:` means select all elements along that axis.

### 6.4 Select multiple rows and columns

```python
print(monthly_sales[0:2, 1:3])
```

Output:

```text
[[200 300]
 [500 600]]
```

This selects the first two rows and the last two columns.

## 7. Boolean Indexing

Boolean indexing selects values that satisfy a condition.

```python
import numpy as np

sales = np.array([100, 250, 500, 750, 1000])

print(sales > 500)
print(sales[sales > 500])
```

Output:

```text
[False False False  True  True]
[ 750 1000]
```

### Practical example: Filter high sales

```python
sales = np.array([1200, 1500, 900, 1800, 2100])

high_sales = sales[sales >= 1500]

print(high_sales)
```

Output:

```text
[1500 1800 2100]
```

### Combine conditions

Use `&` for AND and `|` for OR. Put each comparison inside parentheses.

```python
sales = np.array([500, 1200, 1500, 1800, 2500])

selected = sales[(sales >= 1200) & (sales <= 1800)]

print(selected)
```

Output:

```text
[1200 1500 1800]
```

## 8. Understanding Array Shapes

The shape of an array tells us the number of elements along each axis.

```python
import numpy as np

sales = np.array([100, 200, 300, 400])

print(sales.shape)
```

Output:

```text
(4,)
```

This is a one-dimensional array containing four elements.

A two-dimensional example:

```python
monthly_sales = np.array([
    [100, 200, 300],
    [400, 500, 600],
])

print(monthly_sales.shape)
```

Output:

```text
(2, 3)
```

This means two rows and three columns.

## 9. Reshaping Arrays

`reshape()` changes the shape of an array without changing the order of its elements.

The new shape must contain the same total number of elements.

### Example 1: Reshape one-dimensional data

```python
import numpy as np

sales = np.array([100, 200, 300, 400, 500, 600])

matrix = sales.reshape(2, 3)

print(matrix)
```

Output:

```text
[[100 200 300]
 [400 500 600]]
```

### Example 2: Reshape into three rows

```python
matrix = sales.reshape(3, 2)

print(matrix)
```

Output:

```text
[[100 200]
 [300 400]
 [500 600]]
```

### Example 3: Let NumPy calculate one dimension

```python
matrix = sales.reshape(2, -1)

print(matrix.shape)
```

Output:

```text
(2, 3)
```

Using `-1` tells NumPy to infer that dimension from the number of elements and the other dimensions.

Only one dimension can be inferred this way.

### Example 4: Flatten an array

```python
matrix = np.array([
    [100, 200, 300],
    [400, 500, 600],
])

print(matrix.flatten())
```

Output:

```text
[100 200 300 400 500 600]
```

`flatten()` returns a one-dimensional copy of the data.

## 10. Views vs Copies

A view shares underlying data with the original array when possible. A copy owns separate data.

### Example 1: Slicing creates a view in this case

```python
import numpy as np

sales = np.array([100, 200, 300, 400])

view = sales[1:3]
view[0] = 999

print(sales)
print(view)
```

Output:

```text
[100 999 300 400]
[999 300]
```

Changing the view also changes the original array.

In NumPy, slicing an array does not create a copy of the data; instead, it creates a view of the original array. This means both variables point to the exact same data in memory.
When you modify the view, the original array changes too.
Here is the exact output of your code:
text
[100, 999, 300, 400]
[999, 300]
Use code with caution.

Step-by-Step Breakdown


Step	Code	What Happens	sales Array	view Array
1	sales = np.array([100, 200, 300, 400])	Creates the original 4-element array.	[100, 200, 300, 400]	Not created yet
2	view = sales[1:3]	Slices index 1 up to (but excluding) 3. view now looks directly at [200, 300] inside sales.	[100, 200, 300, 400]	[200, 300]
3	view[0] = 999	Changes the first element of view. Because it is a view, it alters the shared memory space.	[100, 999, 300, 400]	[999, 300]


How to Prevent This (Making a Copy)

If you want to modify the slice without affecting the original array, you must explicitly use the .copy() method:
python
# This creates a completely independent copy
view = sales[1:3].copy()
view[0] = 999

# sales remains: [100, 200, 300, 400]
# view becomes:  [999, 300]
Use code with caution.
Would you like to explore how this view vs. copy behavior works when dealing with the 2D matrices we looked at earlier, or would you like to try another practice example?


### Example 2: Explicit copy

```python
sales = np.array([100, 200, 300, 400])

copied_sales = sales[1:3].copy()
copied_sales[0] = 999

print(sales)
print(copied_sales)
```

Output:

```text
[100 200 300 400]
[999 300]
```

The original array remains unchanged.

**Important:** Whether an operation creates a view or a copy depends on the operation. Basic slicing usually creates views, while advanced indexing and `flatten()` create copies.

## 11. Useful Functions and Properties

| Function or property | Actual use |
|---|---|
| `array[index]` | Access an individual element |
| `array[start:stop]` | Extract a slice |
| `array[row, column]` | Access an element in a 2D array |
| `array[:, column]` | Select a complete column |
| `array[condition]` | Filter elements using a Boolean condition |
| `np.where()` | Find indices or select values based on a condition |
| `np.reshape()` | Change the shape of an array |
| `array.flatten()` | Create a flattened copy |
| `np.ravel()` | Flatten an array, returning a view when possible |
| `np.expand_dims()` | Add an axis |
| `np.squeeze()` | Remove axes of length one |
| `array.ndim` | Inspect the number of dimensions |
| `array.shape` | Inspect the dimensions along each axis |
| `array.size` | Count all elements |
| `array.copy()` | Create an independent copy |

## 12. Complete Practical Exercise

Create the file:

`lessons/02-numpy-array-operations/lesson02_numpy.py`

```python
import numpy as np

sales = np.array([1200, 1500, 900, 1800, 2100, 2500])

print("First sale:", sales[0])
print("Last sale:", sales[-1])
print("First three sales:", sales[:3])
print("Every second sale:", sales[::2])
print("Reversed sales:", sales[::-1])

print("Sales >= 1500:", sales[sales >= 1500])

monthly_sales = np.array([
    [1200, 1500, 1800],
    [900, 2100, 2500],
])

print("First month:", monthly_sales[0])
print("Second month:", monthly_sales[1])
print("First column:", monthly_sales[:, 0])
print("Shape:", monthly_sales.shape)

values = np.arange(1, 13)
matrix = values.reshape(3, 4)

print("Reshaped array:")
print(matrix)

print("Flattened array:", matrix.flatten())
```

Run the script:

```bash
python lessons/02-numpy-array-operations/lesson02_numpy.py
```

## 13. Homework

Create a file named `homework.py`.

Use this array:

```python
import numpy as np

prices = np.array([499, 799, 1299, 1599, 2499, 999, 1899, 299])
```

Complete these tasks:

1. Print the first and last prices.
2. Print the first four prices.
3. Print the last three prices.
4. Print every second price.
5. Reverse the array.
6. Select prices greater than 1,000.
7. Select prices between 500 and 1,500 inclusive.
8. Reshape the eight prices into two rows and four columns.
9. Print the second row.
10. Print the third column.
11. Flatten the reshaped array.
12. Make a copy, change one copied value, and verify that the original remains unchanged.

## 14. Common Mistakes

### Index out of range

Incorrect:

```python
sales = np.array([100, 200, 300])
print(sales[3])
```

The valid positive indexes are `0`, `1`, and `2`.

### Forgetting that the stop index is excluded

```python
sales[1:4]
```

Selects indexes 1, 2, and 3—not index 4.

### Incorrect reshape dimensions

```python
np.arange(1, 7).reshape(4, 2)
```

This raises a `ValueError` because six elements cannot fill a shape requiring eight elements.

### Using Python's `and` for array comparisons

Incorrect:

```python
sales[(sales >= 500) and (sales <= 1500)]
```

Correct:

```python
sales[(sales >= 500) & (sales <= 1500)]
```

### Accidentally modifying the original array

A basic slice can share data with the original. Use `.copy()` when independent data is required.

## 15. Completion Checklist

- [x] Understood positive and negative indexing.
- [x] Practiced basic slicing and slice steps.
- [x] Accessed rows, columns, and individual elements.
- [x] Filtered arrays using Boolean conditions.
- [x] Inspected array shapes.
- [x] Used `reshape()` and `flatten()`.
- [x] Understood views versus copies.
- [x] Completed the practical exercise.
- [x] Completed the homework.
- [x] Committed the lesson code and documentation to GitHub.

## 16. Next Lesson

**Lesson 03 — Vectorized Operations, Statistics and Broadcasting**

Topics include vectorized arithmetic, broadcasting rules, aggregation along axes, cumulative calculations, and practical numerical analysis.
