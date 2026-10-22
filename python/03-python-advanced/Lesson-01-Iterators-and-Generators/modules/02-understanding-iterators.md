# Module 02 – Understanding Iterators

## Module Overview

In Module 01, you learned that a **for loop** works with iterable objects such as lists, tuples, strings, dictionaries, sets, and files.

However, Python does **not** iterate over these objects directly.

Before the loop starts, Python converts an **iterable** into an **iterator**. The iterator is responsible for returning one element at a time until all elements have been processed.

This module explains what an iterator is, how the **Iterator Protocol** works, and how Python uses the built-in `iter()` and `next()` functions internally.

---

# Why This Module Is Important

Every `for` loop in Python uses an iterator behind the scenes.

Understanding iterators helps you:

* Understand how Python loops work internally.
* Debug iteration-related issues.
* Build custom iterators in the next module.
* Understand generators, which are special types of iterators.

Many Python frameworks such as FastAPI, Django, Pandas, and AI libraries rely heavily on iterators for efficient data processing.

---

# Learning Objectives

After completing this module, you will be able to:

* Define an iterator.
* Explain the difference between an iterable and an iterator.
* Convert an iterable into an iterator using `iter()`.
* Retrieve values using `next()`.
* Understand `StopIteration`.
* Explain the Iterator Protocol.
* Understand what Python does internally when executing a `for` loop.

---

# Topics Covered

## 1. What is an Iterator?

An **iterator** is an object that returns **one value at a time** from an iterable.

Unlike an iterable, an iterator remembers its current position.

Think of an iterable as a **book** and an iterator as a **bookmark**.

```text
Book (Iterable)

Page 1
Page 2
Page 3
Page 4

        │

Bookmark (Iterator)

Current Position
```

Every time you ask the bookmark for the next page, it moves forward.

---

## 2. Iterable vs Iterator

| Iterable                            | Iterator                        |
| ----------------------------------- | ------------------------------- |
| Collection of data                  | Object used to traverse data    |
| Can create multiple iterators       | Keeps track of current position |
| Uses `iter()` to create an iterator | Uses `next()` to return values  |
| Examples: list, tuple, string, set  | Returned by `iter()`            |

Example:

```python
numbers = [10, 20, 30]
```

`numbers` is an **iterable**, not an iterator.

To create an iterator:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(iterator)
```

Possible output:

```text
<list_iterator object at 0x...>
```

---

## 3. The `iter()` Function

`iter()` converts an iterable into an iterator.

Syntax:

```python
iterator = iter(iterable)
```

Example:

```python
fruits = ["Apple", "Banana", "Orange"]

fruit_iterator = iter(fruits)
```

Now `fruit_iterator` remembers where it is while traversing the list.

---

## 4. The `next()` Function

`next()` retrieves one value from the iterator.

Example:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
10
20
30
```

Notice that each call moves the iterator forward.

---

## 5. What Happens After the Last Item?

Calling `next()` again:

```python
print(next(iterator))
```

Produces:

```text
StopIteration
```

This exception tells Python that there are no more values.

---

## 6. How `for` Loops Work Internally

When you write:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Python performs something conceptually similar to:

```python
iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break
```

This is why a `for` loop stops automatically—it catches `StopIteration` internally.

---

## 7. Iterator Protocol

An object follows the **Iterator Protocol** if:

1. It implements `__iter__()`.
2. It implements `__next__()`.

Python uses these two methods to retrieve values during iteration.

You'll implement them yourself in the next module.

---

# Best Practices

* Use `for` loops instead of repeatedly calling `next()` unless you specifically need manual control.
* Use `iter()` and `next()` when building custom iteration logic.
* Understand that iterators are **consumed** as you iterate through them.

---

# Common Mistakes

## Mistake 1

Calling `next()` too many times.

```python
iterator = iter([1, 2])

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Results in:

```text
StopIteration
```

---

## Mistake 2

Assuming an iterator resets automatically.

```python
numbers = [1, 2, 3]

iterator = iter(numbers)

for value in iterator:
    print(value)

for value in iterator:
    print(value)
```

The second loop prints nothing because the iterator has already been exhausted.

Create a new iterator if you need to iterate again.

---

# Real-World Examples

### File Processing

```python
with open("products.txt") as file:
    iterator = iter(file)

    print(next(iterator))
    print(next(iterator))
```

The iterator returns one line at a time.

---

### Database Records

Database cursors often return rows sequentially using iterator-like behavior.

---

### AI Dataset Processing

Training data is frequently processed one record or one batch at a time using iterators to reduce memory usage.

---

# Exercises

## Exercise 01

Create a list containing five numbers.

* Convert it into an iterator using `iter()`.
* Retrieve each value using `next()`.
* Observe what happens after the last element.

---

## Exercise 02

Create a tuple containing five fruits.

* Convert it into an iterator.
* Print each value using `next()`.
* Handle the `StopIteration` exception using `try` and `except`.

---

# Interview Questions

### What is an iterator?

### What is the difference between an iterable and an iterator?

### What does `iter()` do?

### What does `next()` do?

### What is `StopIteration`?

### What is the Iterator Protocol?

### How does a `for` loop work internally?

---

# Key Takeaways

* An iterator retrieves one value at a time.
* Every iterator is created from an iterable.
* `iter()` creates an iterator.
* `next()` returns the next value.
* `StopIteration` indicates there are no more values.
* Every `for` loop internally uses `iter()` and `next()`.
* Iterators remember their current position and are consumed as they are traversed.

---

# Module Summary

In this module, you learned how Python converts an iterable into an iterator, how values are retrieved using `next()`, why `StopIteration` exists, and how the Iterator Protocol powers every `for` loop. This knowledge forms the foundation for the next module, where you'll create your own custom iterators by implementing `__iter__()` and `__next__()`.
