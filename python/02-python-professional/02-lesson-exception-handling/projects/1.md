# 📘 Lesson 12 – Capstone Project Overview

## Project Name

**ATM Banking System (Console Application)**

---

# Estimated Time

| Activity              | Time      |
| --------------------- | --------- |
| Project Explanation   | 20 min    |
| Coding                | 60–90 min |
| Review & Improvements | 30 min    |
| Interview Questions   | 20 min    |

**Total:** ~2 hours

---

# Difficulty

⭐⭐⭐☆☆ (Intermediate)

---

# What We'll Build

A menu-driven ATM system.

```
========================
      ATM SYSTEM
========================

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Choose:
```

---

# Features

### Core Features

* ✅ Check Balance
* ✅ Deposit
* ✅ Withdraw
* ✅ Exit

---

### Validation

* Negative deposit not allowed
* Deposit of zero not allowed
* Negative withdrawal not allowed
* Withdraw more than balance not allowed
* Invalid menu option
* Invalid numeric input

---

### Exception Handling

* try
* except
* else
* finally
* raise
* Custom Exceptions

---

### OOP Concepts

* Class
* Object
* Constructor
* Encapsulation
* Methods
* Custom Exception Classes

---

# Concepts Used

| Topic                  | Used |
| ---------------------- | ---- |
| Class                  | ✅    |
| Object                 | ✅    |
| Constructor            | ✅    |
| Methods                | ✅    |
| Encapsulation          | ✅    |
| Exception Handling     | ✅    |
| raise                  | ✅    |
| Custom Exception       | ✅    |
| Loops                  | ✅    |
| Conditional Statements | ✅    |

---

# Final Output

Example

```
========= ATM =========

1.Check Balance
2.Deposit
3.Withdraw
4.Exit

Choose :

2

Enter Amount :
500

Deposit Successful

Current Balance : 5500
```

---

# How We'll Build It

We'll build it exactly like a real developer.

Instead of writing everything at once, we'll go step by step.

```
Step 1
↓

Create Custom Exceptions

↓

Step 2

Create ATM Class

↓

Step 3

Create Deposit Method

↓

Step 4

Create Withdraw Method

↓

Step 5

Check Balance

↓

Step 6

Menu System

↓

Step 7

Testing

↓

Step 8

Code Improvement
```

This is how projects are developed in real companies.

---

# Project Structure

```
atm.py

│

├── Custom Exceptions

│

├── ATM Class

│      __init__()

│      deposit()

│      withdraw()

│      check_balance()

│

└── Main Menu
```

---

# Step 1 – Create Custom Exceptions

First create three custom exceptions.

```python
class InvalidAmountError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


class InvalidChoiceError(Exception):
    pass
```

---

## Why Three Exceptions?

### InvalidAmountError

For

```
Deposit = -100

Withdraw = -50

Deposit = 0
```

---

### InsufficientBalanceError

```
Balance = 5000

Withdraw = 7000
```

---

### InvalidChoiceError

```
Menu

1

2

3

4

User enters

9
```

---

# Mini Exercise 1

Create only these three classes.

```python
class InvalidAmountError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


class InvalidChoiceError(Exception):
    pass
```

Nothing else.

---

# Interview Question ⭐

**Q. Why are we creating three exceptions instead of only one?**

**Answer:**

Because each exception represents a different business rule:

* `InvalidAmountError` → Invalid deposit/withdrawal amount.
* `InsufficientBalanceError` → Withdrawal exceeds available balance.
* `InvalidChoiceError` → User selected an invalid menu option.

This makes the code easier to understand, maintain, and handle appropriately.

---

# Coding Standard (From This Project Onward)

Starting with this project, we'll follow professional coding standards:

* Meaningful class names (`ATM`, `InvalidAmountError`)
* Meaningful method names (`deposit`, `withdraw`, `check_balance`)
* Small methods with one responsibility
* Clear exception names
* Consistent formatting
* Input validation before business logic
* Comments only where they add value (avoid obvious comments)

This is the style you'll see in production Python code.

---

# Lesson Progress

```
Lesson 12

Theory
████████████████████ 100% ✅

Project
█□□□□□□□□□□□□□□□ 10%
```

---

## 📝 Your Task

Create **only** these three custom exception classes:

```python
class InvalidAmountError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


class InvalidChoiceError(Exception):
    pass
```

Paste the code here.

Once I review it (it will be quick), we'll move to **Step 2 – Creating the `ATM` class**, where we'll start building the actual application. We will not skip any steps, so you'll understand how a real-world project grows from a simple class into a complete application.
