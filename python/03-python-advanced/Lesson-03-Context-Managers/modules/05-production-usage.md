**`modules/module-05.md`**

# Module 05 – Production Usage

## Module Overview

Context managers are widely used in production Python applications whenever a resource or operation has a clear lifecycle:

```text
Acquire / Setup
       ↓
Use
       ↓
Cleanup / Release
```

You have already seen file handling as one example. In this module, we'll focus on where context managers are actually useful in real applications and how they can work together with the decorators learned in Lesson 02.

---

## 1. File Resource Management

You have already used:

```python
with open("products.txt", "r") as file:
    data = file.read()
```

This is one of the most common context-manager use cases.

The lifecycle is:

```text
Open File
   ↓
Read / Write
   ↓
Close File
```

The file is automatically closed when the `with` block finishes.

### Best Practice

Prefer:

```python
with open("products.txt") as file:
    data = file.read()
```

over:

```python
file = open("products.txt")

try:
    data = file.read()
finally:
    file.close()
```

when the resource supports the context-manager protocol.

---

## 2. Database Connections

Database connections often require proper resource management.

Conceptually:

```python
with database_connection() as connection:
    connection.execute("SELECT * FROM products")
```

The lifecycle becomes:

```text
Create Connection
       ↓
Execute Queries
       ↓
Close Connection
```

Depending on the database library, the context manager may also manage transaction behavior.

The important concept is that the code using the connection should not have to manually manage every cleanup operation.

---

## 3. Database Transactions

Transactions are one of the strongest real-world examples of context-manager usage.

Consider:

```python
with transaction(connection) as db:
    db.create_order()
    db.update_inventory()
```

The desired behavior is:

```text
Begin Transaction
       ↓
Execute Operations
       ↓
       ├── Success → COMMIT
       │
       └── Failure → ROLLBACK
```

A context manager provides a clear lifecycle around the transaction.

### Why is this useful?

Without structured resource management, developers may forget to:

* Commit successful operations.
* Roll back failed operations.
* Release database resources.
* Close connections when required.

---

## 4. Locks

Context managers are commonly used with thread locks.

Example:

```python
with lock:
    update_shared_data()
```

Conceptually:

```text
Acquire Lock
     ↓
Update Shared Data
     ↓
Release Lock
```

If an exception occurs:

```text
Acquire Lock
     ↓
Update Shared Data
     ↓
Exception
     ↓
Release Lock
```

The context manager ensures that the lock lifecycle is properly managed.

This is particularly important in concurrent applications.

---

## 5. Temporary Resources

Applications sometimes create resources that should exist only for a limited period.

Examples include:

* Temporary files.
* Temporary directories.
* Temporary configuration.
* Temporary application state.
* Temporary connections.

Conceptually:

```python
with temporary_resource() as resource:
    use_resource(resource)
```

Lifecycle:

```text
Create
  ↓
Use
  ↓
Cleanup
```

The caller doesn't need to remember the cleanup operation.

---

## 6. Network Resources

Network resources can also have a lifecycle:

```text
Connect
   ↓
Send / Receive
   ↓
Disconnect
```

A library may provide a context-manager interface such as:

```python
with network_connection() as connection:
    connection.send(data)
```

The exact implementation depends on the networking library.

The important principle remains:

```text
Connection Setup
       ↓
Communication
       ↓
Connection Cleanup
```

---

## 7. Multiple Context Managers

Python allows multiple context managers in one `with` statement.

Example:

```python
with open("products.txt") as source, open("output.txt", "w") as destination:

    for line in source:
        destination.write(line)
```

Both files are managed automatically.

Conceptually:

```text
Open Source
     ↓
Open Destination
     ↓
Process Data
     ↓
Close Destination
     ↓
Close Source
```

This is useful when multiple resources are required for the same operation.

---

## 8. Nested Context Managers

Context managers can also be nested:

```python
with database_connection() as connection:

    with transaction(connection) as transaction:

        transaction.create_order()
```

However, unnecessary nesting should be avoided.

When appropriate, multiple resources can be managed in one statement:

```python
with database_connection() as connection, transaction(connection) as transaction:
    transaction.create_order()
```

Choose the structure that makes the resource lifecycle easiest to understand.

---

## 9. Context Managers with Decorators

You have already learned decorators in Lesson 02.

Decorators and context managers can work together.

Example:

```python
@logger
@timer
def export_products():

    with export_session("products.txt") as file:
        export_data(file)
```

Here each component has a different responsibility.

### Decorators

Handle:

```text
Logging
Timing
```

### Context Manager

Handles:

```text
File lifecycle
```

### Business Function

Handles:

```text
Product export
```

This creates a clean separation of concerns.

---

## 10. Separation of Concerns

Consider:

```python
@logger
@timer
def export_products():

    with export_session("products.txt") as file:
        export_data(file)
```

Each component has one primary responsibility:

| Component        | Responsibility          |
| ---------------- | ----------------------- |
| `logger`         | Logging                 |
| `timer`          | Performance measurement |
| `export_session` | Resource lifecycle      |
| `export_data`    | Business logic          |

This is much cleaner than putting logging, timing, file management, exception handling, and business logic into one large function.

---

## 11. Context Managers in Web Applications

Context managers can be useful in backend applications for managing:

* Database sessions.
* Database transactions.
* Temporary resources.
* Locks.
* External connections.
* Request-scoped resources.

Conceptually:

```python
with database_session() as session:
    process_request(session)
```

The application can focus on processing the request while the context manager handles the session lifecycle.

---

## 12. Context Managers in AI Applications

Context managers can also be useful in AI applications when a resource has a defined lifecycle.

Examples include:

* Temporary files used for document processing.
* Database sessions used to retrieve AI application data.
* Connections to external services.
* Temporary model-processing resources.
* Resource locks.
* Temporary directories containing uploaded documents.

For example:

```python
with temporary_document() as document:
    process_document(document)
```

The lifecycle is:

```text
Create Temporary Resource
          ↓
Process Document
          ↓
Cleanup Temporary Resource
```

The AI logic doesn't need to manually handle every cleanup operation.

---

## 13. Context Managers in Testing

Context managers are also useful in tests.

For example, a test may temporarily change some application state:

```python
with temporary_configuration() as config:
    config["environment"] = "testing"

    run_test()
```

After the block:

```text
Testing Configuration
        ↓
Run Test
        ↓
Restore Original Configuration
```

This prevents temporary test changes from leaking into other tests.

---

## 14. Context Managers and Exception Handling

A context manager does not automatically mean that exceptions disappear.

Consider:

```python
with export_session("products.txt") as file:

    file.write("Laptop\n")

    raise ValueError("Export failed")
```

The context manager performs cleanup.

But unless the exception is deliberately suppressed, the exception continues to propagate.

This is why our implementation uses:

```python
raise
```

rather than silently returning.

The general production pattern is:

```text
Exception
   ↓
Cleanup
   ↓
Log / Handle if appropriate
   ↓
Propagate when necessary
```

---

## 15. Context Managers and the `finally` Principle

A very important production pattern is:

```python
try:
    yield resource

finally:
    cleanup(resource)
```

This ensures cleanup happens regardless of whether the operation succeeds or fails.

Remember:

```text
Success
   ↓
Cleanup

Failure
   ↓
Cleanup
   ↓
Exception continues
```

This is why `finally` is so important in context managers.

---

## 16. Don't Overuse Custom Context Managers

Not every piece of code needs a custom context manager.

For example, don't create:

```python
class ProductProcessor:
    def __enter__(self):
        ...

    def __exit__(self, ...):
        ...
```

unless there is a meaningful resource lifecycle to manage.

A context manager should normally represent something like:

```text
Acquire → Use → Release
```

or:

```text
Begin → Execute → Commit/Rollback
```

If there is no meaningful lifecycle, a normal function or class may be more appropriate.

---

## 17. Prefer Existing Context Managers

Before creating your own context manager, check whether the Python standard library or the library you're using already provides one.

For example:

```python
with open("products.txt") as file:
    ...
```

There is no need to create another file-opening context manager unless you need additional behavior.

Similarly, many database, threading, temporary-resource, and networking libraries already provide context-manager support.

### Practical Rule

```text
Existing context manager available
             ↓
          Use it

No suitable context manager
             ↓
      Create your own
```

---

## 18. Context Manager Design Principles

A good context manager should have a clear responsibility.

### Good

```python
with database_transaction(connection):
    create_order()
```

The context manager manages the transaction lifecycle.

### Good

```python
with export_session("products.txt") as file:
    export_products(file)
```

The context manager manages the export resource lifecycle.

### Avoid

```python
with application_manager():
    generate_products()
    calculate_salary()
    send_email()
    update_database()
    create_report()
```

if the context manager has no meaningful relationship with all these operations.

Keep the lifecycle focused.

---

# 19. Production Checklist

When creating or using a context manager, consider:

* What resource or operation is being managed?
* What needs to happen during setup?
* What needs to happen during cleanup?
* What happens if an exception occurs?
* Should the exception propagate?
* Is cleanup guaranteed with `finally`?
* Does an existing context manager already solve the problem?
* Is the context manager responsible for only one clear lifecycle?
* Would `@contextmanager` be sufficient?
* Is a class-based implementation needed?

---

# 20. Context Manager Decision Guide

Use this simple decision process:

```text
Does the operation have a resource lifecycle?
              │
             Yes
              ↓
Can an existing context manager handle it?
         ↙           ↘
       Yes            No
        ↓              ↓
     Use it       Create one
                       ↓
             Simple lifecycle?
                  ↙       ↘
                Yes        No
                 ↓          ↓
          @contextmanager  Class
```

---

# 21. Complete Production Pattern

A realistic combination of the concepts learned in Lessons 01–03 could look like:

```python
from contextlib import contextmanager
from functools import wraps
import time


def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(f"[LOG] Calling {function.__name__}")

        result = function(*args, **kwargs)

        print(f"[LOG] Completed {function.__name__}")

        return result

    return wrapper


def timer(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        try:
            return function(*args, **kwargs)

        finally:
            end = time.perf_counter()

            print(
                f"[TIMER] {function.__name__} "
                f"took {end - start:.6f} seconds"
            )

    return wrapper


@contextmanager
def export_session(filename):

    file = open(filename, "w")

    try:
        yield file

    finally:
        file.close()


@logger
@timer
def export_products(products, filename):

    with export_session(filename) as file:

        for product in products:
            file.write(f"{product}\n")
```

This combines:

```text
Lesson 01
Generators
    ↓
Lesson 02
Decorators
    ↓
Lesson 03
Context Managers
```

into a single application pattern.

---

# Interview Questions & Answers

## 1. Where are context managers commonly used?

> They are commonly used for files, database connections and transactions, locks, temporary resources, network resources, and other operations requiring reliable setup and cleanup.

## 2. Why are context managers useful in production applications?

> They provide a consistent and reliable way to manage resources and ensure cleanup even when exceptions occur.

## 3. Should every resource have a custom context manager?

> No. Existing context managers should be preferred when they already provide the required behavior.

## 4. When should you create a custom context manager?

> When an operation has a meaningful setup and cleanup lifecycle that isn't adequately handled by an existing context manager.

## 5. What is the advantage of combining decorators and context managers?

> Decorators can handle cross-cutting concerns such as logging and timing, while context managers manage resource lifecycles. This keeps responsibilities separated.

## 6. Should a context manager always suppress exceptions?

> No. Exceptions should normally propagate unless the context manager has a specific reason to handle and suppress them.

## 7. Why is `finally` important in context managers?

> It ensures cleanup code executes whether the managed operation succeeds or raises an exception.

---

# Key Takeaways

Context managers are primarily about **resource and lifecycle management**.

Remember:

```text
Context Manager
      ↓
Setup
      ↓
Use
      ↓
Cleanup
```

Common real-world examples:

```text
File
 ↓
Open → Use → Close

Database
 ↓
Connect → Query → Close

Transaction
 ↓
Begin → Execute → Commit/Rollback

Lock
 ↓
Acquire → Use → Release

Temporary Resource
 ↓
Create → Use → Delete
```

And the key design principle:

> **A context manager should manage a clear resource or operation lifecycle.**

---

# Module 05 Exercise

No separate coding exercise is required for this module.

The purpose of Module 05 is to understand **where context managers are actually useful in production**, and you've already implemented both:

* A class-based context manager.
* A `@contextmanager` implementation.

Instead, use these questions as the final knowledge check:

1. Give three real-world situations where a context manager is useful.
2. Why should you prefer an existing context manager when one is available?
3. When would you choose `@contextmanager` instead of a class?
4. Why should cleanup normally be placed in `finally`?
5. Should context managers normally suppress exceptions?
6. How can decorators and context managers work together?
7. What does `Acquire → Use → Release` represent?

---
