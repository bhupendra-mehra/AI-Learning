# Module 06 – Production Decorators

## Module Overview

In the previous modules, you learned how decorators work internally and how to build reusable decorators.

In this final module, we'll create decorators that solve real-world problems commonly found in backend applications.

These include:

* Logging function execution.
* Measuring execution time.
* Handling exceptions.
* Validating inputs.

Instead of changing business functions, we'll apply decorators to add these behaviors in a clean and reusable way.

---

# Learning Objectives

After completing this module, you will be able to:

* Build production-style decorators.
* Measure function execution time.
* Handle exceptions using decorators.
* Validate function inputs.
* Understand when decorators should (and should not) be used.

---

# 1. Logging Decorator

```python
from functools import wraps

def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(f"[LOG] Calling {function.__name__}")

        result = function(*args, **kwargs)

        print(f"[LOG] Completed {function.__name__}")

        return result

    return wrapper
```

Usage:

```python
@logger
def create_user():
    print("Creating User")
```

Output:

```text
[LOG] Calling create_user
Creating User
[LOG] Completed create_user
```

---

# 2. Execution Time Decorator

```python
import time
from functools import wraps

def timer(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = function(*args, **kwargs)

        end = time.perf_counter()

        print(f"Execution Time: {end - start:.6f} seconds")

        return result

    return wrapper
```

Usage:

```python
@timer
def calculate():
    total = sum(range(1000000))
    return total
```

---

# 3. Exception Handling Decorator

```python
from functools import wraps

def handle_errors(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        try:
            return function(*args, **kwargs)

        except Exception as error:
            print(f"Error: {error}")

    return wrapper
```

Usage:

```python
@handle_errors
def divide(a, b):
    return a / b
```

Now:

```python
divide(10, 0)
```

doesn't crash the program.

---

# 4. Input Validation Decorator

```python
from functools import wraps

def positive_numbers(function):

    @wraps(function)
    def wrapper(number):

        if number <= 0:
            raise ValueError("Number must be positive")

        return function(number)

    return wrapper
```

Usage:

```python
@positive_numbers
def square(number):
    return number ** 2
```

---

# Stacking Decorators

Multiple decorators can be combined.

```python
@logger
@timer
def export_products():
    ...
```

Execution Flow:

```text
logger

↓

timer

↓

export_products()

↓

timer

↓

logger
```

Each decorator has one responsibility.

---

# When Should You Use Decorators?

Good use cases:

* Logging
* Authentication
* Authorization
* Timing
* Validation
* Retry logic
* Caching
* Monitoring

Avoid decorators for:

* Business calculations
* Database queries
* Complex application workflows
* Large blocks of unrelated logic

Decorators should enhance behavior, not replace the function's responsibility.

---

# Best Practices

* One decorator = one responsibility.
* Keep wrappers lightweight.
* Use `@wraps`.
* Return the original function's result.
* Don't hide important business logic inside decorators.
* Give decorators meaningful names.

---

# Common Mistakes

## Too Much Logic

Bad:

```python
@logger
def create_order():
```

where the decorator also:

* Writes to the database.
* Sends emails.
* Calculates discounts.

A decorator should not perform unrelated business work.

---

## Swallowing Exceptions

Avoid:

```python
except Exception:
    pass
```

Always log or re-raise exceptions unless you have a good reason not to.

---

## Forgetting Return Values

Always return the wrapped function's result when appropriate.

---

# Interview Questions & Answers

## 1. Give some real-world uses of decorators.

**Interview Answer**

Logging, authentication, authorization, validation, execution timing, caching, retry mechanisms, monitoring, and exception handling.

---

## 2. Should business logic be placed inside decorators?

**Interview Answer**

No. Decorators should contain reusable infrastructure or cross-cutting concerns, not business-specific logic.

---

## 3. Why are decorators popular in backend frameworks?

**Interview Answer**

They provide a clean way to add reusable functionality around existing functions without modifying their implementation.

---

## 4. Can decorators change a function's return value?

**Interview Answer**

Yes. A decorator can inspect, modify, or replace the return value before returning it to the caller.

---

# Key Takeaways

* Decorators solve reusable engineering problems.
* Production decorators are usually small and focused.
* Multiple decorators can be combined.
* Use decorators for infrastructure concerns, not business logic.
* `@wraps` should be standard practice.

---

# Module Summary

This module demonstrated how decorators are applied in production code. Instead of modifying individual functions, decorators provide reusable solutions for logging, timing, validation, and exception handling. Keeping each decorator focused on a single responsibility results in cleaner, more maintainable applications.

---

# Knowledge Check

1. Name four common production uses of decorators.
2. Why shouldn't business logic be placed inside a decorator?
3. What are the advantages of stacking decorators?
4. Why is `@wraps` considered a best practice?
5. Can a decorator modify a function's return value?

---

# Practical Exercise

Create:

```text
exercises/exercise-08.py
```

### Requirements

1. Create these decorators:

   * `logger`
   * `timer`
   * `handle_errors`

2. Apply them to:

```python
def divide(a, b):
    return a / b
```

3. Test:

```python
print(divide(20, 5))
print(divide(20, 0))
```

4. Observe:

   * Function logging
   * Execution time
   * Graceful error handling

5. Add all three decorators to the same function and observe the execution order.
