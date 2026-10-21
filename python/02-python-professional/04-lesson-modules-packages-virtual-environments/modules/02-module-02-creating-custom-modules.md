# Lesson 14 – Module 2

# Creating Your Own Modules

## Module Objective

In Module 1, you learned how to use Python's built-in modules like `math`, `random`, and `datetime`.

Now you'll learn how to create your **own modules**, so your code can be reused across multiple programs.

This is the same concept used in professional software development.

---

# What Problem Does This Solve?

Suppose you write a calculator program.

You create functions like:

```python
add()
subtract()
multiply()
divide()
```

Now imagine another project also needs these functions.

Instead of copying and pasting them everywhere, you can place them in one file and import them wherever needed.

This follows the **DRY (Don't Repeat Yourself)** principle.

---

# Real-World Example

### Without Modules

```text
Project A
---------
main.py
(add function copied)

Project B
---------
main.py
(add function copied)

Project C
---------
main.py
(add function copied)
```

Problems:

* Duplicate code
* Difficult to maintain
* Bugs must be fixed in every project

---

### With Modules

```text
calculator.py

Project A
main.py

Project B
main.py

Project C
main.py
```

All projects share the same module.

If you improve `calculator.py`, every project benefits.

---

# Creating Your First Module

A module is simply a Python file.

Create:

```text
calculator.py
```

Inside it, write:

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b
```

Nothing special is required—any `.py` file can be imported as a module.

---

# Project Structure

Create this folder:

```text
Lesson14/

│── calculator.py
│── main.py
```

---

# Using Your Module

Create `main.py`:

```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))
```

---

## How Python Executes This

When you run:

```bash
python3 main.py
```

Python:

1. Starts executing `main.py`.
2. Sees `import calculator`.
3. Looks for `calculator.py` in the current directory.
4. Loads it into memory.
5. Makes its functions available through the `calculator` name.
6. Continues executing the remaining code.

This is the basic workflow behind every `import`.

---

# Expected Output

```text
15
5
50
2.0
```

---

# How `import` Works Internally

When you write:

```python
import calculator
```

Python creates something like:

```text
calculator
│
├── add()
├── subtract()
├── multiply()
└── divide()
```

To access a function, you use **dot notation**:

```python
calculator.add(10, 5)
```

Just like:

```python
math.sqrt(25)
datetime.datetime.now()
```

The module name acts as a namespace, preventing name conflicts.

---

# What Happens If You Forget the Module Name?

If you write:

```python
add(10, 5)
```

Python will raise:

```text
NameError: name 'add' is not defined
```

because `add()` belongs to the `calculator` module.

---

# Exercise 1

Create these files:

```text
Lesson14/
│── calculator.py
│── main.py
```

### `calculator.py`

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b
```

### `main.py`

```python
import calculator

print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))
print("Division:", calculator.divide(10, 5))
```

### Expected Output

```text
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
```

---

# Common Beginner Mistakes

### 1. Different file names

```text
calculator.py
```

and

```python
import calculator
```

must match exactly (including capitalization on Linux).

---

### 2. Both files should be in the same folder

```text
Lesson14/
│── calculator.py
│── main.py
```

Otherwise, Python won't find the module.

---

### 3. Avoid naming your file after built-in modules

Bad examples:

```text
math.py
random.py
datetime.py
json.py
```

If you create a file named `math.py`, then:

```python
import math
```

will import **your file** instead of Python's built-in `math` module. This is called **module shadowing** and is a common source of confusion.

---

# Mini Challenge

Add two more functions to `calculator.py`:

```python
def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b
```

Then call them from `main.py`:

```python
print("Power:", calculator.power(2, 5))
print("Modulus:", calculator.modulus(17, 5))
```

Expected output:

```text
Power: 32
Modulus: 2
```

---

## Module 2 Summary

By the end of this module, you'll be able to:

* ✅ Create your own Python module.
* ✅ Import it into another file.
* ✅ Understand how Python resolves imports.
* ✅ Use dot notation to access module members.
* ✅ Avoid common import-related mistakes.

### Your Task

1. Create `calculator.py`.
2. Create `main.py`.
3. Complete the mini challenge by adding `power()` and `modulus()`.
4. Run `main.py` and share:

   * The code for both files.
   * The output you received.

Once you've done that, we'll move to **Module 3: Different Import Styles (`from ... import`, aliases, and wildcard imports)** before introducing packages, so you build the concepts step by step.
