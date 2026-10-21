# 📘 Lesson 12 – Module 6

# Exception Handling Best Practices

**Estimated Time:** 35–40 minutes

---

# Learning Objectives

By the end of this module, you'll know:

* ✅ Professional exception handling techniques
* ✅ Common beginner mistakes
* ✅ How large applications handle exceptions
* ✅ Logging exceptions
* ✅ Re-raising exceptions
* ✅ Nested try blocks
* ✅ Multiple exception handling
* ✅ Best coding practices

---

# Why Best Practices Matter?

Consider these two developers.

## Beginner

```python
try:
    process_order()
except:
    pass
```

Program doesn't crash.

Looks good?

❌ No.

If there is an error,

you'll never know.

---

## Professional

```python
try:
    process_order()

except OrderNotFoundError as e:
    print(e)

except Exception as e:
    logger.error(e)
```

Now

* Specific errors are handled.
* Unexpected errors are logged.
* Bugs become easier to fix.

---

# Rule 1

# Never Use

```python
except:
```

Why?

Because it catches almost everything.

Example

```python
try:
    print(name)

except:
    print("Error")
```

Output

```text
Error
```

Question:

What was the error?

You don't know.

Maybe

* NameError
* TypeError
* ValueError

Everything is hidden.

---

# Better

```python
except NameError:
```

or

```python
except Exception as e:
    print(e)
```

Now you know what happened.

---

# Rule 2

# Catch Specific Exceptions First

Wrong

```python
try:
    age = int(input())

except Exception:
    print("General Error")

except ValueError:
    print("Invalid Number")
```

Why wrong?

Because

```text
Exception
    ▲
ValueError
```

Python reaches

```python
except Exception
```

first.

The `ValueError` block is never reached.

---

Correct

```python
try:
    age = int(input())

except ValueError:
    print("Invalid Number")

except Exception:
    print("General Error")
```

---

# Rule 3

# Don't Hide Errors

Wrong

```python
try:
    database.save()

except:
    pass
```

If the database fails,

the user thinks

```text
Everything Worked
```

when nothing was saved.

This creates silent failures.

---

Better

```python
try:
    database.save()

except Exception as e:
    print(e)
```

Even better

```python
logger.error(e)
```

We'll discuss logging in future lessons.

---

# Rule 4

# Keep try Blocks Small

Wrong

```python
try:

    connect_database()

    fetch_data()

    process_data()

    save_data()

    send_email()

except Exception:
    print("Error")
```

Question:

Which statement failed?

Hard to tell.

---

Better

```python
try:
    connect_database()

except DatabaseError:
    print("Database Error")


try:
    send_email()

except EmailError:
    print("Email Failed")
```

Small `try` blocks make debugging much easier.

---

# Rule 5

# Use finally for Cleanup

Wrong

```python
file = open("data.txt")

data = file.read()

print(data)
```

If an exception occurs,

the file may stay open.

---

Better

```python
file = None

try:
    file = open("data.txt")
    data = file.read()

except FileNotFoundError:
    print("File Not Found")

finally:
    if file:
        file.close()
```

Notice the improvement over our earlier example:

* We initialize `file = None`.
* We check `if file:` before calling `close()`.

This avoids needing another `try/except` just to close the file.

> **Production Note:** In modern Python, the preferred approach is:

```python
with open("data.txt") as file:
    data = file.read()
```

We'll learn `with` statements and context managers in a later lesson.

---

# Rule 6

# Re-raising Exceptions

Sometimes

you want to

* Log the error
* Then let another part of the program handle it

Example

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Logging Error")
    raise
```

Output

```text
Logging Error

ZeroDivisionError
```

Notice

The exception wasn't swallowed.

It continued upward.

---

# Why Re-raise?

Large applications

have

```text
Function

↓

Service

↓

Controller

↓

Main Application
```

Sometimes

the function logs

the error

but lets

the controller

decide

what to do.

---

# Rule 7

# Nested try Blocks

Example

```python
try:

    age = int(input())

    try:

        result = 100 / age

    except ZeroDivisionError:

        print("Cannot divide by zero")

except ValueError:

    print("Invalid Number")
```

Input

```text
abc
```

Output

```text
Invalid Number
```

---

Input

```text
0
```

Output

```text
Cannot divide by zero
```

Nested `try` blocks are useful when different operations require different handling.

---

# Rule 8

# Custom Exceptions for Business Rules

Instead of

```python
raise ValueError("Balance Low")
```

Better

```python
raise InsufficientBalanceError(
    "Balance Low"
)
```

This makes your code self-explanatory.

---

# Rule 9

# Never Ignore Exceptions

Wrong

```python
except:
    pass
```

Better

```python
except Exception as e:
    print(e)
```

Best

```python
except Exception as e:
    logger.error(e)
```

Ignoring exceptions makes debugging extremely difficult.

---

# Real AI Example

```python
try:

    response = ai.generate(prompt)

except TimeoutError:

    retry()

except AuthenticationError:

    print("Invalid API Key")

except Exception as e:

    logger.error(e)
```

Different failures require different recovery actions.

---

# Magento Example

```php
try {

    $product = $repository->getById($id);

}
catch (NoSuchEntityException $e) {

    return "Product Not Found";

}
catch (\Exception $e) {

    $logger->error($e->getMessage());

    throw $e;
}
```

This is exactly the pattern used in enterprise applications:

* Handle expected exceptions.
* Log unexpected ones.
* Re-throw when necessary.

---

# Professional Exception Flow

```text
User

↓

Controller

↓

Service

↓

Repository

↓

Database
```

If something fails

```text
Database

↓

Repository logs

↓

Service handles

↓

Controller returns response
```

This layered handling keeps code organized and maintainable.

---

# Summary of Best Practices

| Rule | Good Practice                            |
| ---- | ---------------------------------------- |
| 1    | Catch specific exceptions first          |
| 2    | Avoid bare `except:`                     |
| 3    | Don't ignore exceptions (`pass`)         |
| 4    | Keep `try` blocks small                  |
| 5    | Use `finally` (or `with`) for cleanup    |
| 6    | Re-raise exceptions when appropriate     |
| 7    | Use custom exceptions for business rules |
| 8    | Log unexpected exceptions                |
| 9    | Write meaningful exception messages      |

---

# Mini Exercise

Find the mistakes in this code and rewrite it.

```python
try:

    number = int(input())

    result = 100 / number

except:

    pass

print(result)
```

Questions:

1. What's wrong with this code?
2. How would you improve it?
3. What happens if the user enters:

   * `0`
   * `abc`

---

# Interview Questions

### Q1. Why is `except:` discouraged?

**Answer:** Because it catches almost every exception, including unexpected programming errors, making debugging difficult.

---

### Q2. Why should `try` blocks be small?

**Answer:** Smaller `try` blocks make it easier to identify which statement failed and reduce the chance of accidentally catching unrelated exceptions.

---

### Q3. Why use custom exceptions instead of `ValueError`?

**Answer:** Custom exceptions make business rule violations explicit, improving readability and maintainability.

---

### Q4. When should you re-raise an exception?

**Answer:** When you need to perform an action (such as logging) but still want the caller to decide how to handle the error.

---

# 🏆 Module 6 Complete

Congratulations!

You have now learned:

* ✅ Introduction to Exceptions
* ✅ `try`
* ✅ `except`
* ✅ `else`
* ✅ `finally`
* ✅ `raise`
* ✅ Custom Exceptions
* ✅ Production Best Practices

---

# 📈 Lesson Progress

```text
Lesson 12
│
├── ✅ Module 1
├── ✅ Module 2
├── ✅ Module 3
├── ✅ Module 4
├── ✅ Module 5
├── ✅ Module 6
└── ▶ ATM Banking System Project
```

---

# 📝 Your Exercise

Before we start the ATM Banking System project, review this code:

```python
try:
    number = int(input())

    result = 100 / number

except:
    pass

print(result)
```

Tell me:

1. What are the mistakes?
2. Rewrite it using the best practices you've learned.

Once you've done that, we'll build the **ATM Banking System**, which combines:

* OOP
* Custom Exceptions
* `try` / `except`
* `else`
* `finally`
* `raise`
* Input Validation
* Business Rules

This project will serve as your capstone for Lesson 12 and closely resemble real-world application logic.
