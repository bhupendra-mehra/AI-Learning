# Your Code

```python
class InvalidSalaryError(Exception):
    pass

try:
    salary = float(input("Enter your salary :"))

    if salary < 10000:
        raise InvalidSalaryError("Salary must be at least 10000.")

except ValueError as e:
    print(e)

else:
    print("Salary Accepted")
```

---

# Review

## 1. Custom Exception Class ⭐⭐⭐⭐⭐

```python
class InvalidSalaryError(Exception):
    pass
```

✅ Perfect.

This is exactly how we create a custom exception.

---

## 2. Raising Exception ⭐⭐⭐⭐⭐

```python
raise InvalidSalaryError("Salary must be at least 10000.")
```

Excellent.

You correctly used your custom exception instead of `ValueError`.

This is exactly what professionals do.

---

# The Mistake ❌

You wrote

```python
except ValueError as e:
```

But...

What exception are you raising?

```python
InvalidSalaryError
```

Not

```python
ValueError
```

So this block **will not catch** your custom exception.

---

## What happens?

Input

```text
5000
```

Execution

```
salary = 5000

↓

raise InvalidSalaryError

↓

except ValueError ❌

↓

No Matching except

↓

Program crashes
```

Output

```text
InvalidSalaryError: Salary must be at least 10000.
```

---

# Correct Code

```python
class InvalidSalaryError(Exception):
    pass

try:

    salary = float(input("Enter your salary : "))

    if salary < 10000:
        raise InvalidSalaryError(
            "Salary must be at least 10000."
        )

except InvalidSalaryError as e:

    print(e)

else:

    print("Salary Accepted")
```

Now

Input

```text
5000
```

Output

```text
Salary must be at least 10000.
```

Exactly as expected.

---

# Even Better ⭐⭐⭐⭐⭐

What if the user enters

```text
abc
```

Then

```python
float("abc")
```

raises

```python
ValueError
```

So a production version should handle **both** exceptions.

```python
class InvalidSalaryError(Exception):
    pass

try:

    salary = float(input("Enter your salary : "))

    if salary < 10000:
        raise InvalidSalaryError(
            "Salary must be at least 10000."
        )

except ValueError:
    print("Please enter a valid salary.")

except InvalidSalaryError as e:
    print(e)

else:
    print("Salary Accepted")
```

This handles:

* Invalid numeric input (`ValueError`)
* Business rule violation (`InvalidSalaryError`)

---

# Visual Understanding

Think of it like inheritance.

```
Exception
│
├── ValueError
│
├── TypeError
│
└── InvalidSalaryError   ← Your own exception
```

When you write

```python
except ValueError:
```

Python only catches this branch.

```
Exception
│
└── ValueError  ✅
```

But your exception lives in a different branch.

```
Exception
│
└── InvalidSalaryError  ❌
```

So it isn't caught.

---

# Interview Question ⭐

Suppose the interviewer asks:

> **Why didn't `except ValueError` catch `InvalidSalaryError`?**

Good answer:

> "Because `InvalidSalaryError` directly inherits from `Exception`, not from `ValueError`. Exception handling is based on the class hierarchy, so only matching exception types or their parent classes are caught."

That answer demonstrates a solid understanding of exception inheritance.

---

# Score

| Topic              | Score |
| ------------------ | ----: |
| Custom Exception   | ⭐⭐⭐⭐⭐ |
| raise              | ⭐⭐⭐⭐⭐ |
| Business Logic     | ⭐⭐⭐⭐⭐ |
| Exception Handling | ⭐⭐⭐☆☆ |
| Overall            | ⭐⭐⭐⭐☆ |

## Overall Score

**9.2/10** 🎉

The only issue was catching the wrong exception type. The logic and structure were otherwise excellent.

---

# 🧠 One Extra Interview Concept

Consider this code:

```python
class InvalidSalaryError(Exception):
    pass

try:
    raise InvalidSalaryError("Salary Error")

except Exception as e:
    print(e)
```

**Question:** Will this work?

**Answer:** ✅ Yes.

Why?

Because:

```
Exception
    ▲
    │
InvalidSalaryError
```

`Exception` is the **parent class**, so it catches all exceptions that inherit from it, including your custom exception.

However, in production code, it's better to catch the **most specific exception** when you know exactly what you're expecting.

---

## Lesson Progress

```
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

You're doing very well. I can also see your thinking has changed: instead of just writing code that works, you're now starting to think about **what kind of error should be raised** and **who should handle it**. That's an important step toward writing production-quality software.
