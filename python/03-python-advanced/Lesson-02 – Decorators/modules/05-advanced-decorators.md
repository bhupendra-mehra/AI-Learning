# Module 05 – Advanced Decorators

## Module Overview

The decorator created in the previous module works only for functions without parameters. In real-world applications, decorators must support:

* Any number of positional arguments.
* Any number of keyword arguments.
* Functions that return values.
* Multiple decorators on the same function.
* Preserving function metadata.

This module extends the basic decorator into a reusable production-ready implementation.

---

# Learning Objectives

After completing this module, you will be able to:

* Understand `*args` and `**kwargs` in decorators.
* Decorate functions with parameters.
* Decorate functions that return values.
* Stack multiple decorators.
* Preserve function metadata using `functools.wraps`.

---

# Problem 1 – Functions with Parameters

Suppose we decorate:

```python
@logger
def add(a, b):
    return a + b
```

Our previous decorator was:

```python
def logger(function):

    def wrapper():
        print("Before Function")

        function()

        print("After Function")

    return wrapper
```

Calling:

```python
add(10, 20)
```

produces:

```text
TypeError:
wrapper() takes 0 positional arguments
but 2 were given
```

Why?

Because `wrapper()` accepts no parameters.

---

# Solution – *args and **kwargs

```python
def logger(function):

    def wrapper(*args, **kwargs):

        print("Function Started")

        result = function(*args, **kwargs)

        print("Function Completed")

        return result

    return wrapper
```

Now it works with **every function**.

---

# Understanding *args

Example:

```python
def display(*args):
    print(args)

display(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

`*args` collects all positional arguments into a tuple.

---

# Understanding **kwargs

Example:

```python
def display(**kwargs):
    print(kwargs)

display(name="John", age=25)
```

Output:

```text
{'name': 'John', 'age': 25}
```

`**kwargs` collects keyword arguments into a dictionary.

---

# Passing Arguments to the Original Function

Notice:

```python
function(*args, **kwargs)
```

This forwards **exactly** the same arguments that were received by the wrapper.

Without this line, the original function would never receive its inputs.

---

# Returning Values

Consider:

```python
@logger
def add(a, b):
    return a + b
```

Inside the decorator:

```python
result = function(*args, **kwargs)
```

captures the return value.

Then:

```python
return result
```

passes it back to the caller.

Without returning the result:

```python
print(add(10, 20))
```

would print:

```text
None
```

---

# Stacking Decorators

Multiple decorators can be applied.

Example:

```python
@timer
@logger
def create_user():
    print("Creating User")
```

Execution order:

```text
timer

↓

logger

↓

create_user()

↓

logger

↓

timer
```

Think of decorators like layers wrapping the original function.

---

# Preserving Function Metadata

Consider:

```python
@logger
def add():
    """Adds two numbers"""
```

Now:

```python
print(add.__name__)
```

Output:

```text
wrapper
```

Instead of:

```text
add
```

The original function metadata is lost.

---

# functools.wraps

Python provides:

```python
from functools import wraps
```

Usage:

```python
from functools import wraps

def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print("Started")

        result = function(*args, **kwargs)

        print("Completed")

        return result

    return wrapper
```

Now:

```python
print(add.__name__)
```

Output:

```text
add
```

The original metadata is preserved.

---

# Why Is wraps Important?

Frameworks like:

* FastAPI
* Flask
* Django
* PyTest

often inspect function names, signatures, and docstrings.

Without `@wraps`, that information may be replaced by the wrapper's metadata.

---

# Real-World Example

```python
@logger
@timer
def export_products(products):
    ...
```

Logging and timing can be added without changing the export logic.

---

# Best Practices

* Always use `*args` and `**kwargs` in reusable decorators.
* Return the original function's return value.
* Use `@wraps` for production decorators.
* Keep decorators focused on one responsibility.
* Avoid deeply stacking decorators unless necessary.

---

# Common Mistakes

## Mistake 1

Ignoring return values.

```python
function(*args, **kwargs)
```

Instead of:

```python
return function(*args, **kwargs)
```

---

## Mistake 2

Forgetting `*args` and `**kwargs`.

The decorator will only work with functions that have no parameters.

---

## Mistake 3

Not using `@wraps`.

This causes the original function's metadata to be lost.

---

## Mistake 4

Changing arguments unintentionally inside the decorator.

Decorators should normally forward arguments unchanged unless their purpose is validation or transformation.

---

# Interview Questions & Answers

## 1. Why do decorators use `*args` and `**kwargs`?

**Interview Answer**

They allow a decorator to work with functions that accept any number of positional and keyword arguments.

---

## 2. Why should decorators return the original function's result?

**Interview Answer**

Without returning the result, decorated functions lose their original return value, which can break application logic.

---

## 3. Why is `functools.wraps` important?

**Interview Answer**

It preserves the original function's metadata, including its name, docstring, and other attributes, which is important for debugging and many Python frameworks.

---

## 4. Can multiple decorators be applied to the same function?

**Interview Answer**

Yes. Python applies them from the bottom up during decoration, and execution flows through the nested wrapper functions.

---

# Key Takeaways

* `*args` handles positional arguments.
* `**kwargs` handles keyword arguments.
* Always return the original function's result.
* Use `@wraps` in production decorators.
* Decorators can be stacked.

---

# Module Summary

This module transformed a basic decorator into a production-ready implementation. You learned how to support functions with different argument types, preserve return values, stack decorators, and maintain metadata using `functools.wraps`. These practices are essential when building decorators for real-world Python applications.

---

# Knowledge Check

1. Why do decorators use `*args`?
2. What is the purpose of `**kwargs`?
3. Why should a decorator return the original function's result?
4. What problem does `functools.wraps` solve?
5. What happens if you forget `return result`?
6. Can multiple decorators be applied to one function?
7. In what order are stacked decorators executed?

---

# Practical Exercise

Create:

```text
exercises/exercise-07.py
```

### Requirements

1. Create a decorator named `logger` that:

   * Prints `"Function Started"`
   * Accepts any arguments using `*args` and `**kwargs`
   * Calls the original function
   * Prints `"Function Completed"`
   * Returns the original function's result

2. Decorate these functions:

```python
def add(a, b):
    return a + b

def greet(name, city="Mumbai"):
    return f"Hello {name} from {city}"
```

3. Print:

```python
print(add(10, 20))
print(greet("Bhupendra"))
print(greet("John", city="Delhi"))
```

4. Add `@wraps` to your decorator and verify:

```python
print(add.__name__)
```

Expected output:

```text
add
```
