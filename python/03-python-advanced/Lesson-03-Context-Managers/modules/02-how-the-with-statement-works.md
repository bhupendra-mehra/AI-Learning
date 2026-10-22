# Module 02 – How the `with` Statement Works

## Module Overview

In Module 01, you learned **why** context managers exist.

Now we'll understand **how Python actually implements them**.

When you write:

```python
with resource as value:
    do_something()
```

Python uses two special methods:

```python
__enter__()
__exit__()
```

These methods form the **context manager protocol**.

This module is important because you'll eventually create your own context managers, but we won't add a coding exercise just for the sake of practice. We'll use a practical implementation only where it represents a real-world use case.

---

# 1. The Context Manager Protocol

A class can be used with `with` when it implements:

```python
__enter__()
__exit__()
```

Example:

```python
class MyContext:

    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
```

Now:

```python
with MyContext():
    print("Inside context")
```

Output:

```text
Entering context
Inside context
Exiting context
```

---

# 2. What Does `__enter__()` Do?

`__enter__()` executes when Python enters the `with` block.

```python
with MyContext():
```

Python effectively calls:

```python
context.__enter__()
```

It is normally used for:

* Acquiring resources
* Initializing state
* Opening connections
* Creating temporary resources

---

# 3. What Does `__exit__()` Do?

`__exit__()` executes when Python leaves the `with` block.

It is used for:

* Closing resources
* Releasing locks
* Cleaning temporary resources
* Committing or rolling back operations
* Handling exceptions

Conceptually:

```text
with
 ↓
__enter__()
 ↓
Code Block
 ↓
__exit__()
```

---

# 4. What Does `as` Mean?

Consider:

```python
with MyContext() as value:
    print(value)
```

The value returned by:

```python
__enter__()
```

is assigned to:

```python
value
```

For example:

```python
class MyContext:

    def __enter__(self):
        return "Hello"

    def __exit__(self, exc_type, exc_value, traceback):
        pass


with MyContext() as value:
    print(value)
```

Output:

```text
Hello
```

Because:

```text
__enter__()
   ↓
returns "Hello"
   ↓
value = "Hello"
```

---

# 5. Understanding `__exit__()` Parameters

This is one of the most important parts of custom context managers.

```python
def __exit__(self, exc_type, exc_value, traceback):
```

Python provides three pieces of exception information.

### `exc_type`

The type of exception.

Example:

```text
ZeroDivisionError
```

### `exc_value`

The actual exception object.

Example:

```text
division by zero
```

### `traceback`

Information about where the exception occurred.

---

# 6. When There Is No Exception

Consider:

```python
with MyContext():
    print("Success")
```

Then:

```python
exc_type
exc_value
traceback
```

will all be:

```python
None
```

So conceptually:

```text
Successful execution

__exit__(
    None,
    None,
    None
)
```

---

# 7. When an Exception Occurs

Consider:

```python
with MyContext():

    print("Starting")

    raise ValueError("Something went wrong")
```

Python calls:

```python
__exit__(
    ValueError,
    ValueError("Something went wrong"),
    traceback
)
```

This allows the context manager to know that an exception occurred.

---

# 8. Exception Suppression

Here's something important.

`__exit__()` can decide whether the exception should continue propagating.

If it returns:

```python
False
```

or:

```python
None
```

the exception continues.

If it returns:

```python
True
```

the exception is suppressed.

Example:

```python
class IgnoreError:

    def __enter__(self):
        print("Enter")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Error handled")
        return True
```

Then:

```python
with IgnoreError():
    raise ValueError("Test")
```

Output:

```text
Enter
Error handled
```

The program continues because:

```python
return True
```

suppressed the exception.

---

# 9. Should We Suppress Exceptions?

Usually, **not automatically**.

This:

```python
return True
```

can hide important application errors.

For example, silently suppressing:

```text
Database connection failure
Payment failure
File corruption
API failure
```

could make debugging extremely difficult.

Only suppress an exception when the context manager has a clear reason to handle it.

---

# 10. `__enter__()` and `__exit__()` Execution Flow

Successful execution:

```text
with
 ↓
__enter__()
 ↓
Code
 ↓
__exit__(None, None, None)
 ↓
Continue
```

Failed execution:

```text
with
 ↓
__enter__()
 ↓
Code
 ↓
Exception
 ↓
__exit__(exception information)
 ↓
Return True?
   ↙       ↘
 Yes       No
  ↓         ↓
Suppress   Propagate
```

This is the core context manager mechanism.

---

# 11. How `open()` Relates to This

When you write:

```python
with open("products.txt") as file:
    data = file.read()
```

`open()` returns an object that supports the context manager protocol.

Conceptually:

```text
open()
 ↓
file object
 ↓
__enter__()
 ↓
file available
 ↓
read file
 ↓
__exit__()
 ↓
file closed
```

You don't need to manually call:

```python
file.close()
```

---

# 12. Context Manager vs `try/finally`

These are conceptually similar.

### Manual approach

```python
resource = acquire()

try:
    use(resource)

finally:
    release(resource)
```

### Context manager

```python
with resource_manager() as resource:
    use(resource)
```

The context manager encapsulates the resource lifecycle so the calling code stays clean.

---

# 13. Real-World Example – Database Transaction

A transaction is a strong real-world use case.

Conceptually:

```python
with transaction() as db:

    db.create_order()

    db.update_inventory()
```

The context manager could implement:

```text
__enter__()
    ↓
BEGIN TRANSACTION

    ↓
Execute operations

    ↓

__exit__()

Success → COMMIT
Failure → ROLLBACK
```

This is exactly the kind of lifecycle that context managers are designed to represent.

---

# 14. Real-World Example – Lock

For concurrent applications:

```python
with lock:
    update_shared_data()
```

Conceptually:

```text
__enter__()
    ↓
Acquire Lock

update_shared_data()

__exit__()
    ↓
Release Lock
```

Even if `update_shared_data()` fails, the lock can be released.

---

# Best Practices

### Keep `__enter__()` focused

Use it for setup/resource acquisition.

### Keep `__exit__()` focused

Use it for cleanup/resource release.

### Don't hide exceptions unnecessarily

Only return `True` when suppression is intentional.

### Return useful values from `__enter__()`

If the caller needs the managed resource:

```python
return resource
```

---

# Common Mistakes

### Mistake 1 – Forgetting `__exit__()`

A class won't satisfy the normal context manager protocol if it doesn't implement the required methods.

### Mistake 2 – Returning `True` blindly

This can hide errors.

### Mistake 3 – Putting business logic into `__exit__()`

The context manager should manage the resource lifecycle, not perform unrelated business operations.

---

# Interview Questions & Answers

### 1. What are `__enter__()` and `__exit__()`?

> They are methods that implement Python's context manager protocol. `__enter__()` runs when entering a `with` block, while `__exit__()` runs when leaving it.

### 2. What does `__enter__()` return?

> It returns the value assigned to the variable after the `as` keyword.

### 3. What are the parameters of `__exit__()`?

> `exc_type`, `exc_value`, and `traceback`, which contain exception information when an exception occurs.

### 4. What happens if `__exit__()` returns `True`?

> The exception is suppressed and does not propagate outside the `with` block.

### 5. What happens if `__exit__()` returns `False` or `None`?

> The exception is not suppressed and continues to propagate.

### 6. Does `__exit__()` run when an exception occurs?

> Yes. One of its important purposes is to perform cleanup even when the code inside the context raises an exception.

---

# Key Takeaways

```text
__enter__()
    ↓
Setup / Acquire
    ↓
with block
    ↓
__exit__()
    ↓
Cleanup / Exception handling
```

Remember:

* `__enter__()` → **enter/setup**
* `__exit__()` → **exit/cleanup**
* `as value` → receives the return value of `__enter__()`
* `True` from `__exit__()` → suppress exception
* `False`/`None` → propagate exception

---

# Practical Exercise Decision

There is **no separate exercise for this module**.

We already used custom context-manager code to demonstrate the actual mechanism, and writing another artificial example would add little value.

The first meaningful practical implementation will come when we build a **real resource manager** in Module 03, where you'll create something that has an actual setup/use/cleanup lifecycle.

---

## Module 02 Status

```text
Lesson 03 – Context Managers

✅ Module 01 – Understanding Context Managers
✅ Module 02 – How the `with` Statement Works

Next → Module 03 – Creating Custom Context Managers
```

Module 03 is where we'll build our first **useful custom context manager**, rather than another toy example.
