## Module 01 – Understanding Iterables

> **Estimated Time:** 25–30 Minutes

---

# Module Overview

Before learning **Iterators** and **Generators**, you first need to understand **Iterables**, because every iterator starts from an iterable.

When you write a `for` loop, Python is actually performing several operations behind the scenes. Understanding those operations will help you understand how generators work later.

This module covers:

* What an Iterable is
* Common Iterable Objects
* Iterable vs Non-Iterable Objects
* How Python's `for` loop works with iterables

By the end of this module, you'll understand why lists, tuples, strings, dictionaries, files, and many other Python objects work naturally with loops.

---

# 1. What is an Iterable?

An **iterable** is any Python object whose elements can be accessed **one at a time** in sequence.

In simple terms:

> If you can loop through an object using a `for` loop, it is an iterable.

Examples:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Output:

```text
10
20
30
```

Python reads one element at a time instead of trying to process everything simultaneously.

---

# Common Iterable Objects

Python provides many built-in iterable objects.

### List

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

---

### Tuple

```python
colors = ("Red", "Green", "Blue")

for color in colors:
    print(color)
```

---

### String

```python
name = "Python"

for ch in name:
    print(ch)
```

Output:

```text
P
y
t
h
o
n
```

Each character is treated as an individual element.

---

### Dictionary

By default, dictionaries iterate over their **keys**.

```python
student = {
    "name": "Bhupendra",
    "age": 37
}

for key in student:
    print(key)
```

Output:

```text
name
age
```

To iterate over values:

```python
for value in student.values():
    print(value)
```

To iterate over key-value pairs:

```python
for key, value in student.items():
    print(key, value)
```

---

### Set

```python
languages = {"Python", "PHP", "Java"}

for language in languages:
    print(language)
```

> **Note:** Sets are unordered, so the output order is not guaranteed.

---

### File Objects

A file is also iterable.

```python
with open("data.txt") as file:
    for line in file:
        print(line.strip())
```

Python reads **one line at a time**, making this very memory-efficient for large files.

---

# Iterable vs Non-Iterable Objects

Not every object is iterable.

### Iterable

```python
[1, 2, 3]
```

```python
"Hello"
```

```python
(1, 2, 3)
```

```python
{"a": 1}
```

```python
{1, 2, 3}
```

---

### Non-Iterable

```python
100
```

```python
3.14
```

```python
True
```

Trying to loop over an integer:

```python
number = 100

for value in number:
    print(value)
```

Results in:

```text
TypeError: 'int' object is not iterable
```

Because an integer is a single value, not a collection.

---

# How `for` Loops Work with Iterables

When you write:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

It appears simple, but internally Python performs something like this:

```text
numbers
    │
    ▼
Create an Iterator
    │
    ▼
Get First Value
    │
    ▼
Execute Loop Body
    │
    ▼
Get Next Value
    │
    ▼
Repeat Until Finished
```

The key point is:

> A `for` loop does **not** directly read a list, tuple, or string. It first converts the iterable into an **iterator**, which you'll study in the next module.

---

# Real-World Examples

### Reading a Large CSV File

```python
with open("products.csv") as file:
    for row in file:
        process(row)
```

The file is processed line by line instead of loading the entire file into memory.

---

### Magento Product Processing

Instead of:

```text
Load 500,000 products

↓

Process
```

A better approach is:

```text
Read Product

↓

Process

↓

Read Next Product

↓

Process
```

This is the principle behind efficient iteration.

---

### AI Dataset Processing

Training datasets can contain millions of records.

Instead of loading everything into RAM, AI frameworks process data incrementally using iterable objects and generators.

---

# Best Practices

* Use `for` loops with iterable objects whenever possible.
* Prefer iterating over files rather than reading the entire file into memory.
* Use `.items()` when both dictionary keys and values are required.
* Don't assume sets preserve insertion order.

---

# Common Mistakes

### Mistake 1

Trying to iterate over a number.

```python
for i in 100:
    pass
```

Incorrect.

---

### Mistake 2

Expecting dictionary iteration to return values.

```python
for item in student:
    print(item)
```

This prints **keys**, not values.

Use:

```python
student.values()
```

or

```python
student.items()
```

---

### Mistake 3

Assuming sets are ordered.

Never rely on a specific iteration order for a set.

---

# Exercises

Create:

```text
exercises/exercise-01.py
```

### Exercise 1

Create:

* A list of five programming languages.
* A tuple of five countries.
* A string containing your name.
* A dictionary containing your personal details.
* A set of your favorite technologies.

Use a `for` loop to iterate over each.

---

### Exercise 2

Create a text file with at least 10 lines and write a program that prints each line using a `for` loop.

---

# Interview Questions

### Q1. What is an iterable?

**Answer:**
An iterable is any object whose elements can be accessed one at a time. Objects such as lists, tuples, strings, dictionaries, sets, and files are common examples of iterables.

---

### Q2. How do you identify an iterable?

**Answer:**
If an object can be used in a `for` loop or passed to the `iter()` function, it is an iterable.

---

### Q3. Is a dictionary iterable?

**Answer:**
Yes. By default, iterating over a dictionary returns its keys. Use `.values()` to iterate over values and `.items()` to iterate over key-value pairs.

---

### Q4. Why is a file considered iterable?

**Answer:**
A file object returns one line at a time during iteration, allowing efficient processing of large files without loading the entire file into memory.

---

# Module Summary

In this module, you learned:

* ✅ What an iterable is.
* ✅ Common iterable types in Python.
* ✅ The difference between iterable and non-iterable objects.
* ✅ How `for` loops use iterables internally.
* ✅ Practical applications in file processing, Magento, and AI.

You now have the foundation needed for the next module, where we'll explore **iterators** themselves—how they're created, how the iterator protocol works, and what happens behind every `for` loop. This is where Python's iteration model becomes even more interesting.
