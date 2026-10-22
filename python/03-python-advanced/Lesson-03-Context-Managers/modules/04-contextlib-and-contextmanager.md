# Module 04 – `contextlib` and `@contextmanager`

## Module Overview

In Module 03, you created a context manager using a class:

```python
class ExportSession:
    def __enter__(self):
        ...
    
    def __exit__(self, exc_type, exc_value, traceback):
        ...
```

This approach is powerful, but for simple setup/cleanup operations, it can require quite a lot of code.

Python provides `contextlib` to make these context managers simpler.

The main tool we'll learn is:

```python
from contextlib import contextmanager
```

---

# 1. Why `contextlib`?

Compare your class-based implementation:

```python
class ExportSession:

    def __enter__(self):
        ...
    
    def __exit__(self, exc_type, exc_value, traceback):
        ...
```

with:

```python
@contextmanager
def export_session():
    ...
    yield
    ...
```

The second approach can be much easier to read when the lifecycle is simple.

---

# 2. Basic `@contextmanager`

Import it:

```python
from contextlib import contextmanager
```

Then:

```python
@contextmanager
def my_context():

    print("Entering context")

    yield

    print("Exiting context")
```

Usage:

```python
with my_context():
    print("Inside context")
```

Output:

```text
Entering context
Inside context
Exiting context
```

---

# 3. Understanding `yield`

This is where your **Lesson 01 – Iterators & Generators** knowledge becomes useful.

You already learned that:

```python
yield
```

pauses a generator and resumes it later.

`@contextmanager` uses the same concept.

Consider:

```python
@contextmanager
def my_context():

    print("Before")

    yield

    print("After")
```

Execution:

```text
Before
  ↓
yield
  ↓
with block executes
  ↓
resume function
  ↓
After
```

So:

```python
yield
```

represents the point where control is handed to the `with` block.

---

# 4. Returning a Resource

We can return a value from `yield`.

Example:

```python
from contextlib import contextmanager


@contextmanager
def open_file(filename):

    file = open(filename, "w")

    try:
        yield file

    finally:
        file.close()
```

Now:

```python
with open_file("products.txt") as file:
    file.write("Laptop\n")
    file.write("Mobile\n")
```

The value:

```python
yield file
```

becomes:

```python
file
```

after `as`.

Conceptually:

```text
yield file
    ↓
as file
```

---

# 5. Why `try/finally`?

Notice:

```python
try:
    yield file

finally:
    file.close()
```

This is extremely important.

The code after `yield` must execute even if the `with` block raises an exception.

For example:

```python
with open_file("products.txt") as file:

    file.write("Laptop\n")

    raise ValueError("Something failed")
```

The exception occurs here:

```text
with block
    ↓
ValueError
```

but:

```python
finally:
    file.close()
```

still executes.

So:

```text
Acquire
   ↓
yield
   ↓
Use resource
   ↓
Exception
   ↓
finally
   ↓
Cleanup
```

---

# 6. Exception Handling with `@contextmanager`

We can also catch exceptions:

```python
from contextlib import contextmanager


@contextmanager
def export_session(filename):

    file = open(filename, "w")

    try:

        print(f"Starting export: {filename}")

        yield file

    except Exception as error:

        print(f"Export failed: {error}")

        raise

    finally:

        file.close()

        print("Export session closed")
```

Usage:

```python
with export_session("products.txt") as file:

    file.write("Laptop\n")
    file.write("Mobile\n")
```

Successful output:

```text
Starting export: products.txt
Export session closed
```

If an exception occurs:

```text
Starting export: products.txt
Export failed: Something went wrong
Export session closed
Traceback...
```

---

# 7. Comparing Your Class with `@contextmanager`

### Class-based

```python
class ExportSession:

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_value, traceback):
        ...
```

### Function-based

```python
@contextmanager
def export_session():

    # setup

    try:
        yield resource

    finally:
        # cleanup
```

They implement the same basic lifecycle.

```text
Class                         @contextmanager

__enter__()       ←→          code before yield

with block        ←→          yield

__exit__()        ←→          code after yield/finally
```

---

# 8. When Should You Use `@contextmanager`?

Use it when the context manager has a relatively simple lifecycle.

Good example:

```python
@contextmanager
def open_file(filename):
    file = open(filename)
    try:
        yield file
    finally:
        file.close()
```

A class may be better when you have:

* Complex internal state
* Multiple methods
* Multiple lifecycle operations
* More complicated behavior
* A reusable object representing the resource

---

# 9. Real-World Example – Temporary Resource

`contextlib` is useful for temporary resources.

Conceptually:

```python
@contextmanager
def temporary_resource():

    resource = create_resource()

    try:
        yield resource

    finally:
        delete_resource(resource)
```

Usage:

```python
with temporary_resource() as resource:
    use_resource(resource)
```

The caller doesn't need to remember cleanup.

---

# 10. Real-World Example – Database Transaction

A transaction can be represented as:

```python
@contextmanager
def transaction(connection):

    try:

        connection.begin()

        yield connection

        connection.commit()

    except Exception:

        connection.rollback()

        raise
```

Usage:

```python
with transaction(connection) as db:

    db.create_order()

    db.update_inventory()
```

Flow:

```text
BEGIN
  ↓
Execute operations
  ↓
Success?
 ↙       ↘
Yes      No
 ↓        ↓
COMMIT  ROLLBACK
```

This is a very practical context-manager pattern.

---

# 11. Context Managers and Decorators

You have now learned both.

### Decorator

```python
@logger
def export_products():
    ...
```

Adds behavior around **function execution**.

### Context Manager

```python
with export_session():
    ...
```

Manages **resource lifecycle around a block**.

They can also work together.

For example:

```python
@logger
@timer
def export_products():

    with export_session("products.txt") as file:
        ...
```

Now:

```text
Decorator
   ↓
Monitor function
   ↓
Context Manager
   ↓
Manage resource
   ↓
Execute export
   ↓
Cleanup resource
```

This combination will be useful in our Lesson 03 mini project.

---

# 12. Important Difference: `yield` vs `return`

This is worth remembering because you've already learned generators.

### `return`

```python
return file
```

ends the function.

### `yield`

```python
yield file
```

temporarily gives control to the `with` block and allows the function to continue afterward.

That's why:

```python
@contextmanager
def open_file():

    file = open(...)

    try:
        yield file

    finally:
        file.close()
```

can perform cleanup **after the `with` block finishes**.

---

# 13. Common Mistake

Don't write:

```python
@contextmanager
def open_file(filename):

    file = open(filename)

    yield file

    file.close()
```

This might work during normal execution, but cleanup is not protected against all failure scenarios.

Prefer:

```python
@contextmanager
def open_file(filename):

    file = open(filename)

    try:
        yield file

    finally:
        file.close()
```

The `finally` guarantees cleanup.

---

# 14. Interview Questions & Answers

### 1. What is `contextlib`?

> `contextlib` is a Python standard-library module that provides utilities for creating and working with context managers.

### 2. What does `@contextmanager` do?

> It converts a generator function into a context manager that can be used with the `with` statement.

### 3. What is the purpose of `yield`?

> It provides the value to the `with` block and separates resource setup from cleanup.

### 4. Why use `try/finally` around `yield`?

> To ensure cleanup happens even if an exception occurs inside the `with` block.

### 5. Class-based or `@contextmanager`?

> Use `@contextmanager` for simple setup and cleanup logic. Use a class when the context manager requires more complex state or behavior.

### 6. Does `@contextmanager` eliminate `__enter__()` and `__exit__()`?

> From the developer's implementation perspective, yes. `contextlib` handles the context-manager protocol internally.

---

# Key Takeaways

```text
@contextmanager
       ↓
Setup
       ↓
yield resource
       ↓
with block
       ↓
finally
       ↓
Cleanup
```

Remember these mappings:

```text
Class-Based                  @contextmanager

__enter__()          →       Code before yield

return resource      →       yield resource

__exit__()           →       Code after yield / finally
```

And most importantly:

> **`@contextmanager` is not a replacement for understanding `__enter__()` and `__exit__()`. It is a simpler way of implementing the same context-manager behavior when the lifecycle is straightforward.**

---

# Practical Exercise Decision

This module **does warrant a practical implementation**, because `@contextmanager` is a real production pattern and is directly relevant to the mini project.

However, we don't need multiple artificial exercises.

Create:

```text
exercises/exercise-04.py
```

Implement your previous `ExportSession` again, but this time using:

```python
from contextlib import contextmanager
```

Requirements:

* Accept a filename.
* Open the file before `yield`.
* `yield` the file object.
* Close the file in `finally`.
* Print a success message when completed.
* Print an error message when an exception occurs.
* Re-raise the exception.

Use:

```python
with export_session("products.txt") as file:
    file.write("Laptop\n")
    file.write("Mobile\n")
```

Then intentionally raise an exception and verify that the file is still closed.

This gives you a direct comparison:

```text
Module 03
Class-based ExportSession
        ↓
Module 04
@contextmanager ExportSession
```

---

## Module 04 Status

```text
Lesson 03 – Context Managers

✅ Module 01 – Understanding Context Managers
✅ Module 02 – How the `with` Statement Works
✅ Module 03 – Creating Custom Context Managers
🔄 Module 04 – contextlib & @contextmanager

Next → Module 05 – Production Usage
```
