# 📘 Lesson 12 – Module 3

# `else` & `finally`

**Estimated Time:** 30–35 minutes

---

# Learning Objectives

By the end of this module, you will understand:

* ✅ What is `else`?
* ✅ What is `finally`?
* ✅ Execution flow of `try`, `except`, `else`, and `finally`
* ✅ File handling with `finally`
* ✅ Database cleanup
* ✅ API cleanup
* ✅ Production best practices

---

# Why Do We Need `else`?

Suppose you have this code:

```python
try:
    number = int(input("Enter Number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Invalid Number")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Question:

> **Where should we write the success message?**

Example:

```text
Calculation Completed Successfully
```

Inside `try`?

Not a good idea.

Why?

Because if an exception occurs before reaching that line, the message won't execute.

---

# Enter `else`

The `else` block executes **only when the `try` block completes successfully without any exception**.

---

## Syntax

```python
try:
    risky code

except SomeException:
    handle error

else:
    runs only if no exception occurred
```

---

# Example 1

```python
try:

    number = int(input("Enter Number : "))

    result = 100 / number

except ValueError:

    print("Invalid Number")

except ZeroDivisionError:

    print("Cannot divide by zero.")

else:

    print(f"Result : {result}")

    print("Calculation Successful")
```

---

### Test 1

Input

```text
10
```

Output

```text
Result : 10.0
Calculation Successful
```

---

### Test 2

Input

```text
0
```

Output

```text
Cannot divide by zero.
```

Notice:

The `else` block did **not** execute.

---

### Test 3

Input

```text
abc
```

Output

```text
Invalid Number
```

Again,

`else` did **not** execute.

---

# Execution Flow

```text
            try
              │
      Exception?
      /        \
    No          Yes
    │            │
    ▼            ▼
  else       except
```

---

# Why Not Put Success Code Inside `try`?

Example:

```python
try:

    number = int(input())

    result = 100 / number

    print("Success")
```

This works.

But imagine:

```python
try:

    save_to_database()

    send_email()

    create_invoice()

    print("Success")
```

If an exception occurs in `send_email()`:

```text
save_to_database() ✔

send_email() ❌

create_invoice() ❌

Success ❌
```

Using `else` makes it clear that the success block runs **only if every statement in `try` succeeds**.

This separation improves readability.

---

# What is `finally`?

`finally` means:

> **Run this code no matter what happens.**

Even if:

* Exception occurs
* No exception occurs
* `return` is executed
* Another exception is raised (with some caveats)

---

# Syntax

```python
try:
    risky code

except:
    handle error

finally:
    always executes
```

---

# Example

```python
try:

    print(100 / 0)

except ZeroDivisionError:

    print("Division by Zero")

finally:

    print("Program Finished")
```

Output

```text
Division by Zero
Program Finished
```

Notice:

`finally` always executes.

---

# Another Example

```python
try:

    print("Hello")

finally:

    print("Finished")
```

Output

```text
Hello
Finished
```

Even though no exception occurred, `finally` still ran.

---

# Complete Flow

```text
try
 │
 ├── Success ──► else
 │                 │
 │                 ▼
 └──────────────► finally

OR

try
 │
 ├── Exception
 │
 ▼
except
 │
 ▼
finally
```

---

# Order of Execution

```python
try:

    print("Try")

except:

    print("Except")

else:

    print("Else")

finally:

    print("Finally")
```

---

### Case 1

No Exception

Output

```text
Try
Else
Finally
```

---

### Case 2

Exception

Output

```text
Try
Except
Finally
```

---

# Real-Life Example – File Handling

Suppose you open a file.

```python
file = open("data.txt")
```

After reading,

you should always close it.

Incorrect:

```python
file = open("data.txt")

data = file.read()

print(data)
```

If an exception occurs before closing:

```text
File remains open.
```

This can lead to resource leaks.

---

### Correct

```python
try:

    file = open("data.txt")

    data = file.read()

    print(data)

except FileNotFoundError:

    print("File Not Found")

finally:

    print("Closing File")

    try:
        file.close()
    except NameError:
        pass
```

Whether the file exists or not,

the cleanup code runs.

> **Note:** In modern Python, `with open(...) as file:` is the preferred approach because it automatically closes the file. We'll cover context managers in a later lesson. For now, `finally` helps illustrate the cleanup concept.

---

# Database Example

Imagine:

```python
database.connect()
```

Then

```python
database.disconnect()
```

must always execute.

```python
try:

    database.connect()

    # queries

except:

    print("Database Error")

finally:

    database.disconnect()
```

This ensures the connection is released even if a query fails.

---

# API Example

```python
try:

    api.connect()

    api.fetch_data()

except:

    print("API Error")

finally:

    api.disconnect()
```

Resources are cleaned up properly.

---

# AI Example

Imagine:

```python
try:

    response = ai.generate(prompt)

except TimeoutError:

    print("Request Timed Out")

finally:

    print("Request Finished")
```

Whether:

* API succeeds
* API fails
* Network disconnects

The final cleanup or logging still happens.

---

# Magento Example

Imagine:

```php
try {

    $this->resourceConnection->getConnection()->beginTransaction();

    // Save Order

    $this->resourceConnection->getConnection()->commit();

}
catch (\Exception $e) {

    $this->resourceConnection->getConnection()->rollBack();

}
finally {

    $this->logger->info("Order Process Completed");
}
```

The logging happens regardless of success or failure.

---

# Best Practices

### Use `else` for:

* Success messages
* Saving results after all risky operations succeed
* Code that should not execute if an exception occurs

---

### Use `finally` for:

* Closing files
* Closing database connections
* Releasing locks
* Cleaning up temporary files
* Logging completion
* Releasing network resources

---

# Mini Exercise

Write a program that:

1. Accepts two integers.
2. Divides them.
3. Handles:

   * `ValueError`
   * `ZeroDivisionError`
4. Uses `else` to print:

   * Result
   * `"Calculation Successful"`
5. Uses `finally` to print:

```text
Program Finished
```

---

### Example 1

Input

```text
20
5
```

Output

```text
Result : 4.0
Calculation Successful
Program Finished
```

---

### Example 2

Input

```text
20
0
```

Output

```text
Cannot divide by zero.
Program Finished
```

---

### Example 3

Input

```text
abc
5
```

Output

```text
Invalid Number
Program Finished
```

---

# Interview Questions

## Q1. When does the `else` block execute?

**Answer:** It executes only if the `try` block completes successfully without raising any exception.

---

## Q2. When does the `finally` block execute?

**Answer:** It executes regardless of whether an exception occurs or not, making it ideal for cleanup tasks.

---

## Q3. Why should files be closed in `finally`?

**Answer:** To ensure system resources are released even if an exception occurs while reading or writing the file.

---

## Quick Summary

| Block     | Executes When                       |
| --------- | ----------------------------------- |
| `try`     | Always first                        |
| `except`  | Only if a matching exception occurs |
| `else`    | Only if no exception occurs         |
| `finally` | Always, after `try`/`except`/`else` |

---

# 📈 Lesson Progress

```text
Lesson 12
│
├── ✅ Module 1 – Introduction
├── ✅ Module 2 – try & except
├── ✅ Module 3 – else & finally
├── ▶ Module 4 – raise
├── ⏳ Module 5 – Custom Exceptions
├── ⏳ Module 6 – Best Practices
└── ⏳ ATM Banking System Project
```

---

## 📝 Your Task

Complete the **Mini Exercise** and paste your solution here.

After reviewing it, we'll move to **Module 4 – `raise`**, where you'll learn how to create and throw your own exceptions, a common practice in production applications.
