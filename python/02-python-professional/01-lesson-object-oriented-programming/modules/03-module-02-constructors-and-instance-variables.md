# Lesson 11 – Module 2

## Constructors (`__init__`) & Instance Variables

**Estimated Time:** 35–45 minutes

**Difficulty:** ⭐⭐

---

# Module Objective

By the end of this module, you'll understand:

* Constructors (`__init__`)
* `self`
* Instance Variables
* Creating multiple objects with different data

---

# 1. What is a Constructor?

A constructor is a special method that runs **automatically** when an object is created.

PHP (Magento):

```php
public function __construct($name)
{
    $this->name = $name;
}
```

Python:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

The concept is the same.

The syntax is different.

---

# 2. What is `__init__()`?

`__init__()` is Python's constructor.

It runs automatically when you do:

```python
student = Student("Bhupendra")
```

You never call it directly.

---

# 3. What is `self`?

This is the biggest difference from PHP.

PHP:

```php
$this->name = $name;
```

Python:

```python
self.name = name
```

Think of:

```text
$this  (PHP)

↓

self    (Python)
```

Both refer to the **current object**.

---

# 4. Instance Variables

Current approach:

```python
student.show_name("Bhupendra")
```

The object doesn't remember the name.

Better:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)
```

Now:

```python
student = Student("Bhupendra")

student.show_name()
```

Output

```text
Bhupendra
```

The object stores its own data.

---

# 5. Multiple Instance Variables

```python
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def show_details(self):
        print(self.name)
        print(self.age)
```

Usage:

```python
student = Student("Bhupendra", 37)

student.show_details()
```

Output

```text
Bhupendra
37
```

---

# 6. Multiple Objects

Each object has its own data.

```python
student1 = Student("Bhupendra", 37)

student2 = Student("Rahul", 25)
```

Calling

```python
student1.show_details()
```

Output

```text
Bhupendra
37
```

Calling

```python
student2.show_details()
```

Output

```text
Rahul
25
```

Each object has independent state.

---

# 7. Why Use Constructors?

Without constructor:

```python
student = Student()

student.show_name("Bhupendra")
```

Every method needs the data again.

With constructor:

```python
student = Student("Bhupendra")

student.show_name()
```

Cleaner and easier to maintain.

---

# Magento Comparison

PHP:

```php
$product = new Product("Laptop");

$product->getName();
```

Python:

```python
product = Product("Laptop")

product.get_name()
```

Almost identical.

---

# Best Practices

✅ Store object data inside the constructor.

```python
self.name = name
```

✅ Use `self` only for object-specific data.

---

# Common Mistake

Wrong:

```python
class Student:

    def __init__(name):
        self.name = name
```

`self` is missing.

Correct:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

---

# Exercises

## Exercise 1

Create:

```python
class Car
```

Constructor:

```python
brand
```

Method:

```python
show_brand()
```

Create two objects.

Example:

```python
Car("BMW")

Car("Audi")
```

---

## Exercise 2

Create:

```python
class Employee
```

Constructor

```python
name

salary
```

Method

```python
show_details()
```

Print:

```text
Name : Bhupendra

Salary : 85000
```

---

## Exercise 3

Create:

```python
class Product
```

Constructor

```python
sku

name

price
```

Method

```python
show_product()
```

---

## Exercise 4

Create **two Product objects** with different values.

Call:

```python
show_product()
```

for both.

---

# Mini Project

## Student Report

Create

```python
class Student
```

Constructor

```python
name

age

marks
```

Methods

```python
show_details()

is_pass()
```

Rules

If marks

```text
>=35
```

Print

```text
PASS
```

Else

```text
FAIL
```

---

# Where You'll Use This in AI

Later we'll write code like this:

```python
agent = CustomerSupportAgent(
    model="gpt-5.5",
    temperature=0.2
)
```

That object stores its configuration using `__init__()`, just like the `Student` or `Product` objects you're creating now.

---

## Module Outcome

After this module, you'll understand:

* ✅ `__init__()`
* ✅ `self`
* ✅ Instance Variables
* ✅ Object Initialization
* ✅ Multiple Objects

---

### ⏱️ Target Time

**30–40 minutes**

---

## Small Note

From **Module 3 (Inheritance)** onward, I'll explain the concepts by comparing **Python ↔ Magento/PHP** wherever possible. Since you're already comfortable with OOP in Magento, I don't want to spend time reteaching ideas you already know—I only want to teach you how Python expresses those same concepts. This should significantly speed up the rest of the OOP lesson.
