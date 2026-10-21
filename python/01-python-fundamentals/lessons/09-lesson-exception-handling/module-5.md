# 📘 Lesson 12 – Module 5

# Custom Exceptions

**Estimated Time:** 40–45 minutes

---

# Learning Objectives

By the end of this module, you'll be able to:

* ✅ Understand why custom exceptions are needed.
* ✅ Create your own exception classes.
* ✅ Raise custom exceptions.
* ✅ Handle custom exceptions.
* ✅ Build cleaner, more maintainable applications.
* ✅ Understand how frameworks like Magento, Django, and FastAPI use custom exceptions.

---

# Recap

So far, we've used Python's built-in exceptions:

```python
ValueError
TypeError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError
```

These are useful for general programming errors.

But what about **business errors**?

Example:

* Customer already exists.
* Product is out of stock.
* Insufficient balance.
* User is under 18.
* Coupon expired.

Python doesn't have built-in exceptions for these.

So we create our own.

---

# Why Do We Need Custom Exceptions?

Imagine an ATM.

```python
balance = 5000

withdraw = 7000
```

You could write:

```python
raise ValueError("Insufficient Balance")
```

This works.

But think like a developer maintaining this code six months later.

Does this tell you **what kind of error** occurred?

Not really.

Instead, you could write:

```python
raise InsufficientBalanceError("Insufficient Balance")
```

Now the exception itself clearly describes the problem.

---

# What is a Custom Exception?

A custom exception is simply a class that inherits from `Exception`.

```python
class MyError(Exception):
    pass
```

That's it.

You have created your own exception.

---

# Creating Your First Custom Exception

```python
class InvalidAgeError(Exception):
    pass
```

Now you can use it.

```python
age = 15

if age < 18:
    raise InvalidAgeError("Minimum age is 18.")
```

Output

```text
InvalidAgeError: Minimum age is 18.
```

Notice:

Python displays **your class name**, not `ValueError`.

---

# Complete Example

```python
class InvalidAgeError(Exception):
    pass

try:

    age = int(input("Enter Age : "))

    if age < 18:
        raise InvalidAgeError("Minimum age is 18.")

    print("Registration Successful")

except InvalidAgeError as e:

    print(e)
```

---

### Input

```text
15
```

Output

```text
Minimum age is 18.
```

---

### Input

```text
20
```

Output

```text
Registration Successful
```

---

# Why Not Just Use ValueError?

Let's compare.

### Option 1

```python
raise ValueError("Age must be 18.")
```

When another developer reads the code, they only know:

> Some value is wrong.

---

### Option 2

```python
raise InvalidAgeError("Age must be 18.")
```

Now they immediately know:

> The business rule related to age failed.

This makes debugging and maintenance easier.

---

# ATM Example

```python
class InsufficientBalanceError(Exception):
    pass
```

Now:

```python
balance = 5000

withdraw = 7000

if withdraw > balance:
    raise InsufficientBalanceError("Insufficient Balance")
```

Output

```text
Insufficient Balance
```

---

# E-Commerce Example

```python
class OutOfStockError(Exception):
    pass
```

```python
stock = 2

order = 5

if order > stock:
    raise OutOfStockError("Product Out Of Stock")
```

---

# Login Example

```python
class InvalidPasswordError(Exception):
    pass
```

```python
password = input("Password : ")

if len(password) < 8:
    raise InvalidPasswordError(
        "Password must contain at least 8 characters."
    )
```

---

# AI Example

Imagine you're building an AI chatbot.

```python
class EmptyPromptError(Exception):
    pass
```

```python
prompt = input("Prompt : ")

if prompt.strip() == "":
    raise EmptyPromptError("Prompt cannot be empty.")
```

This is much clearer than raising a generic `ValueError`.

---

# Magento Comparison

You've probably seen exceptions like:

```php
NoSuchEntityException

LocalizedException

InputException
```

Magento doesn't always use generic PHP exceptions.

It defines **custom exceptions** for business scenarios.

Python follows the same idea.

---

# Adding a Constructor

Sometimes we want extra information.

```python
class InvalidAgeError(Exception):

    def __init__(self, message):
        super().__init__(message)
```

Now

```python
raise InvalidAgeError("Age must be 18.")
```

works exactly as before.

At this stage, you don't need to override `__init__` unless you're storing additional information. The simple `pass` version is enough for most custom exceptions.

---

# Multiple Custom Exceptions

```python
class InvalidAgeError(Exception):
    pass


class InvalidSalaryError(Exception):
    pass


class InvalidEmailError(Exception):
    pass
```

Each exception represents a different business rule.

---

# Production Example

```python
class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient Balance"
        )

    return balance - amount


try:

    balance = withdraw(5000, 7000)

    print(balance)

except InsufficientBalanceError as e:

    print(e)
```

This is exactly how large applications structure business validation.

---

# Best Practices

### Good

```python
class ProductNotFoundError(Exception):
    pass
```

The name clearly describes the error.

---

### Avoid

```python
class Error(Exception):
    pass
```

Too vague.

---

### Use Custom Exceptions For

* Banking
* AI
* Login Systems
* Inventory
* Orders
* Payment
* Business Rules

---

### Use Built-in Exceptions For

* Invalid type
* Invalid value
* File missing
* Index out of range
* Division by zero

---

# Mini Exercise

Create a custom exception called:

```text
InvalidSalaryError
```

Rules:

1. Accept salary from the user.
2. If salary is less than **10000**, raise:

```text
Salary must be at least 10000.
```

3. Otherwise print:

```text
Salary Accepted
```

4. Handle the custom exception using `try` and `except`.

---

### Example 1

Input

```text
8000
```

Output

```text
Salary must be at least 10000.
```

---

### Example 2

Input

```text
25000
```

Output

```text
Salary Accepted
```

---

# Interview Questions

## Q1. What is a custom exception?

**Answer:** A custom exception is a user-defined exception class that inherits from `Exception` and represents application-specific or business-specific error conditions.

---

## Q2. Why do we create custom exceptions?

**Answer:** To make code more readable, expressive, and maintainable by representing specific business rule violations with meaningful exception names.

---

## Q3. What is the base class for most custom exceptions?

**Answer:**

```python
Exception
```

---

## Q4. Can a custom exception have methods and attributes?

**Answer:** Yes. Since it's a class, it can define constructors, attributes, methods, and any additional behavior needed.

---

# 🎯 Senior Developer Tip

In enterprise applications, exceptions are part of the **domain language**.

For example:

Instead of:

```python
raise ValueError("Not enough money")
```

developers write:

```python
raise InsufficientBalanceError("Not enough money")
```

When another developer reads the code, they immediately understand the business scenario without needing to inspect the message.

This becomes even more valuable in large systems with hundreds of exception types.

---

# 📈 Lesson Progress

```text
Lesson 12
│
├── ✅ Module 1 – Introduction
├── ✅ Module 2 – try & except
├── ✅ Module 3 – else & finally
├── ✅ Module 4 – raise
├── ✅ Module 5 – Custom Exceptions
├── ▶ Module 6 – Best Practices
└── ⏳ ATM Banking System Project
```

---

## 📝 Your Task

Complete the **Mini Exercise** and paste your code.

After reviewing it, we'll move to **Module 6 – Exception Handling Best Practices**, where you'll learn the patterns used by experienced Python developers in production code. That module will prepare you for the final **ATM Banking System Project**, where you'll apply everything from Lesson 12 in one complete application.
