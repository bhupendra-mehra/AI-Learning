# Module 04 – Generators & `yield`

## Module Overview

In the previous module, you learned how to create custom iterators by implementing the Iterator Protocol using `__iter__()` and `__next__()`. While this approach is powerful, it requires writing a considerable amount of boilerplate code.

Python provides a much simpler and more elegant solution called **Generators**. A generator automatically behaves like an iterator and manages the iterator state internally. Instead of implementing `__iter__()` and `__next__()`, you simply use the `yield` keyword.

Generators are widely used in production applications because they are memory-efficient, easy to read, and ideal for processing large datasets or streaming data.

---

# Why This Module Is Important

Imagine you need to generate numbers from **1 to 1,000,000**.

### Traditional Approach

```python
numbers = []

for i in range(1, 1000001):
    numbers.append(i)
```

This creates a list containing one million numbers and stores them in memory.

### Generator Approach

```python
def numbers():
    for i in range(1, 1000001):
        yield i
```

The numbers are generated **only when needed**, using almost constant memory.

This is why generators are preferred in:

* AI and Machine Learning
* FastAPI Streaming Responses
* Django QuerySets
* Large File Processing
* Database Cursors
* Data Pipelines
* Web Scraping

---

# Learning Objectives

After completing this module, you will be able to:

* Define a generator.
* Explain the purpose of the `yield` keyword.
* Differentiate between `return` and `yield`.
* Create generator functions.
* Understand generator state.
* Explain why generators are memory efficient.
* Use generators with `for` loops and `next()`.

---

# Topics Covered

## 1. What is a Generator?

A **generator** is a special type of function that produces values **one at a time** instead of returning them all at once.

A normal function finishes execution after reaching `return`.

A generator pauses execution at `yield` and resumes from the same point the next time a value is requested.

---

## 2. Generator Function

A function becomes a generator when it contains the `yield` keyword.

Example:

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Create the generator:

```python
generator = numbers()
```

Notice that nothing is printed yet because the function hasn't executed.

Retrieve values:

```python
print(next(generator))
print(next(generator))
print(next(generator))
```

Output:

```text
1
2
3
```

A fourth call:

```python
print(next(generator))
```

raises:

```text
StopIteration
```

Exactly like a custom iterator.

---

## 3. `return` vs `yield`

### Using `return`

```python
def greet():
    return "Hello"
```

Execution ends immediately after `return`.

---

### Using `yield`

```python
def greet():
    yield "Hello"
    yield "Welcome"
```

Execution pauses after the first `yield`.

Each call to `next()` resumes execution from where it stopped.

---

## 4. Generator State

Consider:

```python
def counter():
    print("Start")
    yield 1

    print("Middle")
    yield 2

    print("End")
    yield 3
```

Create the generator:

```python
gen = counter()
```

Nothing happens yet.

First call:

```python
print(next(gen))
```

Output:

```text
Start
1
```

Second call:

```python
print(next(gen))
```

Output:

```text
Middle
2
```

Third call:

```python
print(next(gen))
```

Output:

```text
End
3
```

The generator remembers exactly where execution stopped.

---

## 5. Generator with Loops

Generators are commonly used with loops.

```python
def even_numbers(limit):

    for i in range(2, limit + 1, 2):
        yield i
```

Use:

```python
for number in even_numbers(10):
    print(number)
```

Output:

```text
2
4
6
8
10
```

Python automatically handles the generator until it is exhausted.

---

## 6. Generator vs Custom Iterator

### Custom Iterator

```python
class NumberIterator:

    def __iter__(self):
        return self

    def __next__(self):
        ...
```

Requires:

* Class
* `__iter__()`
* `__next__()`
* State Management
* `StopIteration`

---

### Generator

```python
def numbers():

    yield 1
    yield 2
    yield 3
```

Requires only:

* Function
* `yield`

Python automatically creates the iterator.

---

## 7. Memory Efficiency

### List

```python
numbers = [i for i in range(1000000)]
```

Stores one million numbers in memory.

---

### Generator

```python
numbers = (i for i in range(1000000))
```

Produces one number at a time.

Memory usage remains almost constant regardless of the sequence size.

---

## Best Practices

* Use generators for large datasets.
* Prefer generators when processing files.
* Use generators for streaming APIs.
* Use `yield` instead of manually implementing iterators whenever possible.
* Keep generator functions focused on a single responsibility.

---

## Common Mistakes

### Using `return` instead of `yield`

Incorrect:

```python
def numbers():
    return 1
    return 2
```

Only the first `return` is ever reached.

---

### Expecting a Generator to Execute Immediately

```python
gen = numbers()
```

No code runs until `next()` or a `for` loop requests a value.

---

### Reusing an Exhausted Generator

```python
gen = numbers()

for i in gen:
    print(i)

for i in gen:
    print(i)
```

The second loop produces no output because the generator has already been exhausted.

---

## Real-World Examples

### AI

Training data is generated batch by batch instead of loading the complete dataset.

### FastAPI

Streaming responses are generated one chunk at a time.

### File Processing

Large files are processed line by line using generators.

### Magento

Generating CSV exports without loading every product into memory.

### OpenAI

Streaming token responses from the API.

---

# Interview Questions & Answers

### 1. What is a generator?

**Interview Answer**

A generator is a special function that produces values one at a time using the `yield` keyword. It automatically implements the Iterator Protocol and is memory efficient.

---

### 2. What is the difference between `return` and `yield`?

**Interview Answer**

`return` ends the function and returns a single value. `yield` pauses the function, returns a value, and resumes execution from the same point when the next value is requested.

---

### 3. Why are generators memory efficient?

**Interview Answer**

Generators produce values only when requested instead of storing the entire dataset in memory. This makes them ideal for processing large files, database records, and AI datasets.

---

### 4. Does a generator implement the Iterator Protocol?

**Interview Answer**

Yes. Python automatically creates an iterator for generator functions, so you don't need to manually implement `__iter__()` or `__next__()`.

---

### 5. Can a generator be used in a `for` loop?

**Interview Answer**

Yes. A generator behaves like an iterator and works naturally with `for` loops, which automatically retrieve values until `StopIteration` is raised.

---

### 6. When should you use a generator instead of a list?

**Interview Answer**

Use a generator when working with large datasets, streaming data, or values that don't need to be stored in memory simultaneously.

---

# Where You'll Use This Later

* **FastAPI** – Streaming API responses.
* **LangChain** – Streaming LLM outputs.
* **OpenAI SDK** – Token-by-token response streaming.
* **Pandas** – Processing large datasets.
* **Magento** – Memory-efficient import/export processes.
* **AI Pipelines** – Batch processing and data streaming.

---

# Key Takeaways

* A generator is a simplified iterator.
* `yield` pauses execution and preserves state.
* Generators automatically implement the Iterator Protocol.
* They use significantly less memory than lists for large datasets.
* Generators are ideal for streaming and sequential processing.

---

# Module Summary

Generators are Python's preferred way of creating iterators. They eliminate the need to manually implement `__iter__()`, `__next__()`, state management, and `StopIteration`. By using the `yield` keyword, you can create clean, readable, and memory-efficient code that is widely used in backend development, AI frameworks, and production applications.

---

# Exercises

## Exercise 01

Create:

```text
exercises/exercise-05.py
```

Create a generator function named `odd_numbers(limit)` that generates all odd numbers from `1` to `limit`.

Example:

```python
for number in odd_numbers(10):
    print(number)
```

Output:

```text
1
3
5
7
9
```

---

## Exercise 02

Create:

```text
exercises/exercise-06.py
```

Create a generator function named `product_generator(products)` that yields one product at a time from the following list:

```python
products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Headphones",
    "Keyboard"
]
```

Use a `for` loop to display all products.

---

## Exercise 03 (Challenge)

Without using `range()`, create a generator that produces the first **10 Fibonacci numbers** using `yield`.
