# Lesson 11 – Module 4: Encapsulation, Polymorphism & Abstraction

> **Goal:** Master the remaining three pillars of Object-Oriented Programming (OOP). These concepts are heavily used in **Python, Magento 2, Laravel, Java, C#**, and almost every large software project.

---

# Module Roadmap

```
OOP
├── ✅ Class & Object
├── ✅ Constructor
├── ✅ Inheritance
├── ▶ Encapsulation
├── ▶ Polymorphism
└── ▶ Abstraction
```

---

# 1. Encapsulation

## Definition

Encapsulation means **keeping data (variables) and methods together inside one class while controlling direct access to them.**

Instead of allowing anyone to change variables directly, we expose only the required functionality.

Think of it like an ATM.

```
Customer
     │
     ▼
Withdraw()
     │
     ▼
Bank Account Balance
```

You cannot directly change your bank balance.

You must use

```
deposit()
withdraw()
```

methods.

This is encapsulation.

---

# Why Encapsulation?

Without encapsulation

```python
class Employee:
    salary = 50000

emp = Employee()

emp.salary = -100000
```

Output

```
Salary = -100000
```

This makes no sense.

Instead,

```
Only deposit()
Only increase_salary()
```

should change the salary.

---

# Access Modifiers in Python

Unlike Java/C++, Python doesn't enforce access modifiers strictly. It uses naming conventions.

| Modifier  | Syntax   | Access                                  |
| --------- | -------- | --------------------------------------- |
| Public    | `name`   | Anywhere                                |
| Protected | `_name`  | Inside class & subclasses (convention)  |
| Private   | `__name` | Name-mangled; intended for internal use |

---

## Public Variable

```python
class Student:

    def __init__(self):
        self.name = "Rahul"

student = Student()

print(student.name)
```

Output

```
Rahul
```

Anyone can access it.

---

## Protected Variable

```python
class Student:

    def __init__(self):
        self._marks = 90

student = Student()

print(student._marks)
```

Output

```
90
```

Python allows access, but `_marks` indicates **"don't access this directly outside the class unless necessary."**

---

## Private Variable

```python
class Student:

    def __init__(self):
        self.__salary = 70000

student = Student()

print(student.__salary)
```

Output

```
AttributeError
```

Python internally renames it (name mangling), so direct access fails.

---

### Correct Way

```python
class Employee:

    def __init__(self):
        self.__salary = 70000

    def show_salary(self):
        print(self.__salary)

emp = Employee()

emp.show_salary()
```

Output

```
70000
```

---

## Private Methods

Methods can also be made private.

```python
class Car:

    def __start_engine(self):
        print("Engine Started")

    def drive(self):
        self.__start_engine()
        print("Car is Moving")

car = Car()

car.drive()
```

Output

```
Engine Started
Car is Moving
```

But

```python
car.__start_engine()
```

gives

```
AttributeError
```

---

## Real Magento Example

```php
private $logger;
private $productRepository;
```

Magento keeps dependencies private so other classes cannot modify them directly.

Methods like

```
execute()

save()

get()

delete()
```

interact with these properties instead.

---

# 2. Polymorphism

## Definition

**Poly = Many**

**Morph = Forms**

One method.

Different behavior.

---

## Example

Dog

```
Sound = Bark
```

Cat

```
Sound = Meow
```

Cow

```
Sound = Moo
```

All have

```
sound()
```

but each behaves differently.

---

### Example

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


class Cow:

    def sound(self):
        print("Moo")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()
```

Output

```
Bark
Meow
Moo
```

Notice the loop doesn't care which object it has. It simply calls `sound()`, and each class provides its own implementation.

---

## Method Overriding

```python
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")

dog = Dog()

dog.sound()
```

Output

```
Bark
```

The child class overrides the parent implementation.

---

## Polymorphism in Magento

Magento has many classes implementing the same interface.

Example:

```
save()

delete()

getById()
```

Different repositories implement these methods differently, but client code can call the same method names.

---

# 3. Abstraction

## Definition

Abstraction means:

> Show only what is necessary and hide the implementation details.

Example:

```
Drive Car
```

You press

```
Start Button
```

You don't need to know:

* Fuel injection
* Engine timing
* Spark plugs
* Battery voltage

The complexity is hidden.

---

## Python Abstract Class

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

This class cannot be instantiated.

```python
animal = Animal()
```

Output

```
TypeError
```

---

## Child Class

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")

dog = Dog()

dog.sound()
```

Output

```
Bark
```

---

## What if Child Doesn't Implement?

```python
class Dog(Animal):
    pass

dog = Dog()
```

Output

```
TypeError
```

Python forces you to implement all abstract methods.

---

## Magento Example

Magento relies heavily on abstraction.

Instead of depending on concrete classes, code often depends on interfaces.

```php
ProductRepositoryInterface
```

The actual implementation can change, but code using the interface remains the same. This is a core reason Magento favors dependency injection and interfaces.

---

# Comparison

| Feature       | Purpose                         | Example                        |
| ------------- | ------------------------------- | ------------------------------ |
| Encapsulation | Protect data                    | Private variables & methods    |
| Inheritance   | Reuse code                      | Child extends Parent           |
| Polymorphism  | Same method, different behavior | `sound()` in different animals |
| Abstraction   | Hide implementation             | Abstract class or interface    |

---

# All Four Pillars Together

```
                OOP

                  ▲
                  │

     Encapsulation
            │
Inheritance ─── Polymorphism
            │
       Abstraction
```

Each pillar solves a different problem, and together they make code easier to maintain, extend, and test.

---

# Interview Questions

### Q1. What is Encapsulation?

**Answer:** Wrapping data and methods together in a class while restricting direct access to internal data.

---

### Q2. Difference between Encapsulation and Abstraction?

| Encapsulation             | Abstraction                         |
| ------------------------- | ----------------------------------- |
| Protects data             | Hides implementation                |
| Uses access control       | Uses abstract classes or interfaces |
| Focuses on internal state | Focuses on exposed behavior         |

---

### Q3. What is Polymorphism?

**Answer:** The ability to use the same method name with different implementations depending on the object.

---

### Q4. What is Method Overriding?

**Answer:** When a child class provides its own implementation of a method already defined in the parent class.

---

### Q5. Can we create an object of an abstract class?

**Answer:** No. Abstract classes cannot be instantiated directly. A concrete subclass must implement all abstract methods first.

---

# Mini Exercise

Create a small program with:

1. An abstract class `Shape` containing an abstract method `area()`.
2. Two child classes:

   * `Rectangle`
   * `Circle`
3. Use encapsulation by making dimensions private.
4. Create objects of both classes and print their areas.
5. Store both objects in a list and call `area()` on each to demonstrate polymorphism.

---

## Lesson 11 Progress

* ✅ Module 1 – Classes & Objects
* ✅ Module 2 – Constructors & Inheritance
* ✅ Module 3 – Access Modifiers & Methods
* ✅ **Module 4 – Encapsulation, Polymorphism & Abstraction**
* ▶️ **Next:** **Lesson 11 – Module 5: Magic (Dunder) Methods & Operator Overloading**, where you'll learn methods like `__init__`, `__str__`, `__len__`, `__repr__`, `__eq__`, and how Python objects behave behind the scenes. These are frequently used in advanced Python libraries and AI frameworks.
