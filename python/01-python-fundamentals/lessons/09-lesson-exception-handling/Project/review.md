> **Refactor and improve the code.**

This is the step many tutorials skip, but it's where developers learn to write **maintainable** code instead of just **working** code.

---

# 🏦 ATM Banking System

# Step 7 – Code Refactoring & Professional Improvements

**Estimated Time:** 20–25 minutes

---

# Improvement 1 – Remove Global `atm`

Currently your `Menu` class depends on a global variable:

```python
atm = ATM()

menu = Menu()

menu.options()
```

Inside `Menu`:

```python
atm.deposit(amount)
```

This works, but it's not good design.

---

## Better Design

Pass the `ATM` object into the `Menu`.

```python
class Menu:

    def __init__(self, atm):
        self.atm = atm
```

Now use:

```python
self.atm.deposit(amount)
```

instead of

```python
atm.deposit(amount)
```

---

## Create Objects

```python
atm = ATM()

menu = Menu(atm)

menu.options()
```

This is called **Dependency Injection**.

---

# Why is this better?

Suppose tomorrow you create

```python
class BankATM(ATM):
```

or

```python
class MockATM
```

for testing.

You can simply do

```python
menu = Menu(MockATM())
```

No code inside `Menu` changes.

This is exactly how enterprise applications like **Django**, **FastAPI**, and **Magento** are designed.

---

# Improvement 2 – Separate Display Logic

Instead of

```python
print("Deposit Successful")
```

inside

```python
deposit()
```

prefer

```python
deposit()
```

returns successfully.

Then

```python
print("Deposit Successful")
```

inside the menu.

### Why?

Methods should perform **business logic**, while the menu handles **user interaction**.

---

# Improvement 3 – Avoid Duplicate Code

Currently

```python
amount = float(input(...))
```

appears twice.

Instead

```python
if selected_option in (1, 2):

    amount = float(input("Enter Amount : "))
```

Then

```python
if selected_option == 1:
    self.atm.deposit(amount)

else:
    self.atm.withdraw(amount)
```

Less duplication.

Cleaner code.

---

# Improvement 4 – Constants

Instead of

```python
self.__balance = 5000
```

you could define

```python
INITIAL_BALANCE = 5000
```

Then

```python
self.__balance = INITIAL_BALANCE
```

Large applications avoid "magic numbers."

---

# Improvement 5 – Method Naming

Good

```python
deposit()

withdraw()

check_balance()
```

Avoid

```python
doDeposit()

depositMoney()

balanceChecking()
```

Simple, descriptive names are preferred.

---

# Improvement 6 – Docstrings

Professional Python code often includes docstrings.

Example

```python
def deposit(self, amount):
    """Deposit money into the account."""
```

These help IDEs and documentation tools.

---

# Final Project Structure

```text
atm.py
│
├── Custom Exceptions
│
├── ATM
│      __init__()
│      deposit()
│      withdraw()
│      check_balance()
│
├── Menu
│      __init__()
│      options()
│
└── main()
```

---

# Instead of Running Everything Here

Rather than placing object creation at the bottom:

```python
atm = ATM()

menu = Menu(atm)

menu.options()
```

Professional Python uses

```python
def main():

    atm = ATM()

    menu = Menu(atm)

    menu.options()
```

Then

```python
if __name__ == "__main__":
    main()
```

---

# Why?

Suppose another file imports your ATM.

```python
from atm import ATM
```

Without

```python
if __name__ == "__main__":
```

the menu starts automatically.

That's undesirable.

This statement prevents that.

---

# Interview Question ⭐

### What does

```python
if __name__ == "__main__":
```

mean?

**Answer**

When a Python file is executed directly, `__name__` is set to `"__main__"`.

When the file is imported into another module, `__name__` is set to the module's name.

This allows us to execute application code only when the file is run directly.

---

# Mini Example

```python
def greet():
    print("Hello")


def main():
    greet()


if __name__ == "__main__":
    main()
```

Run directly:

```text
Hello
```

Import into another file:

```python
from demo import greet
```

Only `greet` is imported. The `main()` function does not execute.

---

# What You Have Learned in This Project

✅ Classes

✅ Objects

✅ Constructors

✅ Private Variables

✅ Encapsulation

✅ Methods

✅ Custom Exceptions

✅ `raise`

✅ `try`

✅ `except`

✅ `else`

✅ `finally`

✅ Business Rules

✅ Menu-driven Programs

✅ Dependency Injection (basic)

✅ Code Refactoring

✅ `main()` Function

✅ `if __name__ == "__main__":`

---

# 🎓 Lesson 12 Complete

```text
Lesson 12 – Exception Handling

██████████████████████████ 100% ✅

Theory          ✅
Exercises       ✅
Project         ✅
Refactoring     ✅
Interview Prep  ✅
```

---

# 📊 Roadmap Progress

```text
Python for AI Roadmap

Phase 1 – Python Programming

Lesson 1   ✅
Lesson 2   ✅
Lesson 3   ✅
Lesson 4   ✅
Lesson 5   ✅
Lesson 6   ✅
Lesson 7   ✅
Lesson 8   ✅
Lesson 9   ✅
Lesson 10  ✅
Lesson 11  ✅ OOP
Lesson 12  ✅ Exception Handling

▶ Next: Lesson 13 – File Handling
```

---

# 📘 Preview – Lesson 13

Before we start Lesson 13 (following your preferred workflow), I'll first provide the complete overview including:

* Estimated time
* Modules
* Mini projects
* Real-world applications
* AI relevance
* Magento relevance
* Interview importance
* Final project

and then wait for your confirmation before starting.

## 🎉 Congratulations!

This is a significant milestone. With Lessons **11 (OOP)** and **12 (Exception Handling)** completed, you've covered two of the most important foundations of professional Python development. These concepts will be used repeatedly in upcoming lessons on file handling, databases, APIs, and AI agent development.
