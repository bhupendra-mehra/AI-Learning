# Module 07 – Best Practices & Common Mistakes

## Module Overview

In this lesson, you've learned about iterables, iterators, custom iterators, generators, generator expressions, and real-world applications. The final step is understanding **when to use each concept** and the common mistakes developers make.

Professional Python development is not only about writing working code but also about writing code that is efficient, readable, maintainable, and scalable.

This module summarizes best practices and provides practical guidelines that you can apply in real-world projects.

---

# Why This Module Is Important

Choosing the right data processing approach directly affects:

* Memory usage
* Performance
* Code readability
* Maintainability
* Scalability

A common mistake is using generators everywhere or avoiding them completely. A good developer understands **when each approach is appropriate**.

---

# Learning Objectives

After completing this module, you will be able to:

* Decide when to use lists or generators.
* Know when a custom iterator is appropriate.
* Avoid common iterator and generator mistakes.
* Write more Pythonic and efficient code.
* Explain these concepts confidently in interviews.

---

# Topics Covered

## 1. List vs Generator

### Use a List When

* The dataset is small.
* You need random access (`numbers[5]`).
* You need to iterate over the data multiple times.
* You need list-specific methods such as `append()`, `sort()`, or `reverse()`.

Example:

```python
numbers = [x * x for x in range(10)]

print(numbers[5])
```

---

### Use a Generator When

* Processing large datasets.
* Reading large files.
* Streaming API responses.
* Processing database records.
* Building data pipelines.
* Memory efficiency is important.

Example:

```python
numbers = (x * x for x in range(1000000))

for number in numbers:
    print(number)
```

---

## 2. Custom Iterator vs Generator

### Use a Custom Iterator When

* Complex iteration logic is required.
* You need complete control over iteration.
* You are building reusable iterator classes.
* The iterator needs custom behavior or state.

Example:

```python
class ProductIterator:
    ...
```

---

### Use a Generator When

* Sequential values are generated.
* Simplicity and readability are preferred.
* You don't need to manually implement the Iterator Protocol.

Example:

```python
def even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number
```

**Recommendation:** In most real-world Python projects, generators are used far more frequently than custom iterator classes.

---

## 3. Common Mistakes

### Mistake 1 – Loading Everything into Memory

Avoid:

```python
data = file.readlines()
```

Prefer:

```python
for line in file:
    print(line)
```

---

### Mistake 2 – Using a Generator When You Need Random Access

Generators do not support indexing.

Incorrect:

```python
numbers = (x for x in range(10))
print(numbers[3])
```

This raises a `TypeError`.

---

### Mistake 3 – Reusing an Exhausted Generator

```python
numbers = (x for x in range(5))

for number in numbers:
    print(number)

for number in numbers:
    print(number)
```

The second loop produces no output because the generator has already been consumed.

---

### Mistake 4 – Converting Large Generators into Lists

```python
list(generator)
```

This removes the memory-saving benefit of generators.

Only convert a generator into a list if you truly need all values in memory.

---

### Mistake 5 – Using Built-in Names as Variables

Avoid:

```python
list = [1, 2, 3]
str = "Python"
dict = {}
```

These override Python's built-in types.

Prefer descriptive names:

```python
numbers = [1, 2, 3]
language = "Python"
student = {}
```

---

## 4. Performance Tips

* Prefer generators for large datasets.
* Process files line by line.
* Avoid unnecessary list creation.
* Keep generator functions focused on one responsibility.
* Use generator expressions for simple transformations.
* Use list comprehensions when the entire dataset is genuinely needed.

---

## 5. Memory Optimization

### Less Efficient

```python
numbers = [x for x in range(1000000)]
```

Stores one million values.

---

### More Efficient

```python
numbers = (x for x in range(1000000))
```

Generates one value at a time.

---

## 6. Production Recommendations

In production projects:

* Use generators for file processing.
* Use generators for API pagination.
* Stream database results where possible.
* Avoid reading huge datasets into memory.
* Prefer readable code over clever one-liners.

---

## Real-World Examples

### Magento

* Product export
* Product import
* Inventory synchronization
* Batch order processing

---

### AI & Machine Learning

* Batch training
* Dataset streaming
* Data preprocessing pipelines

---

### FastAPI

* Streaming large responses
* Processing uploaded files

---

### Data Engineering

* ETL pipelines
* Log analysis
* CSV processing

---

# Interview Questions & Answers

### 1. When should you use a generator instead of a list?

**Interview Answer**

Use a generator when processing large datasets or streaming data because it produces values on demand and uses significantly less memory than a list.

---

### 2. When should you use a list instead of a generator?

**Interview Answer**

Use a list when you need random access, multiple iterations over the same data, or list-specific operations such as sorting or indexing.

---

### 3. What is the biggest advantage of generators?

**Interview Answer**

The biggest advantage is memory efficiency. Generators produce values only when requested instead of storing the complete dataset in memory.

---

### 4. Why don't generators support indexing?

**Interview Answer**

Generators produce values sequentially and do not store all elements in memory, so there is no indexable collection.

---

### 5. When would you create a custom iterator?

**Interview Answer**

Create a custom iterator when you need complete control over iteration or when implementing specialized iteration behavior that a generator cannot easily express.

---

### 6. Why are generators widely used in backend development?

**Interview Answer**

Backend applications often process large files, API responses, database records, and streams of data. Generators reduce memory usage while keeping applications scalable and efficient.

---

# Where You'll Use This Later

* FastAPI request and response streaming.
* LangChain document processing.
* OpenAI streaming APIs.
* Magento import/export modules.
* AI model training pipelines.
* Large-scale data processing systems.

---

# Key Takeaways

* Choose the right tool for the problem.
* Lists are best for small, reusable datasets.
* Generators are best for large or streamed datasets.
* Custom iterators are useful but less common than generators.
* Avoid exhausting generators unintentionally.
* Don't sacrifice readability for unnecessary optimization.

---

# Module Summary

This module consolidated the concepts learned throughout the lesson by focusing on practical decision-making rather than new syntax. You now know when to use lists, generators, and custom iterators, how to avoid common mistakes, and how these concepts are applied in professional Python development. These best practices will help you write efficient, maintainable, and production-ready Python code.

---

# Exercises

## Exercise 01

Create:

```text
exercises/exercise-14.py
```

Write a short program that demonstrates **both** a list comprehension and a generator expression that generate the squares of numbers from **1 to 20**.

Print the values and add comments explaining **when you would choose each approach**.

---

## Exercise 02

Create:

```text
exercises/exercise-15.py
```

A file named `products.txt` contains one product name per line.

Write **two** programs:

1. One using `readlines()`.
2. One using direct file iteration (`for line in file:`).

In comments, explain which approach is more suitable for large files and why.

---

## Exercise 03 (Final Challenge)

Create:

```text
exercises/exercise-16.py
```

Write a short note (in comments or a multi-line string) answering:

1. When should you use a **list**?
2. When should you use a **generator**?
3. When should you create a **custom iterator**?

Support each answer with one practical example.
