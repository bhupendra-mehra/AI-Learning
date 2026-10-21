# Question 1

## What's wrong with this code?

Original code:

```python
try:
    number = int(input())

    result = 100 / number

except:
    pass

print(result)
```

### Your Answer

> no instruction in input and except not have any specific exception class except catch all the error also not discourage and keep running code

### Review

✅ Correct points:

* ✔ `input()` should have a meaningful prompt.
* ✔ `except:` catches almost every exception.
* ✔ Bare `except:` is discouraged.
* ✔ Catch specific exceptions whenever possible.

---

### But you missed one **very important bug**.

Look carefully.

```python
print(result)
```

Suppose the user enters

```text
0
```

Execution:

```text
result = 100 / 0

↓

ZeroDivisionError

↓

except

↓

pass

↓

print(result)
```

Question:

Was `result` ever created?

❌ No.

So Python now raises another exception:

```text
NameError:
name 'result' is not defined
```

This is a classic interview question.

---

# Question 2

## What happens when user enters 0?

You answered

> division by zero

Partially correct.

Actually the execution is:

```text
100 / 0

↓

ZeroDivisionError

↓

except

↓

pass

↓

print(result)

↓

NameError
```

Because the original `ZeroDivisionError` is silently ignored, the next error is caused by trying to use `result`, which was never assigned.

---

# Question 3

## What if user enters "abc"?

You answered

```text
invalid literal for int() with base 10: 'abc'
```

Again,

that's what happens **before** the exception is swallowed.

But the original code has:

```python
except:
    pass
```

So the flow is:

```text
ValueError

↓

except

↓

pass

↓

print(result)

↓

NameError
```

Again,

the final visible error becomes

```text
NameError:
name 'result' is not defined
```

---

# Your Improved Code

```python
try:

    number = int(input("Enter number :"))

    result = 100 / number

except ValueError as e:
    print(e)

except Exception as e:
    print(e)

else:
    print(result)
```

---

## Review

### Input Prompt ⭐⭐⭐⭐⭐

```python
input("Enter number :")
```

✔ Good.

---

### ValueError ⭐⭐⭐⭐⭐

```python
except ValueError as e
```

Excellent.

---

### Exception ⭐⭐⭐⭐⭐

```python
except Exception as e
```

Correct.

Acts as a fallback.

---

### else ⭐⭐⭐⭐⭐

Perfect.

```python
else:
    print(result)
```

This guarantees that `result` exists before printing it.

Excellent improvement.

---

# One More Improvement

Suppose user enters

```text
0
```

Your code prints

```text
division by zero
```

Because

```python
ZeroDivisionError
```

inherits from

```python
Exception
```

So it reaches

```python
except Exception
```

This works,

but we can make it clearer.

Production version:

```python
try:

    number = int(input("Enter Number : "))

    result = 100 / number

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception as e:
    print(e)

else:
    print(f"Result : {result}")
```

This provides user-friendly messages for the expected errors while still handling unexpected ones.

---

# Interview Question ⭐⭐⭐⭐⭐

**Q. Why is `else` better than writing `print(result)` after the `try` block?**

**Answer:**

Because `else` executes only when the `try` block completes successfully. It guarantees that variables like `result` have been created and prevents errors such as `NameError`.

This is one of the strongest interview answers you can give.

---

# Score

| Topic                   | Score |
| ----------------------- | ----: |
| Finding Bugs            | ⭐⭐⭐⭐⭐ |
| Understanding `except:` | ⭐⭐⭐⭐⭐ |
| Code Improvement        | ⭐⭐⭐⭐⭐ |
| Logic                   | ⭐⭐⭐⭐☆ |

## Overall

**9.8/10** 🎉

The only thing you missed was the **`NameError` caused by `print(result)`** after swallowing the original exception. That's a subtle bug that even experienced developers sometimes overlook.

---

# 🎉 Congratulations!

## Lesson 12 Theory is 100% Complete.

You now know:

* ✅ Runtime Exceptions
* ✅ `try`
* ✅ `except`
* ✅ `else`
* ✅ `finally`
* ✅ `raise`
* ✅ Custom Exceptions
* ✅ Best Practices
* ✅ Professional Exception Handling

---

# Next: Lesson 12 Capstone Project

Now we'll build a **complete ATM Banking System** that combines everything you've learned.

It will include:

* 🏦 OOP (Classes & Objects)
* 💰 Deposit
* 💸 Withdraw
* 📊 Check Balance
* ⚠️ Exception Handling
* 🚫 Custom Exceptions
* 🔒 Business Rules
* ✅ Input Validation
* 🔁 Menu-driven application
* 🎯 Interview-level code structure

This project will tie together **Lessons 11 and 12** and closely resemble how real applications are structured. After completing it, we'll officially mark **Lesson 12** as complete and move on to **Lesson 13**.
