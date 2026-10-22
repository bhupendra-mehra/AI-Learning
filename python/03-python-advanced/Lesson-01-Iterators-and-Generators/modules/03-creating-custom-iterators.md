# Module 03 – Creating Custom Iterators

## Module Overview

In Module 02, we learned that Python converts an iterable into an iterator using `iter()` and retrieves values one at a time using `next()`.

Now we will go one level deeper and create **our own iterator**.

Python allows us to control how an object behaves during iteration by implementing two special methods:

* `__iter__()`
* `__next__()`

These methods form the **Iterator Protocol**.

By implementing them inside a class, we can decide:

* What values should be returned.
* In what order they should be returned.
* When iteration should stop.

---

## Why This Module Is Important

Built-in objects such as lists already provide iteration functionality.

For example:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

But sometimes we need custom iteration behavior.

For example:

```text
Generate:

2
4
6
8
10
```

Or:

```text
Order-1001
Order-1002
Order-1003
Order-1004
```

Instead of creating and storing these values beforehand, we can build an iterator that produces them when requested.

---

# Learning Objectives

After completing this module, you will understand:

* Custom Iterators
* `__iter__()`
* `__next__()`
* `StopIteration`
* Maintaining iterator state
* Iterator lifecycle
* Using custom iterators with `for`
* Practical iterator use cases

---

# 1. Custom Iterator

A **custom iterator** is a class that controls its own iteration behavior.

For example, suppose we want:

```text
1
2
3
4
5
```

Instead of creating:

```python
numbers = [1, 2, 3, 4, 5]
```

we can create an iterator that generates those numbers.

---

# 2. `__iter__()` Method

`__iter__()` tells Python that an object supports iteration and returns an iterator object.

Example:

```python
def __iter__(self):
    return self
```

Here:

```python
return self
```

means:

> This object itself will act as the iterator.

---

# 3. `__next__()` Method

`__next__()` determines what value should be returned next.

Example:

```python
def __next__(self):
    self.current += 1
    return self.current
```

Every time Python calls `next()`, this method executes.

---

# 4. Creating Our First Custom Iterator

Consider:

```python
class NumberIterator:

    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.current >= self.limit:
            raise StopIteration

        self.current += 1

        return self.current
```

Create the object:

```python
numbers = NumberIterator(5)
```

Then:

```python
print(next(numbers))
print(next(numbers))
print(next(numbers))
```

Output:

```text
1
2
3
```

---

# 5. Understanding the Code

Let's understand what happened.

When:

```python
numbers = NumberIterator(5)
```

Python calls:

```python
__init__()
```

and creates:

```text
limit = 5
current = 0
```

Now:

```python
next(numbers)
```

calls:

```python
__next__()
```

The first time:

```text
current = 0

↓

current = 1

↓

return 1
```

Second call:

```text
current = 1

↓

current = 2

↓

return 2
```

This continues until:

```text
current = 5
```

Then:

```python
raise StopIteration
```

ends the iteration.

---

# 6. Using Custom Iterator with `for`

Here's where it becomes interesting.

We don't have to manually call:

```python
next(numbers)
```

A `for` loop can use our iterator automatically.

Example:

```python
numbers = NumberIterator(5)

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

Python automatically handles `StopIteration`.

---

# 7. What Happens Internally?

When Python sees:

```python
for number in numbers:
```

it conceptually performs:

```python
iterator = iter(numbers)
```

That calls:

```python
numbers.__iter__()
```

which returns:

```python
self
```

Then Python repeatedly calls:

```python
next(iterator)
```

which calls:

```python
__next__()
```

until:

```python
StopIteration
```

is raised.

---

# Iterator Lifecycle

Our custom iterator follows this flow:

```text
Create Object
     ↓
__init__()
     ↓
iter()
     ↓
__iter__()
     ↓
next()
     ↓
__next__()
     ↓
Return Value
     ↓
next()
     ↓
Return Next Value
     ↓
...
     ↓
StopIteration
```

This is the complete Iterator Protocol in action.

---

# Another Example – Even Numbers

Suppose we want:

```text
2
4
6
8
10
```

We can create:

```python
class EvenNumbers:

    def __init__(self, limit):
        self.limit = limit
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.limit:
            raise StopIteration

        number = self.current

        self.current += 2

        return number
```

Use:

```python
numbers = EvenNumbers(10)

for number in numbers:
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

Notice something important.

We never created:

```python
[2, 4, 6, 8, 10]
```

The values are generated as they're requested.

---

# Iterator State

An iterator remembers its current position.

For example:

```python
numbers = NumberIterator(5)

print(next(numbers))
print(next(numbers))
```

Output:

```text
1
2
```

If we now run:

```python
print(next(numbers))
```

Python doesn't start again from `1`.

It returns:

```text
3
```

The iterator remembers:

```text
Current Position = 2
```

This is called **maintaining state**.

---

# Exhausted Iterators

Consider:

```python
numbers = NumberIterator(3)

for number in numbers:
    print(number)
```

Output:

```text
1
2
3
```

Now try:

```python
for number in numbers:
    print(number)
```

Nothing prints.

Why?

Because the iterator has already reached:

```text
StopIteration
```

It is **exhausted**.

You would need a new object:

```python
numbers = NumberIterator(3)
```

to start again with this implementation.

---

# Real-World Example – Order IDs

Imagine processing order numbers:

```python
class OrderIterator:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.end:
            raise StopIteration

        order = f"Order-{self.current}"

        self.current += 1

        return order
```

Use:

```python
orders = OrderIterator(1001, 1005)

for order in orders:
    print(order)
```

Output:

```text
Order-1001
Order-1002
Order-1003
Order-1004
Order-1005
```

This demonstrates that iterators don't have to return numbers.

They can return:

* Strings
* Objects
* Database records
* Products
* Orders
* API results
* Files
* AI dataset records

---

# Best Practices

Use custom iterators when:

* You need custom iteration behavior.
* Values can be generated sequentially.
* Data doesn't need to exist beforehand.
* You're processing large datasets.
* You want controlled traversal.

For simple cases, however, generators are usually easier than creating iterator classes.

We will learn generators in Module 04.

---

# Common Mistakes

## Forgetting `StopIteration`

Incorrect:

```python
def __next__(self):
    self.current += 1
    return self.current
```

This iterator would continue forever.

Always define when iteration should stop if the sequence is meant to be finite.

---

## Forgetting `__iter__()`

A custom iterator should implement:

```python
def __iter__(self):
    return self
```

along with:

```python
def __next__(self):
```

---

## Resetting State Inside `__next__()`

Don't do:

```python
def __next__(self):
    self.current = 0
```

because every call would reset the iterator.

State should normally be initialized in:

```python
__init__()
```

---

# Exercises

## Exercise 01

Create:

```text
exercises/exercise-03.py
```

Create a custom iterator:

```text
OddNumberIterator
```

It should output:

```text
1
3
5
7
9
```

when:

```python
numbers = OddNumberIterator(10)

for number in numbers:
    print(number)
```

Requirements:

* Use a class.
* Implement `__init__()`.
* Implement `__iter__()`.
* Implement `__next__()`.
* Use `StopIteration`.

---

## Exercise 02

Create:

```text
exercises/exercise-04.py
```

Build:

```text
ProductIterator
```

It should accept:

```python
products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Headphones",
    "Keyboard"
]
```

Then:

```python
iterator = ProductIterator(products)

for product in iterator:
    print(product)
```

Expected:

```text
Laptop
Mobile
Tablet
Headphones
Keyboard
```

Do not use another `for` loop inside the iterator class.

Use:

```python
__iter__()
```

and:

```python
__next__()
```

to control iteration.

---

# Interview Questions

### What is a custom iterator?

A custom iterator is a Python object that implements the Iterator Protocol and defines its own logic for returning values sequentially.

### Which methods are required?

The two important methods are:

```python
__iter__()
```

and:

```python
__next__()
```

### What does `__iter__()` do?

It returns an iterator object. For an iterator class, this is commonly:

```python
return self
```

### What does `__next__()` do?

It returns the next value and raises `StopIteration` when no values remain.

### Why does an iterator maintain state?

It needs to remember its current position so subsequent calls to `next()` continue from where the previous call stopped.

### Can a custom iterator work with a `for` loop?

Yes. Python automatically uses the Iterator Protocol when processing it.

---

# Where You'll Use This Later

## FastAPI

Streaming large responses without loading everything into memory.

## Database Development

Processing query results sequentially.

## AI

Processing large datasets in batches or records.

## LLM Applications

Streaming generated output instead of waiting for the entire response.

## Magento Integration

Processing large:

```text
Product catalogs
Orders
Customers
Inventory records
Exports
Imports
```

without unnecessarily loading everything into memory.

---

# Key Takeaways

* Custom iterators control how Python traverses data.
* `__iter__()` returns the iterator.
* `__next__()` returns the next value.
* `StopIteration` ends iteration.
* Iterators maintain their current state.
* Exhausted iterators don't automatically restart.
* `for` loops automatically handle Iterator Protocol mechanics.
* Custom iterators can generate values instead of storing them beforehand.

---

# Module Summary

A custom iterator gives us complete control over how Python retrieves values from an object.

The most important concept to remember is:

```text
Iterable
   ↓
Iterator
   ↓
__iter__()
   ↓
__next__()
   ↓
Values
   ↓
StopIteration
```

Understanding this mechanism makes generators much easier because generators provide a simpler way of creating iterator behavior without manually implementing `__iter__()`, `__next__()`, state tracking, and `StopIteration`.
