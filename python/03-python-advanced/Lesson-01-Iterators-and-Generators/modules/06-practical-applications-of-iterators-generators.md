# Module 06 – Practical Applications of Iterators & Generators

## Module Overview

So far, you've learned:

* What iterables are.
* How iterators work.
* How to build custom iterators.
* How generators simplify iteration.
* How generator expressions make code concise.

This module brings all these concepts together by applying them to real-world scenarios. Instead of focusing on syntax, you'll learn how generators solve practical problems in backend development, AI, data engineering, and Magento applications.

---

# Why This Module Is Important

Generators are not just interview topics—they are used every day in production systems.

Consider these examples:

* Reading a **5 GB log file**.
* Exporting **500,000 Magento products**.
* Processing **millions of AI training records**.
* Streaming **ChatGPT responses**.
* Fetching paginated API results.

Loading all data into memory would be slow and inefficient. Generators solve this by producing one item at a time.

---

# Learning Objectives

After completing this module, you will be able to:

* Process large files efficiently.
* Build memory-efficient data pipelines.
* Simulate API pagination using generators.
* Process large product datasets.
* Understand why generators are preferred in backend and AI applications.

---

# Topics Covered

## 1. Reading Large Files

### Problem

Many beginners write:

```python
with open("products.txt") as file:
    data = file.readlines()

for line in data:
    print(line)
```

This loads the entire file into memory.

For a very large file, this can consume significant RAM.

---

### Better Solution

```python
with open("products.txt") as file:
    for line in file:
        print(line.strip())
```

The file object is iterable.

Python reads one line at a time.

Memory usage stays almost constant.

---

## 2. Generator Pipeline

Suppose you need only even numbers.

Instead of:

```python
numbers = []

for i in range(1, 1000001):
    if i % 2 == 0:
        numbers.append(i)
```

Use:

```python
def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i

for number in even_numbers(1000000):
    print(number)
```

Numbers are generated only when required.

---

## 3. API Pagination

Imagine an API returns 100 products per request.

Instead of loading every page at once, a generator can stream the pages.

```python
def api_pages():

    for page in range(1, 6):

        yield f"Fetching Page {page}"
```

Usage:

```python
for page in api_pages():
    print(page)
```

Output:

```text
Fetching Page 1
Fetching Page 2
Fetching Page 3
Fetching Page 4
Fetching Page 5
```

A real API would yield actual response data instead of strings.

---

## 4. Magento Product Export

Suppose a Magento store contains:

* 1,000,000 products

Avoid:

```python
products = load_all_products()
```

Prefer:

```python
def product_export(products):

    for product in products:
        yield product
```

Then:

```python
for product in product_export(products):
    write_to_csv(product)
```

This is similar to how large export processes are designed.

---

## 5. AI Dataset Processing

Training datasets may contain millions of records.

Instead of:

```python
dataset = load_entire_dataset()
```

AI frameworks process one batch at a time.

Example:

```python
def training_data():

    for i in range(1, 11):
        yield f"Batch {i}"
```

Output:

```text
Batch 1
Batch 2
...
Batch 10
```

This allows models to train without loading the entire dataset into memory.

---

## 6. Chaining Generators

Generators can work together.

Example:

```python
def numbers():

    for i in range(1, 11):
        yield i


def even_numbers(data):

    for number in data:

        if number % 2 == 0:
            yield number


def square_numbers(data):

    for number in data:
        yield number ** 2


result = square_numbers(
            even_numbers(
                numbers()
            )
         )

for value in result:
    print(value)
```

Output:

```text
4
16
36
64
100
```

This creates a simple processing pipeline.

---

# Best Practices

* Process data lazily whenever possible.
* Use generators for streaming large datasets.
* Read files line by line.
* Prefer generators for ETL and data processing pipelines.
* Combine generators to create reusable workflows.

---

# Common Mistakes

### Loading Everything Into Memory

```python
data = file.readlines()
```

Avoid for large files.

---

### Converting a Generator to a List Without Need

```python
list(generator)
```

This removes the memory advantage.

---

### Using a Generator Multiple Times

Generators are exhausted after iteration.

Create a new generator if needed.

---

# Real-World Examples

## Backend Development

Streaming API responses.

---

## AI

Generating batches for model training.

---

## Magento

Product export and import.

---

## Data Engineering

ETL pipelines.

---

## Log Processing

Reading large log files line by line.

---

# Interview Questions & Answers

### 1. Why are generators used in production applications?

**Interview Answer**

Generators process data one item at a time instead of loading everything into memory. This makes applications scalable and memory efficient.

---

### 2. Give some real-world uses of generators.

**Interview Answer**

Large file processing, API pagination, AI dataset processing, Magento exports, ETL pipelines, and streaming API responses.

---

### 3. Why shouldn't large files be read using `readlines()`?

**Interview Answer**

`readlines()` loads the complete file into memory. For very large files, this can consume a significant amount of RAM.

---

### 4. Why are generators useful in AI?

**Interview Answer**

AI models usually process data in batches. Generators provide batches only when required, reducing memory usage.

---

### 5. What is a generator pipeline?

**Interview Answer**

A generator pipeline consists of multiple generators connected together, where the output of one generator becomes the input of the next.

---

# Where You'll Use This Later

## FastAPI

Streaming responses.

---

## LangChain

Streaming LLM output.

---

## OpenAI SDK

Streaming tokens.

---

## Magento

Bulk product exports and imports.

---

## AI Agents

Streaming documents and tool outputs.

---

## Data Engineering

Building ETL pipelines.

---

# Key Takeaways

* Generators solve real production problems.
* They are ideal for large datasets.
* Generator pipelines create efficient workflows.
* Streaming reduces memory consumption.
* Modern backend and AI frameworks rely heavily on generators.

---

# Module Summary

This module demonstrated how iterators and generators are used in real-world software engineering. From processing files and paginated APIs to AI datasets and Magento exports, generators provide a simple yet powerful way to build scalable, memory-efficient applications. Understanding these practical applications prepares you to recognize and use generators confidently in professional Python projects.

---

# Exercises

## Exercise 01

Create:

```text
exercises/exercise-11.py
```

Create a generator named `read_numbers(limit)` that yields numbers from **1** to `limit`.

Create another generator named `square_numbers(data)` that accepts the first generator and yields the square of each number.

Print the results.

Expected output:

```text
1
4
9
16
25
...
```

---

## Exercise 02

Create:

```text
exercises/exercise-12.py
```

Create a list of **20 products**.

Write a generator that yields only products whose names start with the letter **"S"**.

Print the results.

---

## Exercise 03 (Challenge)

Create:

```text
exercises/exercise-13.py
```

Build a **generator pipeline** with three generators:

1. Generate numbers from **1 to 50**.
2. Yield only numbers divisible by **5**.
3. Yield the square of those numbers.

Print the final output.
