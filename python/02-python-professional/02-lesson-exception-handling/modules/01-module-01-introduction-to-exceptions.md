# 📘 Lesson 12 – Module 1

# Introduction to Exception Handling

**Estimated Time:** 20–25 minutes

---

# Learning Objectives

By the end of this module, you will understand:

* ✅ What is an Exception?
* ✅ What is an Error?
* ✅ Difference between Syntax Error and Exception
* ✅ Compile-time vs Runtime Errors
* ✅ Common Python Exceptions
* ✅ Exception Hierarchy
* ✅ Why Exception Handling is Important

---

# What is an Error?

An **error** is any problem that prevents your program from working correctly.

Example:

```python
print("Hello"
```

Output:

```text
SyntaxError: '(' was never closed
```

Python cannot even start the program because the code itself is invalid.

---

# What is an Exception?

An **exception** is an error that occurs **while the program is running (runtime)**.

Example:

```python
print("Program Started")

num = 10 / 0

print("Program Finished")
```

Output:

```text
Program Started

ZeroDivisionError: division by zero
```

Notice:

* The program **started successfully**.
* It crashed only when it reached `10 / 0`.

This is called an **exception**.

---

# Syntax Error vs Exception

| Syntax Error                    | Exception                                           |
| ------------------------------- | --------------------------------------------------- |
| Happens before execution        | Happens during execution                            |
| Program never starts            | Program starts, then fails                          |
| Caused by invalid Python syntax | Caused by invalid operation or unexpected situation |
| Fixed by correcting code        | Can often be handled using `try`/`except`           |

---

## Example 1 – Syntax Error

```python
if True
    print("Hello")
```

Output:

```text
SyntaxError
```

Python stops before running any code.

---

## Example 2 – Exception

```python
numbers = [1, 2, 3]

print(numbers[5])
```

Output:

```text
IndexError: list index out of range
```

The code is syntactically correct, but it fails at runtime.

---

# Compile-Time vs Runtime

Although Python is interpreted, these terms are still useful.

## Compile-Time (Parsing Stage)

Python first checks whether your code is syntactically valid.

Example:

```python
print("Hello"
```

Python stops immediately.

---

## Runtime

Now Python executes line by line.

Example:

```python
print("Start")

name = "John"

print(name.upper())

print(10 / 0)

print("End")
```

Output:

```text
Start
JOHN

ZeroDivisionError
```

Execution stopped only when the invalid operation occurred.

---

# Why Do Exceptions Occur?

Exceptions happen because of situations that cannot always be predicted.

For example:

```python
age = int(input("Enter age: "))
```

Expected input:

```text
25
```

But the user enters:

```text
twenty
```

Output:

```text
ValueError
```

Your code isn't wrong—the user's input is unexpected.

---

# Common Python Exceptions

Let's look at the exceptions you'll encounter most often.

---

## 1. ZeroDivisionError

```python
print(100 / 0)
```

Output:

```text
ZeroDivisionError
```

---

## 2. ValueError

```python
number = int("abc")
```

Output:

```text
ValueError
```

Occurs when a value has the correct type but an invalid value for the operation.

---

## 3. TypeError

```python
print(10 + "5")
```

Output:

```text
TypeError
```

You're trying to combine incompatible types.

---

## 4. IndexError

```python
numbers = [10, 20, 30]

print(numbers[5])
```

Output:

```text
IndexError
```

The requested index doesn't exist.

---

## 5. KeyError

```python
student = {
    "name": "Rahul"
}

print(student["age"])
```

Output:

```text
KeyError
```

The dictionary doesn't contain that key.

---

## 6. FileNotFoundError

```python
open("data.txt")
```

Output:

```text
FileNotFoundError
```

The specified file cannot be found.

---

## 7. AttributeError

```python
number = 10

number.append(5)
```

Output:

```text
AttributeError
```

`append()` exists for lists, not integers.

---

# Exception Hierarchy

Every exception in Python inherits from a base class.

```text
BaseException
│
├── Exception
│   ├── ArithmeticError
│   │     └── ZeroDivisionError
│   │
│   ├── LookupError
│   │     ├── IndexError
│   │     └── KeyError
│   │
│   ├── ValueError
│   ├── TypeError
│   ├── FileNotFoundError
│   ├── AttributeError
│   └── ...
│
├── KeyboardInterrupt
└── SystemExit
```

This hierarchy is why you can catch either a **specific exception** or the broader `Exception` class.

---

# Why Not Ignore Exceptions?

Imagine you're building an ATM.

```python
amount = int(input("Enter amount: "))
```

User enters:

```text
abc
```

Without exception handling:

```text
Program Crashed
```

With exception handling:

```text
Invalid amount.
Please enter numbers only.
```

The application continues running.

---

# Real AI Example

Imagine you're calling an AI API.

```python
response = ai.generate(prompt)
```

Possible failures:

* Internet disconnected
* Invalid API key
* API timeout
* Rate limit exceeded
* Server unavailable

Without exception handling:

```text
Application Crashed
```

With exception handling:

```text
Retrying...
Using backup model...
Showing friendly error message...
```

This is why exception handling is essential in AI applications.

---

# Real Magento Example

Suppose you're loading an order.

```php
$order = $this->orderRepository->get($orderId);
```

If the order doesn't exist, Magento throws an exception.

Without handling it:

```text
500 Internal Server Error
```

With handling:

```php
try {
    $order = $this->orderRepository->get($orderId);
} catch (\Magento\Framework\Exception\NoSuchEntityException $e) {
    // Show "Order not found"
}
```

The same concept applies in Python.

---

# Best Practice

Don't think of exceptions as "bugs."

Many exceptions represent **expected situations**:

* Invalid user input
* Missing file
* Network timeout
* Payment failure
* Product not found

Good software anticipates these situations and responds gracefully.

---

# Mini Exercise

Predict the exception for each snippet **without running the code**.

### Question 1

```python
print(10 / 0)
```

What exception will occur?

---

### Question 2

```python
numbers = [1, 2, 3]

print(numbers[10])
```

What exception will occur?

---

### Question 3

```python
age = int("hello")
```

What exception will occur?

---

### Question 4

```python
student = {
    "name": "John"
}

print(student["age"])
```

What exception will occur?

---

### Question 5

```python
print(10 + "20")
```

What exception will occur?

---

# Interview Questions

### Q1. What is an exception?

**Answer:** An exception is an error that occurs during program execution (runtime) and interrupts the normal flow unless it is handled.

---

### Q2. What is the difference between a syntax error and an exception?

| Syntax Error                        | Exception                               |
| ----------------------------------- | --------------------------------------- |
| Detected before execution           | Occurs during execution                 |
| Prevents the program from starting  | Stops execution at the point of failure |
| Cannot be handled with `try/except` | Can often be handled with `try/except`  |

---

### Q3. Why is exception handling important?

**Answer:** It prevents applications from crashing unexpectedly, allows graceful recovery from expected failures, improves user experience, and makes software more reliable.

---

## ✅ Module 1 Complete

**Progress**

* ✅ Module 1 – Introduction to Exceptions
* ▶️ Module 2 – `try` & `except`
* ⏳ Module 3 – `else` & `finally`
* ⏳ Module 4 – `raise`
* ⏳ Module 5 – Custom Exceptions
* ⏳ Module 6 – Best Practices
* ⏳ Module 7 – ATM Banking System Project
* ⏳ Module 8 – Interview Revision

### Your Task

Reply with the answers to the **5 prediction questions**. Once you answer them, I'll review them and then we'll move to **Module 2 – `try` & `except`**.
