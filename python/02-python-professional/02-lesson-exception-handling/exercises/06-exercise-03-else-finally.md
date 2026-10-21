# Your Code

```python
try:
    number1 = int(input("Enter first number :"))
    number2 = int(input("Enter second number : "))
    result = number1/number2

except ValueError:
    print("Invalid numbers")

except ZeroDivisionError:
    print("Divide by zero")

except Exception as e:
    print(e)

else:
    print(f"Result : {result}")
    print("Calculation Successful")

finally:
    print("Program Finished")
```

---

# Review

## 1. try Block ⭐⭐⭐⭐⭐

```python
try:
```

✔ Correct

Only the risky code is inside `try`.

This is exactly how it should be.

---

## 2. except Blocks ⭐⭐⭐⭐⭐

```python
except ValueError:
```

✔ Correct

Handles

```python
int("abc")
```

---

```python
except ZeroDivisionError:
```

✔ Correct

Handles

```python
10/0
```

---

```python
except Exception as e:
```

✔ Correct

Acts as a fallback for unexpected exceptions.

Excellent.

---

## 3. else ⭐⭐⭐⭐⭐

```python
else:
    print(f"Result : {result}")
```

Perfect.

Notice what you've achieved:

If any exception occurs,

```python
result
```

is never used.

Only successful execution reaches the `else` block.

This is exactly why `else` exists.

---

## 4. finally ⭐⭐⭐⭐⭐

```python
finally:
    print("Program Finished")
```

Perfect.

No matter what happens,

this line always executes.

---

# Dry Run

---

### Case 1

Input

```text
20
5
```

Execution

```text
try
↓

Success

↓

else

↓

finally
```

Output

```text
Result : 4.0
Calculation Successful
Program Finished
```

✔ Correct

---

### Case 2

Input

```text
20
0
```

Execution

```text
try

↓

ZeroDivisionError

↓

except ZeroDivisionError

↓

finally
```

Output

```text
Divide by zero
Program Finished
```

✔ Correct

---

### Case 3

Input

```text
abc
5
```

Execution

```text
try

↓

ValueError

↓

except ValueError

↓

finally
```

Output

```text
Invalid numbers
Program Finished
```

✔ Correct

---

# Visual Flow

```
                try
                 │
      ┌──────────┴──────────┐
      │                     │
 No Exception         Exception
      │                     │
      ▼                     ▼
    else                except
      │                     │
      └──────────┬──────────┘
                 ▼
              finally
```

This is the diagram I personally remember even after years of programming.

---

# Interview Questions

## Q1

**What is the difference between `else` and `finally`?**

**Answer**

| else                                 | finally             |
| ------------------------------------ | ------------------- |
| Executes only if no exception occurs | Executes every time |
| Used for success logic               | Used for cleanup    |
| Optional                             | Optional            |

---

## Q2

**Can `finally` execute after `return`?**

Example

```python
def test():
    try:
        return 100
    finally:
        print("Finally")
```

Output

```text
Finally
100
```

Yes.

`finally` executes **before the function actually returns**.

This is a favorite interview question.

---

## Q3

**Can we write `try` without `except`?**

Yes.

Example

```python
try:
    print("Hello")
finally:
    print("Done")
```

✔ Valid

---

## Q4

**Can we write `try` without `finally`?**

Yes.

```python
try:
    print("Hello")
except:
    print("Error")
```

✔ Valid

---

## Q5

**Can we write `else` without `except`?**

❌ No.

Invalid

```python
try:
    print("Hello")

else:
    print("Done")
```

Python raises a syntax error.

`else` requires at least one `except`.

---

# Professional Tip

Instead of

```python
except ValueError:
```

many companies write

```python
except ValueError as e:
    logger.error(e)
    print("Invalid Number")
```

Even if the user sees a friendly message, the application logs the actual error for debugging.

You'll see this pattern frequently in **Magento**, **Django**, **Flask**, and **AI services**.

---

# Score

| Section      | Score |
| ------------ | ----- |
| try          | ⭐⭐⭐⭐⭐ |
| except       | ⭐⭐⭐⭐⭐ |
| else         | ⭐⭐⭐⭐⭐ |
| finally      | ⭐⭐⭐⭐⭐ |
| Program Flow | ⭐⭐⭐⭐⭐ |
| Code Style   | ⭐⭐⭐⭐⭐ |

# Overall

**10/10** 🎉

This is a production-quality solution for the concepts we've covered.

---

# Lesson Progress

```
Python Roadmap

Lesson 12
│
├── ✅ Module 1 – Introduction
├── ✅ Module 2 – try & except
├── ✅ Module 3 – else & finally
├── ▶ Module 4 – raise
├── ⏳ Module 5 – Custom Exceptions
├── ⏳ Module 6 – Best Practices
└── ⏳ ATM Banking System
```

## 🎯 Next Module: `raise`

In **Module 4**, you'll learn something many Python beginners don't encounter until much later:

* What `raise` is and why it's needed.
* How to intentionally throw exceptions.
* How to enforce business rules (e.g., age must be at least 18, withdrawal amount cannot exceed balance).
* How `raise` differs from `return`.
* Real-world examples from AI applications and Magento.

This module is especially important because it introduces **creating errors intentionally**, which is a common practice in production software.
