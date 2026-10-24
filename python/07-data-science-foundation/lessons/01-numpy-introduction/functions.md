### A. Functions used in Lesson 01

| Function or property | Actual use                                          |
| -------------------- | --------------------------------------------------- |
| `np.array()`         | Converts a list or tuple into a NumPy array.        |
| `np.zeros()`         | Creates an array initialized with zeros.            |
| `np.ones()`          | Creates an array initialized with ones.             |
| `np.arange()`        | Creates a numerical sequence using a step size.     |
| `np.linspace()`      | Creates a specified number of evenly spaced values. |
| `np.sum()`           | Calculates the sum of array values.                 |
| `np.mean()`          | Calculates the arithmetic mean.                     |
| `np.min()`           | Returns the smallest value.                         |
| `np.max()`           | Returns the largest value.                          |
| `.ndim`              | Returns the number of dimensions.                   |
| `.shape`             | Returns the dimensions along each axis.             |
| `.size`              | Returns the number of elements.                     |
| `.dtype`             | Shows the array's element data type.                |

### B. Array creation functions

| Function          | Actual use                                                                                   |
| ----------------- | -------------------------------------------------------------------------------------------- |
| `np.empty()`      | Allocates an array without initializing its values; contents must not be assumed to be zero. |
| `np.full()`       | Creates an array filled with a specified value.                                              |
| `np.zeros_like()` | Creates a zero-filled array with the same shape as another array.                            |
| `np.ones_like()`  | Creates an array of ones matching another array's shape.                                     |
| `np.full_like()`  | Creates an array matching another array's shape, filled with a chosen value.                 |
| `np.eye()`        | Creates a 2D array with ones on a selected diagonal and zeros elsewhere.                     |
| `np.identity()`   | Creates a square identity matrix.                                                            |
| `np.logspace()`   | Creates values evenly spaced on a logarithmic scale.                                         |
| `np.geomspace()`  | Creates values evenly spaced geometrically.                                                  |
| `np.asarray()`    | Converts array-like input to an array, avoiding a copy when possible.                        |

Example:

```
import numpy as npprint(np.full(4, 7))print(np.zeros_like([10, 20, 30]))print(np.eye(3))
```

### C. Array manipulation functions

| Function           | Actual use                                                    |
| ------------------ | ------------------------------------------------------------- |
| `np.reshape()`     | Changes array shape without changing its data, when possible. |
| `np.transpose()`   | Reorders array axes.                                          |
| `np.swapaxes()`    | Swaps two specified axes.                                     |
| `np.ravel()`       | Returns a flattened 1D view when possible.                    |
| `np.squeeze()`     | Removes axes whose length is one.                             |
| `np.expand_dims()` | Adds a new axis at a specified position.                      |
| `np.concatenate()` | Joins arrays along an existing axis.                          |
| `np.stack()`       | Joins arrays along a new axis.                                |
| `np.vstack()`      | Stacks arrays vertically.                                     |
| `np.hstack()`      | Stacks arrays horizontally.                                   |
| `np.split()`       | Splits an array into multiple subarrays.                      |
| `np.repeat()`      | Repeats individual elements.                                  |
| `np.tile()`        | Repeats an array pattern.                                     |
| `np.flip()`        | Reverses the order of elements along selected axes.           |
| `np.roll()`        | Shifts elements, wrapping values around the ends.             |
| `np.copy()`        | Creates a separate copy of an array.                          |

Example:

```
values = np.array([1, 2, 3, 4, 5, 6])matrix = np.reshape(values, (2, 3))print(matrix)print(np.ravel(matrix))
```

### D. Indexing, filtering and searching

| Function or syntax   | Actual use                                                        |
| -------------------- | ----------------------------------------------------------------- |
| `array[index]`       | Accesses an element by position.                                  |
| `array[start:stop]`  | Selects a slice of elements.                                      |
| `array[row, column]` | Accesses an element in a multidimensional array.                  |
| Boolean indexing     | Selects elements based on a condition.                            |
| `np.where()`         | Returns matching indices or chooses values based on a condition.  |
| `np.nonzero()`       | Returns indices of nonzero elements.                              |
| `np.argmax()`        | Returns the index of the maximum value.                           |
| `np.argmin()`        | Returns the index of the minimum value.                           |
| `np.argsort()`       | Returns indices that would sort the array.                        |
| `np.sort()`          | Returns sorted values.                                            |
| `np.unique()`        | Returns unique values, optionally with counts or inverse indices. |
| `np.count_nonzero()` | Counts elements that are nonzero or satisfy a condition.          |
| `np.clip()`          | Restricts values to a specified minimum and maximum.              |

Example:

```
sales = np.array([500, 1200, 800, 2000, 1200])print(sales[sales > 1000])print(np.where(sales > 1000))print(np.argmax(sales))print(np.unique(sales))
```

### E. Mathematical functions

| Function        | Actual use                                             |
| --------------- | ------------------------------------------------------ |
| `np.add()`      | Adds values element by element.                        |
| `np.subtract()` | Subtracts values element by element.                   |
| `np.multiply()` | Multiplies values element by element.                  |
| `np.divide()`   | Divides values element by element.                     |
| `np.power()`    | Raises values to specified powers.                     |
| `np.sqrt()`     | Calculates square roots.                               |
| `np.abs()`      | Returns absolute values.                               |
| `np.round()`    | Rounds values to a specified number of decimal places. |
| `np.floor()`    | Rounds values down to the nearest integer.             |
| `np.ceil()`     | Rounds values up to the nearest integer.               |
| `np.exp()`      | Calculates the exponential function.                   |
| `np.log()`      | Calculates the natural logarithm.                      |
| `np.log10()`    | Calculates the base-10 logarithm.                      |
| `np.sin()`      | Calculates sine values in radians.                     |
| `np.cos()`      | Calculates cosine values in radians.                   |
| `np.maximum()`  | Selects the greater value element by element.          |
| `np.minimum()`  | Selects the smaller value element by element.          |
| `np.diff()`     | Calculates differences between adjacent elements.      |
| `np.cumsum()`   | Calculates cumulative sums.                            |
| `np.cumprod()`  | Calculates cumulative products.                        |

Example:

```
prices = np.array([100, 200, 300])print(np.multiply(prices, 1.10))print(np.round(np.sqrt(prices), 2))print(np.cumsum(prices))
```

### F. Statistics functions

| Function                      | Actual use                                        |
| ----------------------------- | ------------------------------------------------- |
| `np.sum()`                    | Total of values.                                  |
| `np.mean()`                   | Arithmetic average.                               |
| `np.median()`                 | Middle value after sorting.                       |
| `np.std()`                    | Standard deviation, measuring spread.             |
| `np.var()`                    | Variance of values.                               |
| `np.min()` / `np.max()`       | Smallest and largest values.                      |
| `np.percentile()`             | Calculates a percentile using a specified method. |
| `np.quantile()`               | Calculates a quantile between zero and one.       |
| `np.average()`                | Calculates a weighted or unweighted average.      |
| `np.argmin()` / `np.argmax()` | Positions of minimum and maximum values.          |
| `np.corrcoef()`               | Calculates a correlation coefficient matrix.      |
| `np.cov()`                    | Calculates covariance between variables.          |
| `np.histogram()`              | Counts observations in numerical bins.            |
| `np.bincount()`               | Counts occurrences of nonnegative integer values. |

Example:

```
sales = np.array([100, 120, 150, 180, 250])print("Mean:", np.mean(sales))print("Median:", np.median(sales))print("Standard deviation:", np.std(sales))print("75th percentile:", np.percentile(sales, 75))
```

### G. Logic and comparison functions

| Function           | Actual use                                                        |
| ------------------ | ----------------------------------------------------------------- |
| `np.any()`         | Checks whether at least one element satisfies a condition.        |
| `np.all()`         | Checks whether all elements satisfy a condition.                  |
| `np.isin()`        | Checks membership in a collection of values.                      |
| `np.isnan()`       | Identifies `NaN` values.                                          |
| `np.isfinite()`    | Identifies finite values, excluding infinities and `NaN`.         |
| `np.isinf()`       | Identifies positive or negative infinity.                         |
| `np.logical_and()` | Performs element-wise logical AND.                                |
| `np.logical_or()`  | Performs element-wise logical OR.                                 |
| `np.logical_not()` | Performs element-wise logical NOT.                                |
| `np.array_equal()` | Checks whether two arrays have the same shape and equal elements. |

Example:

```
prices = np.array([100, 250, 500, 1200])print(np.any(prices > 1000))print(np.all(prices > 0))print(np.where(prices >= 500, "Expensive", "Affordable"))
```

### H. Data types and conversion

| Function or property        | Actual use                                           |
| --------------------------- | ---------------------------------------------------- |
| `np.int32` / `np.int64`     | Integer data types of different widths.              |
| `np.float32` / `np.float64` | Floating-point data types of different precision.    |
| `np.bool_`                  | NumPy Boolean type.                                  |
| `np.dtype()`                | Describes or constructs a data type.                 |
| `array.astype()`            | Converts array values to another data type.          |
| `np.result_type()`          | Determines the resulting data type from input types. |
| `array.tolist()`            | Converts an array into nested Python lists.          |

Example:

```
prices = np.array([100.5, 200.8, 300.2])integer_prices = prices.astype(np.int64)print(integer_prices)print(integer_prices.tolist())
```

Note: converting floating-point values to integers truncates the fractional parts; it does not automatically round them.

### I. Random number functions

Use these when generating sample data or performing simulations.

| Function                  | Actual use                                                              |
| ------------------------- | ----------------------------------------------------------------------- |
| `np.random.default_rng()` | Creates a random number generator; the recommended modern interface.    |
| `rng.integers()`          | Generates random integers.                                              |
| `rng.random()`            | Generates random floating-point values from a uniform distribution.     |
| `rng.choice()`            | Randomly selects from a collection.                                     |
| `rng.normal()`            | Generates values from a normal distribution.                            |
| `rng.uniform()`           | Generates values from a uniform distribution over a specified interval. |
| `rng.permutation()`       | Returns a randomly permuted sequence.                                   |
| `rng.shuffle()`           | Shuffles an array in place.                                             |

Example:

```
rng = np.random.default_rng(42)print(rng.integers(1, 101, size=5))print(rng.choice([100, 200, 300], size=3))
```

A fixed seed such as `42` makes results reproducible for the same generator and call sequence.

### J. Linear algebra functions

These become more useful in later machine learning lessons.

| Function            | Actual use                                                       |
| ------------------- | ---------------------------------------------------------------- |
| `np.dot()`          | Computes dot products; its behavior depends on input dimensions. |
| `np.matmul()`       | Performs matrix multiplication.                                  |
| `np.linalg.solve()` | Solves a system of linear equations.                             |
| `np.linalg.inv()`   | Calculates a matrix inverse when it exists.                      |
| `np.linalg.det()`   | Calculates a matrix determinant.                                 |
| `np.linalg.norm()`  | Calculates vector or matrix norms.                               |
| `np.linalg.eig()`   | Computes eigenvalues and eigenvectors.                           |
| `np.linalg.svd()`   | Performs singular value decomposition.                           |

Example:

```
a = np.array([[1, 2], [3, 4]])b = np.array([[5, 6], [7, 8]])print(np.matmul(a, b))
```

### K. Input and output functions

| Function          | Actual use                                           |
| ----------------- | ---------------------------------------------------- |
| `np.loadtxt()`    | Loads numerical data from text files.                |
| `np.genfromtxt()` | Loads text data and supports missing-value handling. |
| `np.savetxt()`    | Saves arrays to text files.                          |
| `np.save()`       | Saves an array in NumPy's binary `.npy` format.      |
| `np.load()`       | Loads `.npy` arrays or `.npz` archives.              |
| `np.savez()`      | Saves multiple arrays in an `.npz` archive.          |

Example:

```
values = np.array([100, 200, 300])np.save("sales.npy", values)loaded_values = np.load("sales.npy")print(loaded_values)
```

For the upcoming sales project, Pandas will usually be the more convenient library for reading and writing CSV datasets.

## 3. Recommended official reference

The list above is a practical reference, not an exhaustive list of every NumPy API. For the full function catalog, use the official documentation:

- [NumPy — Routines by topic](https://numpy.org/doc/stable/reference/routines.html?utm_source=chatgpt.com)
- [NumPy — Quickstart tutorial](https://numpy.org/doc/stable/user/quickstart.html?utm_source=chatgpt.com)
- [NumPy — Array object reference](https://numpy.org/doc/stable/reference/arrays.ndarray.html?utm_source=chatgpt.com)

## 4. What to focus on now

Don't try to memorize every function before moving forward.

For Lesson 01, prioritize:

`array`, `zeros`, `ones`, `arange`, `linspace`, `sum`, `mean`, `min`, `max`, and the properties `ndim`, `shape`, `size`, and `dtype`.

You'll learn indexing and slicing in Lesson 02, then more advanced array operations and statistics in Lesson 03. The other functions in this reference are there for future use as you work through the roadmap.