# Lesson 14 – Module 3

# Different Ways to Import Modules

## Module Objective

In Module 2, you imported your module like this:

```python
import calculator
```

However, Python provides several ways to import modules. As you read open-source AI projects or professional codebases, you'll encounter all of them.

By the end of this module, you'll know:

* When to use each import style.
* Their advantages and disadvantages.
* Which style is preferred in production code.

---

# There are 4 Common Import Styles

| Style                     | Example                      | Most Common |
| ------------------------- | ---------------------------- | ----------- |
| Import Entire Module      | `import calculator`          | ⭐⭐⭐⭐⭐       |
| Import Specific Functions | `from calculator import add` | ⭐⭐⭐⭐⭐       |
| Import with Alias         | `import calculator as calc`  | ⭐⭐⭐⭐        |
| Wildcard Import           | `from calculator import *`   | ⭐ (Avoid)   |

Let's explore each one.

---

# Method 1 — Import the Entire Module

This is what you've already learned.

```python
import calculator

print(calculator.add(10, 5))
print(calculator.multiply(4, 8))
```

### How it works

```
calculator
│
├── add()
├── subtract()
├── multiply()
└── divide()
```

You access everything through the module name.

### Advantages

* Clear where each function comes from.
* No naming conflicts.
* Best for large projects.
* Preferred in professional code.

### Disadvantage

You must type the module name each time.

---

# Method 2 — Import Specific Functions

Instead of importing the whole module:

```python
from calculator import add

print(add(10, 5))
```

Notice:

No need to write:

```python
calculator.add()
```

because `add()` is imported directly into your current file.

---

## Import Multiple Functions

```python
from calculator import add, subtract

print(add(20, 5))
print(subtract(20, 5))
```

---

### Advantages

* Less typing.
* Cleaner code for small programs.

### Disadvantages

If two modules contain a function with the same name, Python won't know which one you mean.

Example:

```python
from math import sqrt
from numpy import sqrt
```

Now which `sqrt()` is being called? The later import overwrites the earlier one, making the code confusing.

---

# Method 3 — Import with an Alias

You can rename the module during import.

```python
import calculator as calc

print(calc.add(10, 5))
```

This is especially useful for modules with long names.

For example:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

These aliases are used in almost every AI, data science, and machine learning project.

### Why?

Instead of:

```python
import matplotlib.pyplot

matplotlib.pyplot.plot(...)
```

you write:

```python
import matplotlib.pyplot as plt

plt.plot(...)
```

Much shorter and easier to read.

---

# Method 4 — Wildcard Import

```python
from calculator import *

print(add(5, 5))
print(subtract(10, 5))
```

Everything from `calculator.py` is imported automatically.

---

### Why This Is Discouraged

Suppose:

```python
calculator.py
```

contains:

```python
def print():
    return "Hello"
```

Now:

```python
from calculator import *

print("Hello")
```

Which `print()` gets called?

* Python's built-in `print()`
* Your custom `print()`

This can cause hard-to-find bugs.

---

# Best Practice

Avoid:

```python
from module import *
```

unless you have a very specific reason.

---

# Professional Recommendation

| Style                         | Recommendation                 |
| ----------------------------- | ------------------------------ |
| `import module`               | ⭐⭐⭐⭐⭐ Best for most projects   |
| `from module import function` | ⭐⭐⭐⭐ Great for a few functions |
| `import module as alias`      | ⭐⭐⭐⭐⭐ Very common in AI        |
| `from module import *`        | ❌ Avoid                        |

---

# Real AI Examples

### NumPy

```python
import numpy as np

arr = np.array([1, 2, 3])
```

---

### Pandas

```python
import pandas as pd

df = pd.read_csv("employees.csv")
```

---

### Matplotlib

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3])
plt.show()
```

You'll see these aliases repeatedly throughout the rest of your AI roadmap.

---

# Exercise 1

Using your existing `calculator.py`, create four files.

---

### `main1.py`

```python
import calculator

print(calculator.add(10, 20))
```

---

### `main2.py`

```python
from calculator import add

print(add(10, 20))
```

---

### `main3.py`

```python
import calculator as calc

print(calc.add(10, 20))
```

---

### `main4.py`

```python
from calculator import *

print(add(10, 20))
```

Run all four.

---

## Challenge

Update your `calculator.py` with:

```python
def square(num):
    return num * num


def cube(num):
    return num * num * num
```

Now call these functions using **all four import styles**.

This will reinforce how each style works.

---

# Module 3 Summary

By the end of this module, you should understand:

* ✅ `import module`
* ✅ `from module import function`
* ✅ `import module as alias`
* ✅ `from module import *`
* ✅ When to use each style
* ✅ Why wildcard imports are discouraged
* ✅ Why aliases are widely used in AI and data science

---

## Before We Move to Module 4

Complete the exercise and challenge. Once you've confirmed they work, we'll continue to **Module 4 – Packages (`__init__.py`)**, where you'll learn how professional Python applications organize code across multiple folders instead of keeping everything in a single directory. This is the same structure you'll see in frameworks like Django, FastAPI, and AI libraries such as LangChain and Hugging Face.
