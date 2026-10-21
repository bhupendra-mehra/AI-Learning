# Your Code

```python
try:
    number1 = int(input("Enter first number : "))
    number2 = int(input("Enter second number : "))
    print(number1 / number2)

except ValueError:
    print("Invalid Number")

except ZeroDivisionError:
    print("Division by Zero")

except Exception as e:
    print(type(e))
    print(e)

print("Program Ended Successfully")
```

---

# Review

## 1. `try` Block ✅

```python
try:
```

Perfect.

Only the code that might fail is inside the `try` block.

✔ Correct practice.

---

## 2. `ValueError` ✅

```python
except ValueError:
    print("Invalid Number")
```

Excellent.

This handles inputs like:

```
abc
```

instead of

```
100
```

---

## 3. `ZeroDivisionError` ✅

```python
except ZeroDivisionError:
    print("Division by Zero")
```

Correct.

Input:

```
10
0
```

Output:

```
Division by Zero
```

---

## 4. Generic Exception ✅

```python
except Exception as e:
```

Excellent.

You placed it **after** the specific exceptions.

This is exactly how professionals write exception handling.

---

## 5. Program Continues ✅

```python
print("Program Ended Successfully")
```

Excellent.

No matter what happens,

this line executes.

---

# One Missing Requirement ⭐

The exercise asked:

> Print the actual error message using `Exception as e`.

Currently,

```python
except ValueError:
    print("Invalid Number")
```

doesn't print

```
invalid literal for int()...
```

Similarly,

```python
except ZeroDivisionError:
```

doesn't print

```
division by zero
```

---

## Better Version

You can capture the exception object in the specific handlers too.

```python
except ValueError as e:
    print("Invalid Number")
    print(e)

except ZeroDivisionError as e:
    print("Division by Zero")
    print(e)
```

Now you'll get:

```
Division by Zero

division by zero
```

or

```
Invalid Number

invalid literal for int() with base 10: 'abc'
```

---

# Another Small Improvement

Instead of

```python
print(number1/number2)
```

use

```python
result = number1 / number2

print(f"Result : {result}")
```

Professional code is usually easier to extend.

Example:

```python
result = number1 / number2

database.save(result)
```

---

# Production Version

```python
try:
    number1 = int(input("Enter First Number : "))
    number2 = int(input("Enter Second Number : "))

    result = number1 / number2

    print(f"Result : {result}")

except ValueError as e:
    print("Invalid Number")
    print(e)

except ZeroDivisionError as e:
    print("Division by Zero")
    print(e)

except Exception as e:
    print(type(e))
    print(e)

print("Program Ended Successfully")
```

---

# Interview Questions

### Q1. Why do we write

```python
except Exception as e
```

instead of

```python
except Exception
```

**Answer**

Because `e` stores the actual exception object, allowing us to inspect or log details such as the error message and exception type.

---

### Q2. Why should `Exception` always be the last `except` block?

**Answer**

Because it is the parent class of most application exceptions. If it appears first, it will catch errors like `ValueError` and `ZeroDivisionError`, preventing their specific handlers from running.

---

### Q3. Is this correct?

```python
except:
```

**Answer**

Technically yes, but it's generally discouraged because it catches almost everything, including unexpected programming errors, making debugging harder. Prefer catching specific exceptions or `Exception` explicitly.

---

# Score

| Topic                  | Score |
| ---------------------- | ----: |
| try                    | ⭐⭐⭐⭐⭐ |
| ValueError             | ⭐⭐⭐⭐⭐ |
| ZeroDivisionError      | ⭐⭐⭐⭐⭐ |
| Generic Exception      | ⭐⭐⭐⭐⭐ |
| Exception Order        | ⭐⭐⭐⭐⭐ |
| Error Message Handling | ⭐⭐⭐⭐☆ |
| Code Quality           | ⭐⭐⭐⭐⭐ |

# Overall Score

**9.8/10** ⭐⭐⭐⭐⭐

Only a tiny improvement was needed: capture `e` in the specific `except` blocks if you want to print the actual error message.

---

# Roadmap Progress

```text
Lesson 12
│
├── ✅ Module 1 - Introduction
├── ✅ Module 2 - try & except
├── ▶ Module 3 - else & finally
├── ⏳ Module 4 - raise
├── ⏳ Module 5 - Custom Exceptions
├── ⏳ Module 6 - Best Practices
└── ⏳ ATM Banking System Project
```

## 🎯 Next Module

We'll move to **Module 3 – `else` & `finally`**, where you'll learn:

* Why `else` exists when we already have `try` and `except`
* When `finally` executes (even if an exception occurs)
* Resource cleanup (files, database connections, APIs)
* Real-world examples from Python, AI applications, and Magento
