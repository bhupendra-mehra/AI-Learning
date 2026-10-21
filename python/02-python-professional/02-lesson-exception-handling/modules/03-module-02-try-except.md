# 📘 Lesson 12 – Module 2

# `try` & `except`

**Estimated Time:** 30–40 minutes

---

# Learning Objectives

By the end of this module, you will be able to:

* ✅ Understand `try`
* ✅ Understand `except`
* ✅ Catch specific exceptions
* ✅ Catch multiple exceptions
* ✅ Capture exception messages
* ✅ Know when to use generic exceptions
* ✅ Write production-quality exception handling

---

# Imagine This Scenario

Suppose you're creating a calculator.

```python
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

print(num1 / num2)

print("Thank You")
```

### Case 1

Input

```
10
2
```

Output

```
5.0
Thank You
```

Everything works.

---

### Case 2

Input

```
10
0
```

Output

```
ZeroDivisionError
```

Program crashes.

---

### Case 3

Input

```
ten
5
```

Output

```
ValueError
```

Again crashes.

---

This is where **Exception Handling** comes into the picture.

---

# What is `try`?

`try` means:

> **"Python, execute this block because it might throw an exception."**

Syntax

```python
try:
    risky code
```

Example

```python
try:
    print(10 / 0)
```

Python executes the code.

If no error occurs:

Everything runs normally.

If an error occurs:

Python immediately jumps to the matching `except` block.

---

# What is `except`?

`except` means:

> **"If something goes wrong inside the `try` block, execute this code instead of crashing."**

Example

```python
try:
    print(10 / 0)

except:
    print("Something went wrong.")
```

Output

```
Something went wrong.
```

Notice

The program didn't crash.

---

# Flow Diagram

```
          try
           │
           ▼
    Any Exception?
      /        \
    No          Yes
    │            │
    ▼            ▼
 Continue     except Block
```

---

# Example 1

Without exception handling

```python
number = int(input("Enter Number : "))

print(100 / number)

print("Program Finished")
```

Input

```
0
```

Output

```
ZeroDivisionError
```

Program stops.

---

Now

```python
try:

    number = int(input("Enter Number : "))

    print(100 / number)

except:

    print("Error occurred.")

print("Program Finished")
```

Input

```
0
```

Output

```
Error occurred.

Program Finished
```

Notice

The last line executes.

---

# Execution Flow

Input

```
0
```

Execution

```
try
↓

100 / 0

↓

Exception Occurred

↓

Jump to except

↓

Print Error

↓

Continue Program
```

---

# Example 2

```python
try:

    age = int(input("Age : "))

    print(age)

except:

    print("Please enter numbers only.")
```

Input

```
twenty
```

Output

```
Please enter numbers only.
```

---

# Catching Specific Exceptions

This is the preferred approach.

Instead of

```python
except:
```

Use

```python
except ValueError:
```

or

```python
except ZeroDivisionError:
```

---

## Why?

Suppose

```python
try:

    print(name)
```

Output

```
NameError
```

If you use

```python
except:
```

It catches **everything**, including unexpected bugs.

This makes debugging difficult because it hides the real problem.

---

## Better Version

```python
try:

    age = int(input("Age : "))

except ValueError:

    print("Age should contain only numbers.")
```

Now only `ValueError` is handled.

Other unexpected exceptions still appear, helping you identify bugs.

---

# Handling Multiple Exceptions

Example

```python
try:

    number = int(input("Enter Number : "))

    print(100 / number)

except ValueError:

    print("Invalid Number")

except ZeroDivisionError:

    print("Cannot divide by zero.")
```

---

## Test 1

Input

```
abc
```

Output

```
Invalid Number
```

---

## Test 2

Input

```
0
```

Output

```
Cannot divide by zero.
```

---

## Test 3

Input

```
5
```

Output

```
20.0
```

---

# Multiple Exceptions in One Block

Sometimes multiple exceptions need the same handling.

```python
try:

    number = int(input("Enter Number : "))

    print(100 / number)

except (ValueError, ZeroDivisionError):

    print("Invalid Input")
```

Notice

Parentheses create a tuple of exception types.

---

## Test

Input

```
abc
```

Output

```
Invalid Input
```

---

Input

```
0
```

Output

```
Invalid Input
```

---

# Capturing Exception Object

Sometimes we want to know

**What exactly happened?**

Example

```python
try:

    number = int(input("Enter Number : "))

    print(100 / number)

except Exception as e:

    print(e)
```

Input

```
0
```

Output

```
division by zero
```

---

Input

```
abc
```

Output

```
invalid literal for int() with base 10: 'abc'
```

---

## What is `e`?

Think of `e` as an object that contains information about the exception.

For example:

```python
try:
    number = int("abc")

except Exception as e:
    print(type(e))
    print(e)
```

Output

```text
<class 'ValueError'>
invalid literal for int() with base 10: 'abc'
```

Here:

* `type(e)` tells you which exception occurred.
* `e` contains the human-readable error message.

---

# Generic Exception

```python
except Exception as e:
```

This catches **most application exceptions**.

### When should you use it?

✔ At the top level of your application to prevent it from crashing unexpectedly.

✔ For logging unexpected errors before re-raising or exiting gracefully.

### When should you avoid it?

If you already know which exception can occur.

Example:

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a valid number.")
```

This is clearer than catching every exception.

---

# Exception Order Matters

Suppose you write:

```python
try:
    number = int(input())

except Exception:
    print("General Error")

except ValueError:
    print("Invalid Number")
```

❌ This is incorrect.

Why?

Because `Exception` is the parent class of `ValueError`.

The first `except` already catches `ValueError`, making the second block unreachable.

---

## Correct Order

```python
try:
    number = int(input())

except ValueError:
    print("Invalid Number")

except Exception:
    print("General Error")
```

**Rule:**

> Catch **specific exceptions first**, then more general ones.

---

# Real AI Example

```python
try:
    response = ai.generate(prompt)

except TimeoutError:
    print("Retrying request...")

except PermissionError:
    print("Invalid API key.")

except Exception as e:
    print("Unexpected Error:", e)
```

This allows different recovery strategies for different failures.

---

# Real Magento Example

```php
try {
    $product = $this->productRepository->getById($id);

} catch (\Magento\Framework\Exception\NoSuchEntityException $e) {

    echo "Product not found.";

} catch (\Exception $e) {

    $this->logger->error($e->getMessage());
}
```

Notice the same principle:

* Catch the **specific** exception first.
* Catch the **general** exception last.

---

# Best Practices

✅ Catch only the exceptions you expect.

```python
except ValueError:
```

❌ Avoid

```python
except:
```

unless you have a very specific reason.

---

# Mini Exercise

Write a program that:

1. Takes **two numbers** from the user.
2. Divides the first by the second.
3. Handles:

   * `ValueError`
   * `ZeroDivisionError`
4. Prints the actual error message using `Exception as e`.
5. Prints `"Program Ended Successfully"` after the exception handling, regardless of whether an error occurred.

---

### Sample Output 1

Input

```
10
2
```

Output

```
Result: 5.0
Program Ended Successfully
```

---

### Sample Output 2

Input

```
10
0
```

Output

```
Cannot divide by zero.
division by zero
Program Ended Successfully
```

---

### Sample Output 3

Input

```
abc
5
```

Output

```
Please enter valid numbers.
invalid literal for int() with base 10: 'abc'
Program Ended Successfully
```

---

# Interview Questions

### Q1. What is the purpose of the `try` block?

**Answer:** It contains code that may raise an exception.

---

### Q2. Why should we avoid using a bare `except:`?

**Answer:** Because it catches all exceptions, including unexpected programming errors, making debugging difficult and potentially hiding bugs.

---

### Q3. Why should specific exceptions be caught before `Exception`?

**Answer:** Because `Exception` is the parent class of most application exceptions. If it's placed first, it catches the error before the specific `except` blocks get a chance to handle it.

---

## Module 2 Progress

* ✅ Module 1 – Introduction to Exceptions
* ✅ Module 2 – `try` & `except`
* ▶️ Next: Module 3 – `else` & `finally`

---

### Your Task

Complete the **Mini Exercise** and paste your code here. I'll review it as if it were a coding interview submission, then we'll continue with **Module 3 – `else` & `finally`**.
