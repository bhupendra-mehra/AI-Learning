# Code Review

## 1. Abstraction ✅

You correctly created an abstract class.

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

✔ Perfect.

This ensures every child class **must** implement `area()`.

---

## 2. Inheritance ✅

```python
class Rectangle(Shape):
```

and

```python
class Circle(Shape):
```

Both inherit from `Shape`.

✔ Correct.

---

## 3. Encapsulation ✅

You used private variables.

```python
self.__length
self.__width
self.__radius
```

Excellent.

These variables cannot be accessed directly outside the class.

Example:

```python
rect = Rectangle()

print(rect.__length)
```

Output

```
AttributeError
```

---

## 4. Polymorphism ✅

This is the best part.

```python
shapes = [Rectangle(5,6), Circle(5)]

for shape in shapes:
    shape.area()
```

The loop doesn't know whether it's dealing with a rectangle or a circle.

It simply calls

```python
shape.area()
```

Each object behaves differently.

This is **runtime polymorphism**.

---

# Output

Rectangle

```
Area of Rectangle : 30
```

Circle

```
Area of Circle : 78.5
```

✔ Correct.

---

# One Small Improvement

Currently,

```python
def area(self):
    print(...)
```

works fine.

But in real projects, especially AI, Django, Flask, Magento APIs, etc., methods usually **return values instead of printing them**.

Instead of

```python
def area(self):
    print(self.__length * self.__width)
```

prefer

```python
def area(self):
    return self.__length * self.__width
```

Then

```python
for shape in shapes:
    print(shape.area())
```

Why?

Because another function can reuse the returned value.

Example

```python
total += shape.area()
```

Printing cannot be reused.

Returning can.

---

# Even Better Version

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius ** 2


shapes = [
    Rectangle(5, 6),
    Circle(5)
]

for shape in shapes:
    print(shape.area())
```

Output

```
30
78.5
```

This style is preferred in production code.

---

# Interview Discussion

If an interviewer asks:

> **Where are all four OOP pillars used in your program?**

You can answer:

| OOP Pillar    | Used In                                            |
| ------------- | -------------------------------------------------- |
| Encapsulation | `__length`, `__width`, `__radius`                  |
| Inheritance   | `Rectangle(Shape)`, `Circle(Shape)`                |
| Abstraction   | `Shape` abstract class with `area()`               |
| Polymorphism  | `shape.area()` behaves differently for each object |

This is a concise and complete explanation.

---

# Score

| Concept              | Score |
| -------------------- | ----- |
| Abstract Class       | ⭐⭐⭐⭐⭐ |
| Inheritance          | ⭐⭐⭐⭐⭐ |
| Encapsulation        | ⭐⭐⭐⭐⭐ |
| Polymorphism         | ⭐⭐⭐⭐⭐ |
| Code Quality         | ⭐⭐⭐⭐☆ |
| Production Readiness | ⭐⭐⭐⭐☆ |

**Overall: 9.5/10** 🎉

The only deduction is using `print()` instead of `return` in `area()`. That's a common beginner pattern and an easy improvement.

---

## Lesson 11 Status

* ✅ Module 1 – Classes & Objects
* ✅ Module 2 – Constructors & Inheritance
* ✅ Module 3 – Access Modifiers & Methods
* ✅ Module 4 – Encapsulation, Polymorphism & Abstraction

We're now ready for **Lesson 11 – Module 5: Magic (Dunder) Methods & Operator Overloading**, which will complete Lesson 11.
