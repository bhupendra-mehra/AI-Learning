# Lesson 14 – Modules, Packages & Virtual Environments

### Estimated Time

**2–3 Hours**

### Modules

1. Introduction to Modules
2. Importing Modules
3. Creating Your Own Module
4. Packages
5. `pip` and Installing Libraries
6. Virtual Environments (`venv`)
7. Mini Project

### Mini Project

Build a small calculator package and use it from another Python file inside a virtual environment.

### Why This Lesson Matters for AI

Every AI project uses external libraries such as:

* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* TensorFlow
* PyTorch
* OpenAI SDK

Without understanding modules and virtual environments, managing AI projects becomes difficult.

---

# Module 1 — What is a Module?

A **module** is simply a Python file (`.py`) that contains reusable code.

Example:

```
math.py
```

may contain:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Instead of copying these functions into every program, you import the module.

---

## Python's Built-in Modules

Python includes many useful modules.

Examples:

| Module   | Purpose                      |
| -------- | ---------------------------- |
| math     | Mathematical functions       |
| random   | Random numbers               |
| datetime | Date and time                |
| os       | Operating system interaction |
| sys      | Python runtime information   |
| json     | JSON handling                |
| csv      | CSV files                    |

---

## Example 1

```python
import math

print(math.sqrt(25))
print(math.pi)
```

Output

```
5.0
3.141592653589793
```

---

## Example 2

```python
import random

print(random.randint(1, 10))
```

Each run gives a different number between 1 and 10.

---

## Example 3

```python
import datetime

today = datetime.datetime.now()

print(today)
```

---

# Different Import Styles

### Import the whole module

```python
import math

print(math.sqrt(16))
```

---

### Import specific functions

```python
from math import sqrt

print(sqrt(16))
```

---

### Import multiple functions

```python
from math import sqrt, pi

print(sqrt(64))
print(pi)
```

---

### Import with an alias

```python
import math as m

print(m.sqrt(49))
```

---

# Exercise 1

Create a file named:

```
lesson14_module1.py
```

Write code to:

1. Import `math`
2. Print `sqrt(144)`
3. Print `pi`
4. Import `random`
5. Print a random number from 1–100
6. Print the current date and time using `datetime`

---

## Expected Skills After Module 1

You should be able to:

* ✅ Understand what a module is
* ✅ Import built-in modules
* ✅ Use `import`, `from`, and aliases
* ✅ Use commonly used standard library modules

Once you've completed the exercise (or shared your code/output), we'll move to **Module 2: Creating Your Own Modules**, where you'll start organizing your own reusable Python code—the same approach used in production AI projects.
