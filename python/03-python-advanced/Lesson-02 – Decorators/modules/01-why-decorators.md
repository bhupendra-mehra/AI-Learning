# Module 01 – Why Decorators?

## Module Overview

Before learning the syntax of decorators, it's important to understand **why Python introduced them**.

Decorators were created to solve one of the most common problems in software development: **code duplication**.

As applications grow, many functions require additional behavior such as logging, authentication, validation, exception handling, caching, or performance monitoring. Copying this code into every function leads to repetition, poor maintainability, and harder debugging.

Decorators solve this by allowing reusable behavior to be written once and applied to many functions without modifying the original function.

---

# Learning Objectives

After completing this module, you will be able to:

* Explain why decorators exist.
* Define code duplication.
* Understand cross-cutting concerns.
* Recognize situations where decorators should be used.
* Explain the benefits of decorators in production applications.

---

# The Problem Without Decorators

Suppose an application contains three functions.

```python
def create_order():
    print("Order Created")


def update_order():
    print("Order Updated")


def delete_order():
    print("Order Deleted")
```

Everything looks good.

Now your team lead asks you to log every function execution.

You modify every function.

```python
def create_order():
    print("[LOG] create_order() called")
    print("Order Created")


def update_order():
    print("[LOG] update_order() called")
    print("Order Updated")


def delete_order():
    print("[LOG] delete_order() called")
    print("Order Deleted")
```

Now another requirement arrives.

> Measure execution time.

Now every function becomes:

```python
start_timer()

print("[LOG] Function Started")

# Business Logic

stop_timer()
```

Then another requirement:

* Authentication
* Authorization
* Exception Handling
* Input Validation

Soon every function looks like this:

```text
Authentication

↓

Logging

↓

Timing

↓

Validation

↓

Business Logic

↓

Exception Handling
```

The actual business logic becomes difficult to identify.

---

# Code Duplication

Code duplication means writing the same logic repeatedly in multiple places.

Example:

```python
def login():
    print("[LOG] Function Started")
    print("User Logged In")


def logout():
    print("[LOG] Function Started")
    print("User Logged Out")
```

The logging code is duplicated.

If tomorrow the logging format changes, every function must be modified.

This increases:

* Maintenance effort
* Bug risk
* Development time

---

# Cross-Cutting Concerns

Some functionality is required by many different parts of an application.

These are called **cross-cutting concerns**.

Examples:

* Logging
* Authentication
* Authorization
* Validation
* Exception Handling
* Performance Monitoring
* Retry Logic
* Caching
* Auditing

These concerns "cut across" multiple business functions.

Decorators allow these concerns to remain separate from the business logic.

---

# Before and After Decorators

Without decorators:

```text
create_order()

├── Authentication
├── Logging
├── Timing
├── Validation
├── Business Logic
└── Error Handling
```

With decorators:

```text
@authenticate

@log_execution

@measure_time

@validate

↓

create_order()

↓

Business Logic Only
```

The business function becomes much cleaner.

---

# Real-World Example – Magento

Suppose you create a custom export feature.

```python
def export_products():
```

The function should only export products.

Instead, it often contains:

* Permission checks
* Logging
* Error handling
* Timing
* Validation

Using decorators:

```python
@permission_required

@log_execution

@measure_execution_time

def export_products():
```

The function focuses only on exporting products.

---

# Real-World Example – FastAPI

One of the most common decorators you'll encounter is:

```python
@app.get("/products")
def get_products():
    ...
```

This tells FastAPI:

> Register this function as a GET API endpoint.

Without decorators, registering routes would require much more manual code.

---

# Real-World Example – PyTest

```python
@pytest.mark.slow
def test_export():
    ...
```

This marks the test as a slow-running test.

Again, this behavior is added without changing the function itself.

---

# Real-World Example – AI

Later in the roadmap, we'll create decorators for:

* Logging LLM prompts.
* Measuring OpenAI response time.
* Counting API usage.
* Validating AI tool inputs.
* Recording conversation history.

---

# Benefits of Decorators

Decorators provide several advantages:

* Eliminate duplicate code.
* Improve readability.
* Improve maintainability.
* Encourage reusable code.
* Separate business logic from infrastructure logic.
* Make testing easier.

---

# Best Practices

* Use decorators for reusable behavior.
* Keep decorators focused on one responsibility.
* Name decorators clearly.
* Avoid placing business logic inside decorators.
* Reuse decorators across multiple modules.

---

# Common Mistakes

## Decorating Everything

Not every function needs a decorator.

Use decorators only when behavior is shared.

---

## Mixing Responsibilities

Incorrect:

```text
Decorator

↓

Authentication

↓

Database Update

↓

Business Calculation
```

A decorator should not perform unrelated business operations.

---

## Ignoring Readability

Five or six stacked decorators may make code difficult to understand.

Keep decorator usage intentional.

---

# Interview Questions & Answers

## 1. What problem do decorators solve?

**Interview Answer**

Decorators eliminate duplicate code by allowing reusable functionality such as logging, authentication, validation, and performance monitoring to be written once and applied to multiple functions.

---

## 2. What are cross-cutting concerns?

**Interview Answer**

Cross-cutting concerns are functionalities shared across multiple parts of an application, such as logging, authentication, authorization, validation, exception handling, caching, and monitoring.

---

## 3. Why are decorators better than copy-pasting code?

**Interview Answer**

Decorators centralize reusable logic, making applications easier to maintain, test, and extend while reducing duplication and improving readability.

---

## 4. Give some real-world examples of decorators.

**Interview Answer**

FastAPI route registration, Django authentication, Flask routing, PyTest markers, logging, caching, retry mechanisms, and execution time measurement.

---

## Key Takeaways

* Decorators solve code duplication.
* They separate reusable logic from business logic.
* Cross-cutting concerns belong in decorators.
* Decorators improve maintainability and readability.
* Modern Python frameworks rely heavily on decorators.

---

# Module Summary

This module focused on the motivation behind decorators rather than their implementation. By understanding the problems of duplicated code and cross-cutting concerns, you now have the foundation needed to appreciate how decorators improve software design. In the next module, you'll learn **nested functions**, the first technical building block required to create decorators.

---

# Exercises

## Exercise 01

Create:

```text
exercises/exercise-01.py
```

Write three functions:

* `create_user()`
* `update_user()`
* `delete_user()`

Add the same logging statement inside each function.

Observe the duplicated code.

---

## Exercise 02

Modify the above functions by adding:

* Logging
* Start message
* End message
* Error message (just print it; don't use exception handling yet)

Notice how much duplication is introduced.

---

## Exercise 03

Create:

```text
exercises/exercise-03.py
```

Write **150–200 words** explaining:

1. What is code duplication?
2. What are cross-cutting concerns?
3. Why are decorators useful?
4. Give one real-world example from Magento, FastAPI, or AI.
