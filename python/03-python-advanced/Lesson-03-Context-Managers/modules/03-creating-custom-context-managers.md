# Module 03 – Creating Custom Context Managers

## Module Overview

In Module 02, you learned the context manager protocol:

```python
__enter__()
__exit__()
```

Now we'll use that knowledge to create **custom context managers**.

There are two main approaches:

1. **Class-based context manager**
2. **Function-based context manager using `@contextmanager`**

We'll first understand the class-based approach because it makes the underlying mechanism very clear. Then we'll use `contextlib` to create the same type of resource manager with less code.

---

# 1. Class-Based Context Manager

A class becomes a context manager by implementing:

```python
__enter__()
__exit__()
```

Basic structure:

```python
class MyContext:

    def __enter__(self):
        # setup
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # cleanup
        return False
```

Usage:

```python
with MyContext() as context:
    # use context
```

---

# 2. Real-World Example — File Export Session

Let's create something relevant to our existing product-export project.

Imagine we want every export operation to have a clear lifecycle:

```text
Start Export
     ↓
Write Products
     ↓
Export Completed
     ↓
Close Resource
```

We can create an `ExportSession` context manager.

```python
class ExportSession:

    def __enter__(self):
        print("Starting export session")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing export session")
        return False
```

Usage:

```python
with ExportSession():
    print("Exporting products...")
```

Output:

```text
Starting export session
Exporting products...
Closing export session
```

---

# 3. Returning a Resource

Usually, the main purpose of `__enter__()` is to return something useful.

For example:

```python
class ExportSession:

    def __enter__(self):
        self.file = open("products.txt", "w")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        return False
```

Now:

```python
with ExportSession() as file:
    file.write("Laptop\n")
    file.write("Mobile\n")
```

The flow is:

```text
ExportSession()
      ↓
__enter__()
      ↓
Open file
      ↓
return file
      ↓
file = returned value
      ↓
Write data
      ↓
__exit__()
      ↓
Close file
```

This is a **real use case**, because we're managing the file's lifecycle ourselves.

---

# 4. Why Create This Instead of Using `open()`?

Normally, you should simply use:

```python
with open("products.txt", "w") as file:
    ...
```

There is no reason to create a custom context manager just to duplicate `open()`.

Custom context managers become useful when you have **additional resource-management behavior**.

For example:

```text
Open file
   ↓
Write export header
   ↓
Track export state
   ↓
Close file
   ↓
Log completion
```

That lifecycle isn't provided directly by `open()`.

---

# 5. A More Useful Export Session

Let's build one.

```python
class ExportSession:

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):

        print(f"Starting export: {self.filename}")

        self.file = open(self.filename, "w")

        self.file.write("Product Export\n")
        self.file.write("====================\n")

        return self.file

    def __exit__(self, exc_type, exc_value, traceback):

        if self.file:
            self.file.close()

        if exc_type:
            print(f"Export failed: {exc_value}")
        else:
            print("Export completed successfully")

        return False
```

Usage:

```python
with ExportSession("products.txt") as file:

    file.write("Laptop\n")
    file.write("Mobile\n")
    file.write("Tablet\n")
```

Output:

```text
Starting export: products.txt
Export completed successfully
```

And:

```text
products.txt
```

contains:

```text
Product Export
====================
Laptop
Mobile
Tablet
```

This is a meaningful custom context manager because it manages an **export session**, not just a file.

---

# 6. Handling Exceptions

Suppose:

```python
with ExportSession("products.txt") as file:

    file.write("Laptop\n")

    raise ValueError("Export failed")
```

The exception reaches:

```python
__exit__(
    ValueError,
    ValueError("Export failed"),
    traceback
)
```

Our code:

```python
if exc_type:
    print(f"Export failed: {exc_value}")
```

prints:

```text
Export failed: Export failed
```

Then:

```python
return False
```

allows the exception to continue propagating.

This is generally the safer default.

---

# 7. Why Return `False`?

Remember:

```python
return True
```

means:

> "I handled this exception. Don't propagate it."

While:

```python
return False
```

means:

> "I did not suppress this exception. Let it continue."

For our export session:

```python
return False
```

is appropriate because an export failure should not silently disappear.

---

# 8. Cleanup Must Happen Regardless

Notice that we close the file before checking the exception:

```python
if self.file:
    self.file.close()
```

Therefore:

```text
Successful export
       ↓
Close file
       ↓
Success message
```

and:

```text
Failed export
       ↓
Close file
       ↓
Error message
       ↓
Exception propagates
```

The resource cleanup happens in both cases.

---

# 9. `__enter__()` Can Return Different Things

You don't have to return `self`.

For example:

```python
def __enter__(self):
    self.file = open(self.filename, "w")
    return self.file
```

Then:

```python
with ExportSession("products.txt") as file:
```

means:

```text
file
 ↓
value returned by __enter__()
```

You can return:

* `self`
* a file
* a database connection
* a transaction object
* a custom resource

depending on what the caller needs.

---

# 10. `__enter__()` Can Also Fail

Consider:

```python
with ExportSession("/invalid/path/products.txt"):
    ...
```

If opening the file fails inside `__enter__()`:

```python
self.file = open(...)
```

then `__exit__()` is **not called**, because the context was never successfully entered.

This is an important detail.

The lifecycle is:

```text
__enter__ succeeds
       ↓
with block executes
       ↓
__exit__ executes
```

If:

```text
__enter__ fails
```

the `with` block never starts.

---

# 11. Class-Based Context Manager Pattern

A useful pattern to remember:

```python
class ResourceManager:

    def __init__(self, resource):
        self.resource = resource

    def __enter__(self):
        # acquire/setup
        return self.resource

    def __exit__(self, exc_type, exc_value, traceback):
        # cleanup
        return False
```

Think:

```text
__init__
   ↓
Store configuration

__enter__
   ↓
Acquire resource

with block
   ↓
Use resource

__exit__
   ↓
Release resource
```

---

# 12. Function-Based Context Managers

Writing a class can sometimes feel excessive for a simple lifecycle.

Python's `contextlib` provides another approach.

```python
from contextlib import contextmanager
```

Then:

```python
@contextmanager
def export_session(filename):

    file = open(filename, "w")

    try:
        yield file

    finally:
        file.close()
```

Usage:

```python
with export_session("products.txt") as file:
    file.write("Laptop\n")
    file.write("Mobile\n")
```

Much shorter.

---

# 13. Understanding `yield`

This is an important connection with your **Lesson 01 – Iterators & Generators**.

You already learned:

```python
yield
```

in generators.

Here, `yield` divides the context manager into two parts:

```python
@contextmanager
def export_session(filename):

    # BEFORE yield
    file = open(filename, "w")

    try:
        yield file

    finally:
        # AFTER yield
        file.close()
```

Think of it as:

```text
Before yield
     ↓
__enter__ equivalent
     ↓
with block
     ↓
yield returns resource
     ↓
with block finishes
     ↓
After yield
     ↓
__exit__ equivalent
```

This is one reason your previous understanding of generators is useful here.

---

# 14. Class vs `@contextmanager`

### Class-based

```python
class ExportSession:

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_value, traceback):
        ...
```

Advantages:

* Explicit lifecycle.
* Easy to maintain complex state.
* Good when the context manager is substantial.
* Makes the protocol visible.

### `@contextmanager`

```python
@contextmanager
def export_session():
    ...
    yield
    ...
```

Advantages:

* Less code.
* Easy to read.
* Excellent for simple setup/cleanup.
* Convenient for small resource-management utilities.

---

# 15. Which Should You Use?

A practical rule:

```text
Simple setup + cleanup
        ↓
@contextmanager

Complex state/lifecycle
        ↓
Class-based context manager
```

Don't choose the class-based approach just because it is more advanced.

Choose the simplest implementation that clearly represents the lifecycle.

---

# Real-World Examples

### Database transaction

```python
with transaction() as db:
    ...
```

### Temporary directory

```python
with temporary_directory() as directory:
    ...
```

### File export

```python
with export_session("products.txt") as file:
    ...
```

### Lock

```python
with lock:
    update_data()
```

These all follow the same principle:

```text
Acquire
   ↓
Use
   ↓
Release
```

---

# Interview Questions & Answers

### 1. How do you create a custom context manager?

> Implement `__enter__()` and `__exit__()` in a class, or use `contextlib.contextmanager` with a function containing `yield`.

### 2. What does `__enter__()` normally do?

> It performs setup or resource acquisition and returns the value that can be assigned using `as`.

### 3. What does `__exit__()` normally do?

> It performs cleanup and can also inspect or handle exceptions raised inside the context.

### 4. Why might `__exit__()` return `False`?

> To allow an exception to propagate instead of suppressing it.

### 5. When would you use `@contextmanager`?

> When the context manager has a relatively simple setup and cleanup lifecycle and a class would add unnecessary code.

### 6. What is the role of `yield` in `@contextmanager`?

> It separates the setup portion from the code executed inside the `with` block and provides the value returned after `as`.

### 7. Is `__exit__()` called if `__enter__()` fails?

> No. The context was never successfully entered, so `__exit__()` is not invoked.

---

# Practical Exercise

This module **does warrant a practical exercise** because creating a custom context manager is a real-world skill, not just theory.

Create:

```text
exercises/exercise-03.py
```

Build a simple `ExportSession` context manager that:

1. Accepts a filename.
2. Opens the file in `__enter__()`.
3. Returns the opened file.
4. Writes product data inside the `with` block.
5. Closes the file in `__exit__()`.
6. Prints whether the export succeeded or failed.
7. Does **not** suppress exceptions.

Use it like:

```python
with ExportSession("products.txt") as file:
    file.write("Laptop\n")
    file.write("Mobile\n")
    file.write("Tablet\n")
```

Then test a failure:

```python
with ExportSession("products.txt") as file:
    file.write("Laptop\n")
    raise ValueError("Export failed")
```

The important part isn't writing a large application. The goal is to verify that you understand this lifecycle:

```text
__enter__()
    ↓
resource acquired
    ↓
with block
    ↓
__exit__()
    ↓
resource cleaned up
```
