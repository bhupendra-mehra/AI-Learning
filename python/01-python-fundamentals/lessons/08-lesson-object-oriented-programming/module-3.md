# Lesson 11 – Module 3

## Inheritance

**Estimated Time:** 30–40 minutes

**Difficulty:** ⭐⭐⭐

---

# Module Objective

By the end of this module, you'll understand:

* Inheritance
* Parent Class
* Child Class
* `super()`
* Method Overriding
* Code Reuse

---

# 1. What is Inheritance?

Inheritance allows one class to **reuse** another class.

Instead of writing the same code again,

we inherit it.

---

## Real World

```
Animal
   │
 ┌─┴────────┐
Dog       Cat
```

Dog and Cat inherit common behavior from Animal.

---

# Magento Example

You already do this.

```php
class CustomProduct extends Product
```

Python

```python
class Dog(Animal):
```

Exactly the same idea.

---

# 2. Parent Class

```python
class Animal:

    def eat(self):
        print("Animal is eating")
```

---

# 3. Child Class

```python
class Dog(Animal):
    pass
```

Now Dog automatically has:

```python
eat()
```

---

# Example

```python
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    pass


dog = Dog()

dog.eat()
```

Output

```
Animal is eating
```

Dog inherited the method.

---

# 4. Adding New Methods

```python
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Woof!")
```

Usage

```python
dog = Dog()

dog.eat()

dog.bark()
```

Output

```
Animal is eating

Woof!
```

---

# 5. Method Overriding

Parent

```python
class Animal:

    def sound(self):
        print("Animal Sound")
```

Child

```python
class Dog(Animal):

    def sound(self):
        print("Woof!")
```

Usage

```python
dog = Dog()

dog.sound()
```

Output

```
Woof!
```

Child replaces the parent's implementation.

---

# 6. `super()`

Sometimes we want to use the parent implementation first.

Example

```python
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        super().sound()

        print("Woof!")
```

Output

```
Animal Sound

Woof!
```

---

# 7. Constructor Inheritance

Parent

```python
class Animal:

    def __init__(self, name):
        self.name = name
```

Child

```python
class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)
```

Usage

```python
dog = Dog("Tommy")

print(dog.name)
```

Output

```
Tommy
```

---

# Magento Comparison

PHP

```php
parent::__construct(...)
```

Python

```python
super().__init__(...)
```

This is one of the biggest syntax differences.

---

# Best Practices

Use inheritance only when there is an **"is-a"** relationship.

Good

```
Dog is an Animal

Car is a Vehicle
```

Bad

```
Customer is an Address ❌

Order is a Product ❌
```

---

# Exercises

## Exercise 1

Create

```python
class Vehicle
```

Method

```python
start()
```

Create

```python
class Car(Vehicle)
```

Call

```python
start()
```

using a `Car` object.

---

## Exercise 2

Add

```python
drive()
```

inside `Car`.

Call both

```python
start()

drive()
```

---

## Exercise 3

Create

```python
class Person
```

Method

```python
show_role()
```

Print

```
Person
```

Create

```python
class Teacher(Person)
```

Override

```python
show_role()
```

Print

```
Teacher
```

---

## Exercise 4

Modify the previous exercise.

Inside

```python
Teacher.show_role()
```

Call

```python
super().show_role()
```

Then print

```
Teacher
```

Expected Output

```
Person

Teacher
```

---

# Mini Project

## Product System

Create

```python
class Product
```

Constructor

```
name

price
```

Method

```python
show_product()
```

Print

```
Name

Price
```

---

Create

```python
class Electronics(Product)
```

Additional Constructor

```
brand
```

Use

```python
super().__init__()
```

Method

```python
show_details()
```

Print

```
Name

Price

Brand
```

---

# AI Example

Soon we'll write classes like:

```python
class BaseAgent:
    ...
```

Then create specialized agents:

```python
class CustomerSupportAgent(BaseAgent):

class ResearchAgent(BaseAgent):

class CodingAgent(BaseAgent)
```

Each agent inherits common functionality from the base class while adding its own behavior.

---

# Module Outcome

After this module you'll understand:

* ✅ Parent Class
* ✅ Child Class
* ✅ Method Inheritance
* ✅ Method Overriding
* ✅ `super()`
* ✅ Constructor Inheritance

---

## One Important Difference Between PHP and Python

In PHP, constructors are often called automatically through dependency injection in frameworks like Magento.

In Python, you'll frequently create objects yourself:

```python
agent = CustomerSupportAgent(...)
```

So understanding `__init__()` and `super()` is especially important—they're used extensively in frameworks like FastAPI, LangChain, and the OpenAI SDK.

---

⏱️ **Target Time:** **30–40 minutes**

Complete the exercises and the mini project, and then we'll move to **Module 4**, where we'll cover encapsulation, polymorphism, and abstraction in a concise, interview-focused way.
