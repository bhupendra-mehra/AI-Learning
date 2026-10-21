# Python Foundation Revision (Lessons 1–10)

**Estimated Time:** 60–90 minutes

---

# Lesson 1 – Python Basics

### Topics

* What is Python?
* Running Python
* Comments
* `print()`

### Syntax

```python
print("Hello World")
```

### AI Usage

Python is the primary language for AI, Machine Learning, APIs, and Automation.

---

# Lesson 2 – Variables

### Topics

* Variables
* Naming conventions
* Assignment

```python
name = "Bhupendra"
age = 37
price = 100.5
```

### Best Practice

```python
product_price
```

Avoid

```python
x
a
abc
```

---

# Lesson 3 – Data Types

### Types

```python
str
int
float
bool
list
tuple
set
dict
```

### Check Type

```python
print(type(age))
```

---

# Lesson 4 – Input & Output

### Input

```python
name = input("Enter Name: ")
```

### Type Conversion

```python
age = int(input("Age: "))
price = float(input("Price: "))
```

---

# Lesson 5 – Operators

### Arithmetic

```python
+
-
*
/
/
//
%
**
```

### Comparison

```python
==
!=
>
<
>=
<=
```

### Assignment

```python
+=
-=
*=
```

---

# Lesson 6 – Conditions

### Syntax

```python
if:
elif:
else:
```

Example

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

# Lesson 7 – Logical Operators

### Operators

```python
and
or
not
```

Example

```python
if logged_in and in_stock:
```

Real Project

* Login
* Checkout
* Discount
* Eligibility

---

# Lesson 8 – Loops

## for

```python
for product in products:
    print(product)
```

## while

```python
while password != "1234":
```

## break

Exit loop.

## continue

Skip current iteration.

## pass

Placeholder.

---

# Lesson 9 – Functions

## Create

```python
def greet():
    print("Hello")
```

## Parameters

```python
def greet(name):
```

## Return

```python
return total
```

## Default Parameters

```python
def greet(name="Guest"):
```

## Keyword Arguments

```python
employee(age=37, name="Bhupendra")
```

## *args

```python
def add(*numbers):
```

## **kwargs

```python
def product(**details):
```

## Lambda

```python
square = lambda x: x * x
```

## Scope

* Local
* Global

---

# Lesson 10 – Collections

## List

```python
products = []
```

Used for:

* Products
* Orders
* Chat History

---

## Tuple

```python
config = ()
```

Used for fixed data.

---

## Set

```python
tags = {}
```

Unique values only.

> **Note:** An empty set must be created with `set()`, because `{}` creates an empty dictionary.

---

## Dictionary

```python
product = {
    "sku": "P001",
    "price": 50000
}
```

Most important collection for:

* JSON
* APIs
* OpenAI Responses
* Magento REST

---

# Most Important Built-in Functions

```python
print()

input()

len()

type()

int()

float()

str()

range()
```

---

# Python Concepts Learned

✅ Variables

✅ Data Types

✅ Input/Output

✅ Operators

✅ Conditions

✅ Logical Operators

✅ Loops

✅ Functions

✅ Lists

✅ Tuples

✅ Sets

✅ Dictionaries

---

# How These Connect in AI

| Python Concept | AI Usage                           |
| -------------- | ---------------------------------- |
| Variables      | Store prompts, tokens, model names |
| Conditions     | Decide next action                 |
| Loops          | Process messages/documents         |
| Functions      | Tool calling and reusable logic    |
| Lists          | Chat history, search results       |
| Dictionaries   | JSON, API responses, LLM outputs   |
| Sets           | Remove duplicate keywords          |
| Tuples         | Fixed return values                |

---

# Final Revision Project (Lessons 1–10)

## Project: Student Management System

**Estimated Time:** 30–45 minutes

### Objective

Build a console-based application that uses everything you've learned in Lessons 1–10.

### Requirements

Create a menu:

```text
========= MENU =========

1. Add Student
2. Show Students
3. Search Student
4. Update Marks
5. Delete Student
6. Exit
```

### Student Structure

Store each student as a dictionary inside a list.

Example:

```python
{
    "roll_no": 101,
    "name": "Rahul",
    "age": 20,
    "marks": 85
}
```

### Functions

Implement these functions:

```python
add_student()

show_students()

search_student()

update_marks()

delete_student()

main_menu()
```

### Concepts Covered

* Variables
* Input/Output
* Data Types
* Operators
* Conditions
* Loops
* Functions
* Lists
* Dictionaries

### Bonus (Optional)

* Prevent duplicate `roll_no`.
* Show `"Student Not Found"` when appropriate.
* Display the average marks of all students.

---

# Revision Complete

Once you finish this project, you should be fully refreshed and ready to start **Lesson 11 – Object-Oriented Programming (OOP)**.

---
