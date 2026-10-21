# Lesson 14 – Module 4

# Packages (`__init__.py`)

## Module Objective

So far, you've organized code into separate **files (modules)**.

Now you'll learn how to organize **multiple modules into folders**, called **packages**.

This is how almost every professional Python project is structured.

---

# Why Do We Need Packages?

Imagine you're building a large AI application.

Instead of just two files:

```text
main.py
calculator.py
```

you now have:

```text
main.py
calculator.py
database.py
authentication.py
api.py
config.py
email.py
logger.py
utils.py
pdf.py
image.py
```

Eventually, the project becomes difficult to navigate.

Packages solve this by grouping related modules into folders.

---

# Real-World Example

Instead of:

```text
project/

main.py
database.py
mysql.py
mongodb.py
sqlite.py
login.py
register.py
jwt.py
email.py
sms.py
```

You organize it as:

```text
project/

main.py

database/
    mysql.py
    mongodb.py
    sqlite.py

auth/
    login.py
    register.py
    jwt.py

notification/
    email.py
    sms.py
```

Much cleaner and easier to maintain.

---

# What Is a Package?

A **package** is simply a directory that contains Python modules.

Example:

```text
calculator/

add.py
subtract.py
multiply.py
divide.py
```

Instead of one large `calculator.py`, each operation has its own module.

---

# The `__init__.py` File

Traditionally, Python packages include a file named:

```text
__init__.py
```

This tells Python that the directory should be treated as a package.

Example:

```text
calculator/

__init__.py
add.py
subtract.py
multiply.py
divide.py
```

### Modern Python

Since Python 3.3, `__init__.py` is **not always required** because Python supports *namespace packages*.

However, most professional projects still include it because it:

* Makes the package explicit.
* Allows package-level initialization.
* Lets you control what is exported.
* Improves compatibility with tools and IDEs.

So it's a good habit to include it.

---

# Creating Your First Package

Create this structure:

```text
Lesson14/

main.py

calculator/
│
├── __init__.py
├── arithmetic.py
```

---

## `arithmetic.py`

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

---

## `main.py`

```python
from calculator.arithmetic import add

print(add(10, 5))
```

Expected output:

```text
15
```

---

# Importing Multiple Functions

```python
from calculator.arithmetic import add, subtract

print(add(20, 5))
print(subtract(20, 5))
```

---

# Importing the Whole Module

```python
import calculator.arithmetic

print(calculator.arithmetic.add(10, 5))
```

---

# Project Structure Used in Real Companies

Here's a simplified example of a production Python project:

```text
project/

main.py

config/
│── __init__.py
│── settings.py

database/
│── __init__.py
│── mysql.py
│── postgres.py

services/
│── __init__.py
│── payment.py
│── email.py

utils/
│── __init__.py
│── helper.py
│── validator.py
```

Each folder is a package, and each `.py` file is a module.

---

# AI Project Example

A chatbot project might look like:

```text
ai_chatbot/

main.py

llm/
│── __init__.py
│── openai_client.py
│── prompt_builder.py

memory/
│── __init__.py
│── vector_store.py

database/
│── __init__.py
│── mysql.py

utils/
│── __init__.py
│── logger.py
```

As your projects grow, this organization becomes essential.

---

# What Does `__init__.py` Do?

It can be empty:

```python
# __init__.py
```

Or it can expose selected functions.

For example:

```python
from .arithmetic import add, subtract
```

Now you can write:

```python
from calculator import add

print(add(10, 5))
```

instead of:

```python
from calculator.arithmetic import add
```

This gives package authors control over what users import.

---

# Exercise 1

Create this folder structure:

```text
Lesson14/

main.py

calculator/
│
├── __init__.py
├── arithmetic.py
```

### `arithmetic.py`

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

### `__init__.py`

```python
from .arithmetic import add, subtract
```

### `main.py`

```python
from calculator import add, subtract

print(add(10, 5))
print(subtract(20, 5))
```

Expected output:

```text
15
15
```

---

# Challenge

Expand your package:

```text
calculator/

__init__.py
arithmetic.py
advanced.py
```

### `advanced.py`

```python
def power(a, b):
    return a ** b


def square(num):
    return num * num
```

Update `__init__.py`:

```python
from .arithmetic import add, subtract
from .advanced import power, square
```

Now in `main.py`:

```python
from calculator import add, square, power

print(add(5, 5))
print(square(8))
print(power(2, 10))
```

Expected output:

```text
10
64
1024
```

---

# Common Mistakes

### 1. Forgetting the package name

Incorrect:

```python
from arithmetic import add
```

Correct:

```python
from calculator.arithmetic import add
```

---

### 2. Missing `__init__.py`

Modern Python can often work without it, but many projects and tools expect it. Including it is a good practice.

---

### 3. Using incorrect relative imports

Inside the package:

```python
from .arithmetic import add
```

The leading `.` means "import from the current package."

---

# Module 4 Summary

After completing this module, you'll be able to:

* ✅ Understand the difference between a module and a package.
* ✅ Create package folders.
* ✅ Use `__init__.py`.
* ✅ Import modules from packages.
* ✅ Re-export functions from `__init__.py`.
* ✅ Read the structure of professional Python and AI projects.

---
