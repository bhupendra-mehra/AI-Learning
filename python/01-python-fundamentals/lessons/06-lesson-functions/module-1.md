# Lesson 9 – Module 1: Introduction to Functions

**Estimated Time:** 35–45 minutes (Fast Track)

---

# 1. What is a Function?

A function is a **reusable block of code** that performs a specific task.

Instead of writing the same code multiple times, write it once inside a function and call it whenever needed.

---

# 2. Why Do We Need Functions?

Suppose you need to print a welcome message in five different places.

Without functions:

```python
print("Welcome")
print("Please Login")

# 100 lines later...

print("Welcome")
print("Please Login")

# Again...

print("Welcome")
print("Please Login")
```

If the message changes, you'll have to update it everywhere.

With a function:

```python
def welcome():
    print("Welcome")
    print("Please Login")
```

Whenever you need it:

```python
welcome()
```

Change it once, and every call uses the updated version.

---

# 3. Function Syntax

```python
def function_name():
    # Code
```

Example:

```python
def greet():
    print("Hello")
```

Here:

* `def` → defines a function.
* `greet` → function name.
* `()` → parentheses (parameters will come later).
* `:` → start of the function body.

---

# 4. Calling a Function

Defining a function **does not execute it**.

Example:

```python
def greet():
    print("Hello")
```

Nothing happens.

To execute it:

```python
greet()
```

Output:

```text
Hello
```

You can call it multiple times:

```python
greet()
greet()
greet()
```

Output:

```text
Hello
Hello
Hello
```

---

# 5. Execution Flow

```text
Program Starts
      │
      ▼
Function Defined
      │
      ▼
(No execution yet)
      │
      ▼
greet()
      │
      ▼
Execute Function
      │
      ▼
Return to Program
```

---

# 6. Magento Comparison

Imagine Magento.

Instead of copying the login code everywhere:

```php
validateCustomer();
```

Instead of repeating discount logic:

```php
calculateDiscount();
```

Functions let you write logic once and reuse it.

Exactly the same idea in Python.

---

# 7. AI Agent Example

An AI assistant receives multiple user messages.

Instead of writing the validation logic repeatedly:

```python
validate_user()

search_documents()

generate_response()

save_chat()
```

Each task is a separate function.

Production AI applications are built from many small functions working together.

---

# 8. Best Practices

### Good function names

```python
calculate_discount()

login_user()

search_product()
```

Avoid:

```python
abc()

test()

fun1()
```

Function names should describe **what they do**.

---

# 9. Common Mistakes

### ❌ Forgetting to call the function

```python
def greet():
    print("Hello")
```

No output.

Because the function was defined but never called.

---

### ❌ Calling before defining (in a top-to-bottom script)

```python
greet()

def greet():
    print("Hello")
```

Python executes files from top to bottom, so this raises an error.

Define first, then call.

---

# Exercises

## Exercise 1

Create a function named:

```python
greet()
```

that prints:

```text
Welcome to Python
```

Call it **three times**.

---

## Exercise 2

Create a function named:

```python
show_menu()
```

that prints:

```text
1. Login
2. Register
3. Exit
```

Call it twice.

---

## Exercise 3

Predict the output:

```python
def hello():
    print("Hello")

hello()
hello()
```

---

## Exercise 4

Predict the output:

```python
def test():
    print("Python")

print("Start")

test()

print("End")
```

---

## Mini Project

Create two functions:

```python
show_header()

show_footer()
```

Output:

```text
====================
Shopping System
====================

...

====================
Thank You
====================
```

Call both functions from the main program.

---

# Senior Developer Tip

A good function should do **one job only**.

Good:

```python
calculate_discount()
```

Bad:

```python
login_and_calculate_discount_and_send_email()
```

One function = one responsibility.

---

Complete these exercises, and then we'll move to **Module 2 (Parameters & Return Values)**, which is where functions become truly powerful. This is the module that will prepare you for writing reusable code in AI applications and production projects.
