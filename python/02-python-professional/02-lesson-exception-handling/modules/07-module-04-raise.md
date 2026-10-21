# 📘 Lesson 12 – Module 4

# `raise` Statement

**Estimated Time:** 30–35 minutes

---

# Learning Objectives

By the end of this module, you'll understand:

* ✅ What is `raise`?
* ✅ Why do we intentionally raise exceptions?
* ✅ Built-in exceptions with `raise`
* ✅ Custom error messages
* ✅ Input validation
* ✅ Business rule validation
* ✅ Difference between `raise` and `return`
* ✅ Production use cases

---

# What is `raise`?

Until now, you've been **catching** exceptions.

Example:

```python
try:
    number = int(input())

except ValueError:
    print("Invalid Number")
```

Here,

Python created the exception automatically.

But what if **you** want to create an exception?

That's where `raise` comes in.

---

# Definition

`raise` means:

> **"Stop execution and throw an exception manually."**

Think of it as pressing an emergency stop button.

```text
Condition Failed
      │
      ▼
 raise Exception
      │
      ▼
 Program jumps to except
```

---

# Why Do We Need `raise`?

Imagine you're creating a banking application.

User enters:

```text
Withdraw Amount : -500
```

Technically,

```python
-500
```

is a valid integer.

So Python **won't** raise an exception.

But from a business perspective,

negative withdrawal is invalid.

We need to stop the program ourselves.

---

# Example Without `raise`

```python
amount = int(input("Enter Amount : "))

print("Processing...")
```

Input

```text
-500
```

Output

```text
Processing...
```

Wrong!

---

# Example With `raise`

```python
amount = int(input("Enter Amount : "))

if amount < 0:
    raise ValueError("Amount cannot be negative.")

print("Processing...")
```

Input

```text
-500
```

Output

```text
ValueError: Amount cannot be negative.
```

Now the invalid data is rejected.

---

# How `raise` Works

```python
age = int(input("Age : "))

if age < 18:
    raise ValueError("Age must be at least 18.")

print("Eligible")
```

---

### Input

```text
15
```

Output

```text
ValueError: Age must be at least 18.
```

---

### Input

```text
20
```

Output

```text
Eligible
```

---

# `raise` with `try`

Usually, `raise` is combined with exception handling.

```python
try:

    age = int(input("Age : "))

    if age < 18:
        raise ValueError("Age must be at least 18.")

    print("Registration Successful")

except ValueError as e:

    print(e)
```

---

### Input

```text
16
```

Output

```text
Age must be at least 18.
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

# Raising Different Exceptions

You are not limited to `ValueError`.

---

## TypeError

```python
raise TypeError("Only strings are allowed.")
```

---

## IndexError

```python
raise IndexError("Invalid Position")
```

---

## KeyError

```python
raise KeyError("Customer ID Missing")
```

---

## RuntimeError

```python
raise RuntimeError("Unknown Server Error")
```

---

# Business Rule Example

Suppose you're developing an e-commerce application.

```python
quantity = int(input("Quantity : "))

if quantity <= 0:
    raise ValueError("Quantity must be greater than zero.")

print("Order Placed")
```

Python won't detect this automatically because `0` is a valid integer.

The business rule is yours to enforce.

---

# ATM Example

```python
balance = 5000

withdraw = int(input("Withdraw Amount : "))

if withdraw > balance:
    raise ValueError("Insufficient Balance")

balance -= withdraw

print(balance)
```

Input

```text
7000
```

Output

```text
ValueError: Insufficient Balance
```

---

# AI Example

Suppose you're building an AI chatbot.

```python
prompt = input("Prompt : ")

if prompt.strip() == "":
    raise ValueError("Prompt cannot be empty.")
```

This prevents invalid requests from reaching the AI model.

---

# Magento Example

Imagine a custom validation before placing an order.

```php
if ($qty <= 0) {
    throw new \Magento\Framework\Exception\LocalizedException(
        __("Quantity must be greater than zero.")
    );
}
```

PHP uses `throw`, while Python uses `raise`, but the purpose is the same.

---

# `raise` vs `return`

This is a common interview question.

| `return`                        | `raise`                                         |
| ------------------------------- | ----------------------------------------------- |
| Returns a value to the caller   | Stops execution by throwing an exception        |
| Indicates successful completion | Indicates an error or invalid condition         |
| Flow continues normally         | Flow jumps to an exception handler (if present) |

---

### Example of `return`

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

Output

```text
30
```

---

### Example of `raise`

```python
def withdraw(balance, amount):

    if amount > balance:
        raise ValueError("Insufficient Balance")

    return balance - amount

print(withdraw(5000, 7000))
```

Output

```text
ValueError: Insufficient Balance
```

---

# Real Production Example

```python
def register_user(age):

    if age < 18:
        raise ValueError("User must be at least 18 years old.")

    print("Registration Successful")
```

Notice how the function immediately rejects invalid input instead of continuing with incorrect data.

---

# Best Practices

### ✔ Use `raise` for business rules.

Examples:

* Minimum age
* Maximum withdrawal
* Empty username
* Invalid order quantity
* Negative price

---

### ❌ Don't use `raise` for conditions Python already checks automatically.

Example:

```python
10 / 0
```

Python already raises `ZeroDivisionError`, so you don't need to.

---

# Mini Exercise

Create a program that:

1. Accepts a user's age.
2. If age is less than **18**, raise a `ValueError` with the message:

```text
You are not eligible to vote.
```

3. Otherwise print:

```text
You are eligible to vote.
```

4. Use `try` and `except` to handle the exception and display the message.

---

### Example 1

Input

```text
16
```

Output

```text
You are not eligible to vote.
```

---

### Example 2

Input

```text
22
```

Output

```text
You are eligible to vote.
```

---

# Interview Questions

### Q1. What is the purpose of `raise`?

**Answer:** `raise` is used to manually throw an exception when your code detects an invalid condition or business rule violation.

---

### Q2. When should you use `raise`?

**Answer:** Use it when the program detects invalid input or a business rule violation that Python cannot detect automatically.

---

### Q3. What is the difference between `raise` and `return`?

| `raise`                | `return`                       |
| ---------------------- | ------------------------------ |
| Throws an exception    | Returns a value                |
| Stops normal execution | Ends the function successfully |
| Used for errors        | Used for successful results    |

---

# 💡 Senior Developer Tip

One of the biggest differences between **beginner** and **professional** developers is this:

* Beginners write code that **assumes** inputs are correct.
* Professionals **validate inputs first**, and if something is invalid, they `raise` an exception immediately.

This is called **"Fail Fast"**.

Instead of letting invalid data travel through the application and cause problems later, you stop it at the earliest possible point.

For example:

```python
def create_order(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    # Safe to continue
    print("Order created")
```

This pattern is used extensively in production systems because it makes bugs easier to find and prevents corrupted data from spreading.

---

# 📈 Lesson Progress

```text
Lesson 12
│
├── ✅ Module 1 – Introduction
├── ✅ Module 2 – try & except
├── ✅ Module 3 – else & finally
├── ✅ Module 4 – raise
├── ▶ Module 5 – Custom Exceptions
├── ⏳ Module 6 – Best Practices
└── ⏳ ATM Banking System Project
```

---

## 📝 Your Task

Complete the **Mini Exercise** and paste your code here.

After reviewing it, we'll move to **Module 5 – Custom Exceptions**, where you'll learn how to create your own exception classes instead of relying only on Python's built-in exceptions. This is a common technique in large applications and frameworks.
