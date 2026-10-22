# Module 04 – Building Your First Decorator

## Module Overview

In the previous modules, you learned three essential concepts:

1. Nested Functions
2. Returning Functions
3. Closures

A decorator simply combines these concepts into one reusable pattern.

A decorator is a function that:

* Accepts another function as input.
* Creates a new function.
* Executes additional logic.
* Calls the original function.
* Returns the new function.

Once you understand this flow, the `@decorator` syntax becomes just a convenient shortcut.

---

# Learning Objectives

After completing this module, you will be able to:

* Create your first decorator.
* Understand wrapper functions.
* Decorate functions manually.
* Use the `@` syntax.
* Understand how decorators execute.

---

# Step 1 – Functions Can Be Passed as Arguments

Just as integers or strings can be passed to a function, functions can also be passed.

```python
def greet():
    print("Hello")


def execute(function):
    function()


execute(greet)
```

Output:

```text
Hello
```

Notice:

```python
execute(greet)
```

We pass the **function itself**, not `greet()`.

---

# Step 2 – A Simple Decorator

```python
def logger(function):

    def wrapper():
        print("Before Function")

        function()

        print("After Function")

    return wrapper
```

Let's understand this carefully.

### The decorator receives:

```python
function
```

↓

Creates:

```python
wrapper()
```

↓

Calls:

```python
function()
```

↓

Returns:

```python
wrapper
```

---

# Step 3 – Manual Decoration

Suppose we have:

```python
def welcome():
    print("Welcome User")
```

Instead of using `@`, decorate it manually.

```python
decorated = logger(welcome)

decorated()
```

Output:

```text
Before Function
Welcome User
After Function
```

What happened?

```text
welcome
        │
        ▼
logger()
        │
Creates wrapper()
        │
        ▼
Returns wrapper
        │
        ▼
decorated()
```

The original function never changed.

It was simply wrapped.

---

# Step 4 – The @ Syntax

Python provides a cleaner syntax.

Instead of:

```python
welcome = logger(welcome)
```

you simply write:

```python
@logger
def welcome():
    print("Welcome User")
```

This is exactly equivalent to:

```python
def welcome():
    print("Welcome User")


welcome = logger(welcome)
```

The `@` syntax is just syntactic sugar.

---

# Execution Flow

When Python sees:

```python
@logger
def welcome():
    print("Welcome")
```

Internally it performs:

```text
Create welcome()

↓

Pass welcome to logger()

↓

logger returns wrapper()

↓

Replace welcome with wrapper()

↓

Calling welcome() actually calls wrapper()
```

---

# Visual Flow

```text
Original Function

↓

Decorator

↓

Wrapper Function

↓

Original Function Executes

↓

Wrapper Completes
```

---

# Why Is This Useful?

Imagine 100 functions need logging.

Without decorators:

```python
def create_user():

    print("Log")

    ...

def update_user():

    print("Log")

    ...

def delete_user():

    print("Log")

    ...
```

With decorators:

```python
@logger
def create_user():
    ...

@logger
def update_user():
    ...

@logger
def delete_user():
    ...
```

One decorator.

Unlimited reuse.

---

# Best Practices

* A decorator should have one responsibility.
* Keep wrapper functions small.
* Do not place business logic inside decorators.
* Give decorators meaningful names.

---

# Common Mistakes

## Mistake 1

Passing:

```python
logger(welcome())
```

This executes `welcome()` immediately.

Correct:

```python
logger(welcome)
```

---

## Mistake 2

Returning:

```python
return wrapper()
```

Instead of:

```python
return wrapper
```

Remember:

* `wrapper()` → Execute now.
* `wrapper` → Return the function.

---

## Mistake 3

Forgetting to call the original function.

Incorrect:

```python
def wrapper():
    print("Before")
```

The original function never runs.

Correct:

```python
def wrapper():
    print("Before")

    function()

    print("After")
```

---

# Interview Questions & Answers

## 1. What is a decorator?

**Interview Answer**

A decorator is a function that accepts another function, adds additional behavior without modifying the original function, and returns a new function.

---

## 2. What does a wrapper function do?

**Interview Answer**

A wrapper function contains the additional logic and calls the original function before, after, or around its execution.

---

## 3. Is `@decorator` required?

**Interview Answer**

No. It is only syntactic sugar. A decorator can also be applied manually using:

```python
function = decorator(function)
```

---

## 4. Why are decorators useful?

**Interview Answer**

Decorators allow reusable behaviors such as logging, validation, timing, authentication, and exception handling to be added without changing the original function.

## 5. Does a decorator modify the original function?

**Interview Answer**

No. A decorator does not modify the original function's source code. It creates a new wrapper function that adds additional behavior, calls the original function, and returns the wrapper. The original function is then replaced by the wrapper reference.

---

# Key Takeaways

* Decorators receive functions.
* Decorators return functions.
* Wrapper functions contain additional behavior.
* `@decorator` is a shortcut for `function = decorator(function)`.
* The original function remains unchanged.

---

# Module Summary

This module introduced the structure of a Python decorator. You learned that a decorator wraps an existing function inside another function, allowing reusable behavior to be added without modifying the original implementation. You also saw that the `@` syntax is simply a more readable way of applying a decorator.

---

# Knowledge Check

1. What is a decorator?
2. What is the purpose of the wrapper function?
3. Why do decorators return a function instead of executing it immediately?
4. What is the difference between:

   * `logger(welcome)`
   * `logger(welcome())`
5. Why is `@logger` called syntactic sugar?
6. What happens internally when Python encounters `@logger`?

---

# Practical Exercise

Create:

```text
exercises/exercise-06.py
```

### Requirement

Create a decorator named:

```python
logger
```

It should:

* Print **"Function Started"**
* Execute the original function
* Print **"Function Completed"**

Decorate the following functions:

```python
create_user()
update_user()
delete_user()
```

Expected output for:

```python
create_user()
```

```text
Function Started
Creating User...
Function Completed
```

Apply the same decorator to all three functions without duplicating the logging code.
