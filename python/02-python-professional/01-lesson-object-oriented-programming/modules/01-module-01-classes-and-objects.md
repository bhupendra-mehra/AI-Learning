# Module 1 – Classes & Objects

**Estimated Time:** 40–50 minutes

---

# 1. What is OOP?

So far, we've written programs using **functions**.

Example:

```python
def calculate_discount():
    ...
```

As programs grow larger, managing everything through standalone functions becomes difficult.

OOP organizes code by grouping **data** and **behavior** together.

---

# Real-World Example

Think of a **Car**.

A car has:

### Data (Attributes)

* Brand
* Color
* Speed

### Behavior (Methods)

* Start
* Stop
* Accelerate

Instead of storing these separately, OOP combines them into one object.

---

# 2. What is a Class?

A **Class** is a blueprint.

Think of it as a design.

Example:

```
House Blueprint
      ↓
Many Houses
```

The blueprint is the **Class**.

Each house built from it is an **Object**.

---

# 3. What is an Object?

An **Object** is an actual instance created from a class.

Example:

Class

```
Car
```

Objects

```
My Car

Friend's Car

Office Car
```

Each object has its own values but follows the same blueprint.

---

# 4. Creating a Class

```python
class Student:
    pass
```

Here:

* `class` → keyword
* `Student` → class name (PascalCase convention)
* `pass` → placeholder

---

# 5. Creating an Object

```python
class Student:
    pass

student1 = Student()

print(student1)
```

You've created an object of the `Student` class.

---

# 6. Methods

Methods are functions inside a class.

```python
class Student:

    def greet(self):
        print("Hello Student")
```

Calling the method:

```python
student = Student()

student.greet()
```

Output:

```
Hello Student
```

---

# 7. What is `self`?

For now, remember this simple rule:

> **`self` refers to the current object.**

We'll explore it properly in Module 2 when we learn constructors.

---

# Magento Comparison

Magento:

```php
$product->getName();
```

Python:

```python
student.greet()
```

Both call a method on an object.

---

# Best Practices

* Class names → `Student`, `Product`, `Order` (PascalCase).
* Method names → `calculate_discount()`, `show_details()` (snake_case).
* One class should represent one concept.

---

# Exercises

## Exercise 1

Create an empty class:

```python
class Car:
    pass
```

Create **two objects** of `Car`.

Print both objects.

---

## Exercise 2

Create:

```python
class Animal:

    def sound(self):
        print("Animal Sound")
```

Create an object and call `sound()`.

---

## Exercise 3

Create:

```python
class Calculator:

    def add(self, a, b):
        print(a + b)
```

Call:

```python
calculator.add(10, 20)
```

---

## Exercise 4

Create a class:

```python
class Employee:

    def show_company(self):
        print("Encora")
```

Create **three objects** and call the method using each object.

---

## Mini Project

Create a `Student` class.

Methods:

```python
show_name(name)

show_marks(marks)
```

Example:

```python
student = Student()

student.show_name("Bhupendra")

student.show_marks(95)
```

---

# Where You'll Use This in AI Agent Development

Today you're creating:

```python
student = Student()
```

Later you'll create:

```python
agent = CustomerSupportAgent()

agent.answer()

agent.search_documents()

agent.call_tools()
```

The syntax is exactly the same—the class just represents an AI agent instead of a student.

---
