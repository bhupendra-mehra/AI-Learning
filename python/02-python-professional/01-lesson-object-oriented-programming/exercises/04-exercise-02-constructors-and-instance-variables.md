# Quick Review

## Exercise 1 – Car

```python
class Car:

    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(self.brand)
```

✅ Perfect

You correctly used:

* Constructor
* `self`
* Instance variable
* Method

---

## Exercise 2 – Employee

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")
```

✅ Perfect

Exactly how I would expect it.

---

## Exercise 3 – Product

```python
class Product:

    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price
```

✅ Perfect

This is very similar to how Magento models hold product data.

---

## Exercise 4

```python
mobile = Product("000002", "Iphone", 99.99)

charger = Product("000003", "Charger", 9.99)
```

✅ Correct

You proved that each object maintains its own state.

---

## Mini Project

```python
class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
```

✅ Excellent

The methods are clean and readable.

---

# Senior Developer Review

Only a few small improvements.

---

## 1. Avoid Unnecessary Type Casting

Current:

```python
print(f"Age = {int(self.age)}")
```

and

```python
if float(self.marks) >= 35:
```

Since you're already storing:

```python
student = Student("Bhupendra", 37, 40)
```

`age` is already an `int` and `marks` is already a number.

So simply write:

```python
print(f"Age = {self.age}")
```

and

```python
if self.marks >= 35:
```

Avoid unnecessary conversions.

---

## 2. Method Naming

Instead of:

```python
is_pass()
```

I would probably use:

```python
show_result()
```

because your method prints the result.

Typically:

* Methods starting with `is_` return a Boolean.
* Methods starting with `show_` display output.

For example:

```python
def is_pass(self):
    return self.marks >= 35
```

Then:

```python
if student.is_pass():
    print("PASS")
else:
    print("FAIL")
```

You'll see this style often in professional code.

---

# One Important OOP Principle

Right now, you're combining **business logic** and **display logic**.

For learning, that's perfectly fine.

In larger applications, we often separate them.

Example:

```python
def is_pass(self):
    return self.marks >= 35
```

Then elsewhere:

```python
result = student.is_pass()

print("PASS" if result else "FAIL")
```

This makes the class easier to reuse in different contexts (console app, web app, API, etc.).

---

# Magento Comparison

This:

```python
student = Student("Bhupendra", 37, 40)
```

is conceptually the same as:

```php
$product = new Product($sku, $name, $price);
```

And:

```python
student.show_details()
```

is similar to calling:

```php
$product->getName();
```

The syntax differs, but the object-oriented design is the same.

---

# Progress

```
Lesson 11

✅ Module 1 – Classes & Objects
✅ Module 2 – Constructors & Instance Variables
⏳ Module 3 – Inheritance
⏳ Module 4 – Encapsulation, Polymorphism & Abstraction
⏳ Module 5 – Final Project
```

---

# Updated Time Estimate

Originally:

* Module 1: ~45 minutes
* Module 2: ~45 minutes

You completed both comfortably.

Because of that, I think we can also compress **Module 3 (Inheritance)**. Since you already know inheritance from Magento, we'll focus on:

* Python inheritance syntax
* `super()`
* Method overriding
* Key differences from PHP
