# Module 05 – Generator Expressions

## Module Overview

In the previous module, you learned how to create generators using the `yield` keyword. Python provides an even shorter and cleaner way to create generators called **Generator Expressions**.

A generator expression looks very similar to a list comprehension but does **not** create all values immediately. Instead, it generates values one at a time, making it more memory efficient for large datasets.

This module explains generator expressions, compares them with list comprehensions, and helps you understand when to use each approach.

---

# Why This Module Is Important

Suppose you want the squares of numbers from **1 to 1,000,000**.

Using a list comprehension:

```python
squares = [x * x for x in range(1, 1000001)]
```

Python creates a list containing one million values.

Using a generator expression:

```python
squares = (x * x for x in range(1, 1000001))
```

Python creates only a generator object. Each square is calculated only when requested.

This approach is used in production applications to reduce memory usage and improve scalability.

---

# Learning Objectives

After completing this module, you will be able to:

* Understand generator expressions.
* Differentiate generator expressions from list comprehensions.
* Explain memory efficiency.
* Choose the appropriate approach for different scenarios.

---

# Topics Covered

## 1. What is a Generator Expression?

A generator expression is a compact way to create a generator.

Syntax:

```python
(expression for item in iterable)
```

Example:

```python
numbers = (x for x in range(1, 6))

for number in numbers:
    print(number)
```

Output:

```text
1
2
3
4
5
```

Notice the use of **parentheses `()`** instead of square brackets `[]`.

---

## 2. Generator Expression vs List Comprehension

### List Comprehension

```python
squares = [x * x for x in range(5)]

print(squares)
```

Output:

```text
[0, 1, 4, 9, 16]
```

The entire list is created immediately.

---

### Generator Expression

```python
squares = (x * x for x in range(5))

print(squares)
```

Output:

```text
<generator object ...>
```

The values are produced only when iterated.

To retrieve values:

```python
for square in squares:
    print(square)
```

Output:

```text
0
1
4
9
16
```

---

## 3. Memory Comparison

### List

```python
numbers = [x for x in range(1000000)]
```

Memory:

```text
Stores all 1,000,000 values
```

---

### Generator

```python
numbers = (x for x in range(1000000))
```

Memory:

```text
Stores only the generator object
```

Each value is generated only when needed.

---

## 4. Performance

### Use a List When

* You need random access using indexing.
* You need to iterate over the data multiple times.
* The dataset is relatively small.

Example:

```python
numbers = [10, 20, 30]

print(numbers[1])
```

Output:

```text
20
```

---

### Use a Generator When

* Processing large datasets.
* Streaming data.
* Reading files.
* Working with APIs.
* Processing database records.
* Handling AI datasets.

---

## 5. Generator Exhaustion

Generator expressions behave like all generators.

Example:

```python
numbers = (x for x in range(3))

for number in numbers:
    print(number)

for number in numbers:
    print(number)
```

The second loop prints nothing because the generator has already been exhausted.

---

# Best Practices

* Use list comprehensions for small datasets.
* Use generator expressions for large datasets.
* Remember that generators can only be consumed once.
* Prefer readability over unnecessary optimization.

---

# Common Mistakes

## Mistake 1

Using parentheses when you actually need a list.

```python
numbers = (1, 2, 3)
```

This creates a tuple, not a generator.

A generator expression must include a `for` clause:

```python
numbers = (x for x in range(3))
```

---

## Mistake 2

Trying to index a generator.

```python
numbers = (x for x in range(5))

print(numbers[0])
```

Output:

```text
TypeError: 'generator' object is not subscriptable
```

Generators do not support indexing.

---

## Mistake 3

Expecting a generator to restart automatically after iteration.

Once exhausted, a generator must be recreated.

---

# Real-World Examples

### AI

Generating training batches on demand.

### FastAPI

Streaming API responses.

### Magento

Generating export records one at a time.

### Log Processing

Reading and processing log files efficiently.

---

# Interview Questions & Answers

### 1. What is a generator expression?

**Interview Answer**

A generator expression is a concise way to create a generator. It uses parentheses and generates values lazily instead of storing them all in memory.

---

### 2. What is the difference between a list comprehension and a generator expression?

**Interview Answer**

A list comprehension creates and stores all values immediately, while a generator expression produces values only when requested, making it more memory efficient.

---

### 3. Why are generator expressions memory efficient?

**Interview Answer**

They generate one value at a time instead of storing the complete dataset in memory.

---

### 4. Can you access a generator using an index?

**Interview Answer**

No. Generators do not support indexing because they produce values sequentially.

---

### 5. When should you use a generator expression?

**Interview Answer**

Use generator expressions when processing large datasets, streaming data, reading files, or whenever storing all values in memory is unnecessary.

---

# Where You'll Use This Later

* FastAPI response streaming.
* LangChain document processing.
* OpenAI streaming responses.
* Data engineering pipelines.
* Magento bulk export/import.
* Processing large CSV or log files.

---

# Key Takeaways

* Generator expressions use parentheses `()`.
* They generate values lazily.
* They consume much less memory than lists.
* They are exhausted after one complete iteration.
* Use them for large datasets and streaming operations.

---

# Module Summary

Generator expressions provide the shortest and most efficient way to create generators in Python. They offer the same memory advantages as generator functions while requiring minimal code. Understanding when to use a list comprehension versus a generator expression is an important skill for writing efficient and scalable Python applications.

---

# Exercises

## Exercise 01

Create:

```text
exercises/exercise-08.py
```

Create a generator expression that generates the **square of numbers from 1 to 10**.

Display all values using a `for` loop.

---

## Exercise 02

Create:

```text
exercises/exercise-09.py
```

Create:

```python
products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Headphones",
    "Keyboard"
]
```

Using a **generator expression**, generate only the products whose names contain **more than six characters**.

Print the results using a `for` loop.

---

## Exercise 03 (Challenge)

Without creating a list, use a **generator expression** to generate all numbers between **1 and 100** that are divisible by both **3 and 5**.

Print the results using a `for` loop.
