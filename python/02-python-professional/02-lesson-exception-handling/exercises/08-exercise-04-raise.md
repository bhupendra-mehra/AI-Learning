# Your Code

```python
try:
    age = int(input("Enter your age :"))

    if age < 18:
        raise ValueError("You are not eligible to vote")

except Exception as e:
    print(e)

else:
    print("You are eligible to vote.")
```

---

# Review

## 1. Input Validation ⭐⭐⭐⭐⭐

```python
age = int(input("Enter your age :"))
```

✔ Correct.

If the user enters

```text
abc
```

Python itself raises

```text
ValueError
```

---

## 2. Using `raise` ⭐⭐⭐⭐⭐

```python
if age < 18:
    raise ValueError("You are not eligible to vote")
```

Excellent.

This is the most important concept of this module.

Notice:

Python sees

```python
15
```

as a perfectly valid integer.

It doesn't know that

> Minimum voting age is 18.

That is **your business rule**, so **you** raise the exception.

This is exactly how production applications work.

---

## 3. Exception Handling ⭐⭐⭐⭐⭐

```python
except Exception as e:
    print(e)
```

Perfect.

When

```python
raise ValueError(...)
```

executes,

Python immediately jumps here.

The output becomes

```text
You are not eligible to vote
```

---

## 4. else ⭐⭐⭐⭐⭐

```python
else:
    print("You are eligible to vote.")
```

Excellent.

This executes only if:

* Input is valid.
* No exception is raised.
* Age is 18 or above.

Exactly correct.

---

# Dry Run

## Case 1

Input

```text
16
```

Execution

```text
try
↓

age = 16

↓

age < 18

↓

raise ValueError

↓

except

↓

Print message
```

Output

```text
You are not eligible to vote
```

✔ Correct

---

## Case 2

Input

```text
20
```

Execution

```text
try

↓

age = 20

↓

Condition False

↓

else
```

Output

```text
You are eligible to vote.
```

✔ Correct

---

## Case 3

Input

```text
abc
```

Execution

```text
int("abc")

↓

Python raises ValueError

↓

except
```

Output

```text
invalid literal for int() with base 10: 'abc'
```

Also correct.

---

# One Small Improvement ⭐

You wrote

```python
except Exception as e:
```

This works.

But ask yourself:

> **What exceptions are expected in this program?**

Only:

* `ValueError` from `int()`
* `ValueError` from your own `raise`

So it's even better to write:

```python
except ValueError as e:
    print(e)
```

Why?

Because if some completely different bug occurs, you'll notice it immediately instead of accidentally hiding it.

This follows the best practice we learned in Module 2: **catch the most specific exception you expect.**

---

# Production Version

```python
try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("You are not eligible to vote.")

except ValueError as e:
    print(e)

else:
    print("You are eligible to vote.")
```

Simple, clean, and production-ready.

---

# Interview Questions

## Q1. Does `raise` always have to be inside a `try` block?

**Answer:** No.

Example:

```python
raise ValueError("Invalid Age")
```

This is valid.

However, if it's not caught by a `try/except`, the program will terminate with a traceback.

---

## Q2. Can we raise any exception?

Yes.

```python
raise TypeError("Wrong Type")

raise RuntimeError("Server Error")

raise FileNotFoundError("Missing File")
```

You can raise any exception class.

---

## Q3. Why do we use `raise` instead of just `print("Error")`?

Consider this code:

```python
if age < 18:
    print("Not Eligible")

print("Voting Started")
```

Output:

```text
Not Eligible
Voting Started
```

Even after detecting an invalid condition, the program continues.

Now with `raise`:

```python
if age < 18:
    raise ValueError("Not Eligible")

print("Voting Started")
```

The second line never executes because the exception stops normal execution.

That's why `raise` is much more powerful than simply printing an error.

---

# Score

| Topic              | Score |
| ------------------ | ----: |
| Input Validation   | ⭐⭐⭐⭐⭐ |
| raise              | ⭐⭐⭐⭐⭐ |
| Business Logic     | ⭐⭐⭐⭐⭐ |
| else               | ⭐⭐⭐⭐⭐ |
| Exception Handling | ⭐⭐⭐⭐☆ |

## Overall Score

**9.9/10** ⭐⭐⭐⭐⭐

The only improvement is using `except ValueError as e:` instead of `except Exception as e:` since `ValueError` is the only expected exception here.

---

# Lesson Progress

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

## Before We Continue

A quick observation about your progress:

In the last few lessons (OOP and Exception Handling), you're consistently scoring **9.5–10/10** on the exercises. That tells me you've understood the core concepts rather than just copying the syntax.

Because of that, from the next module onward I'll start including a few more **production-style scenarios** (similar to Magento and AI projects) in addition to the basic examples. That way you'll not only learn Python syntax but also develop the problem-solving skills you'll need for AI Agent Engineering and backend development.

Next, we'll start **Module 5 – Custom Exceptions**, where you'll learn how to create your own exception classes like `InsufficientBalanceError`, `InvalidAgeError`, or `ProductNotFoundError`—a pattern you'll see in large Python applications and frameworks.
