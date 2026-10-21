# Lesson 11 – Module 5

# Magic (Dunder) Methods & Operator Overloading

This is one of the most important Python topics because **everything in Python is an object**.

When you use:

```python
print(obj)
len(obj)
obj1 + obj2
obj1 == obj2
str(obj)
```

Python is actually calling **magic methods** behind the scenes.

These methods are also called **Dunder Methods** because they begin and end with double underscores (`__`).

Example:

```python
__init__
__str__
__len__
__eq__
__add__
```

---

# What are Magic Methods?

Suppose you write

```python
print("Hello")
```

Internally Python does something similar to

```python
"Hello".__str__()
```

Likewise,

```python
len("Python")
```

internally becomes

```python
"Python".__len__()
```

You usually don't call these methods directly—Python calls them for you.

---

# Common Magic Methods

| Method     | Called When             | Example                  |
| ---------- | ----------------------- | ------------------------ |
| `__init__` | Object creation         | `Person()`               |
| `__str__`  | `print(obj)`            | User-friendly string     |
| `__repr__` | `repr(obj)` / debugging | Developer representation |
| `__len__`  | `len(obj)`              | Object length            |
| `__eq__`   | `==`                    | Compare objects          |
| `__add__`  | `+`                     | Add objects              |
| `__lt__`   | `<`                     | Less than                |
| `__gt__`   | `>`                     | Greater than             |

---

# 1. `__init__`

You've already used it.

```python
class Student:

    def __init__(self, name):
        self.name = name

student = Student("Rahul")
```

When you create

```python
Student("Rahul")
```

Python automatically calls

```python
__init__()
```

---

# 2. `__str__`

Without `__str__`

```python
class Student:

    def __init__(self, name):
        self.name = name

student = Student("Rahul")

print(student)
```

Output

```text
<__main__.Student object at 0x7f...>
```

Not useful.

---

### With `__str__`

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student Name : {self.name}"

student = Student("Rahul")

print(student)
```

Output

```text
Student Name : Rahul
```

Much better.

---

## Real Life

Think of

```python
print(student)
```

as asking

> "How should I display this object?"

`__str__()` provides the answer.

---

# 3. `__repr__`

Suppose

```python
student = Student("Rahul")
```

Now

```python
repr(student)
```

calls

```python
__repr__()
```

Example

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student('{self.name}')"

student = Student("Rahul")

print(repr(student))
```

Output

```text
Student('Rahul')
```

---

## Difference Between `__str__` and `__repr__`

| `__str__`         | `__repr__`                     |
| ----------------- | ------------------------------ |
| User-friendly     | Developer-friendly             |
| Used by `print()` | Used by `repr()` and debugging |
| Easy to read      | Detailed representation        |

Example

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name : {self.name}"

    def __repr__(self):
        return f"Student(name='{self.name}')"

student = Student("Rahul")

print(student)
print(repr(student))
```

Output

```text
Name : Rahul
Student(name='Rahul')
```

---

# 4. `__len__`

Normally

```python
len("Python")
```

returns

```text
6
```

You can define your own length.

```python
class Playlist:

    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

playlist = Playlist(["Song1", "Song2", "Song3"])

print(len(playlist))
```

Output

```text
3
```

---

# 5. `__eq__`

Without it

```python
class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Rahul")
s2 = Student("Rahul")

print(s1 == s2)
```

Output

```text
False
```

Because Python compares **memory addresses**, not the data.

---

### Override `__eq__`

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

s1 = Student("Rahul")
s2 = Student("Rahul")

print(s1 == s2)
```

Output

```text
True
```

Now the comparison is based on the `name`.

---

# 6. Operator Overloading (`__add__`)

Suppose

```python
5 + 10
```

Internally

```python
5.__add__(10)
```

Similarly, you can define what `+` means for your own class.

```python
class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"₹{self.amount}"

m1 = Money(500)
m2 = Money(700)

print(m1 + m2)
```

Output

```text
₹1200
```

Without `__add__`, `m1 + m2` would raise a `TypeError`.

---

# Real-World AI Example

Imagine a machine learning model.

```python
class Dataset:

    def __init__(self, rows):
        self.rows = rows

    def __len__(self):
        return len(self.rows)
```

Now

```python
len(dataset)
```

returns the number of records.

This is how many AI and data science libraries work.

---

# Real-World Magento Example

Magento PHP doesn't use Python's magic methods, but it has similar concepts.

For example:

```php
$product->getName();
$product->setPrice(500);
```

PHP also supports special methods like `__construct()`, `__get()`, `__set()`, and `__toString()`, which serve similar purposes in object behavior.

---

# Mini Project

Create a `Book` class with:

* `title`
* `author`
* `pages`

Implement:

* `__str__` → Display book information.
* `__repr__` → Developer-friendly representation.
* `__len__` → Return the number of pages.
* `__eq__` → Compare books by title and author.

Then:

```python
book1 = Book("Python", "John", 350)
book2 = Book("Python", "John", 400)
book3 = Book("AI", "Alice", 250)
```

Test:

```python
print(book1)
print(repr(book1))
print(len(book1))
print(book1 == book2)
print(book1 == book3)
```

---

# Interview Questions

### Q1. What are magic methods?

**Answer:** Magic (dunder) methods are special methods with double underscores that Python automatically invokes to define how objects behave with built-in operations like `print()`, `len()`, `+`, and `==`.

---

### Q2. What is the difference between `__str__` and `__repr__`?

| `__str__`          | `__repr__`                              |
| ------------------ | --------------------------------------- |
| Readable for users | Intended for developers/debugging       |
| Used by `print()`  | Used by `repr()` and interactive shells |

---

### Q3. Why override `__eq__`?

**Answer:** To compare objects based on their data instead of their memory addresses.

---

### Q4. What is operator overloading?

**Answer:** It allows built-in operators like `+`, `-`, `==`, `<`, etc., to work with custom classes by implementing the corresponding magic methods.

---

# Lesson 11 Summary

In Lesson 11, you learned:

* ✅ Classes and Objects
* ✅ Constructors
* ✅ Inheritance
* ✅ Public, Protected, and Private Members
* ✅ Encapsulation
* ✅ Polymorphism
* ✅ Abstraction
* ✅ Magic (Dunder) Methods
* ✅ Operator Overloading

At this point, your Python OOP foundation is strong enough to understand the design of frameworks like **Magento 2**, **Django**, **Flask**, and many **AI libraries**.

---

# Roadmap Update

```
Python Phase
├── ✅ Lesson 1–10
├── ✅ Lesson 11: Object-Oriented Programming (Completed)
│   ├── ✅ Module 1
│   ├── ✅ Module 2
│   ├── ✅ Module 3
│   ├── ✅ Module 4
│   └── ✅ Module 5
└── ▶ Next: Lesson 12 – Exception Handling (try, except, else, finally, raise, custom exceptions)
```

Before we move to Lesson 12, complete the **Book** mini project. It will reinforce the magic methods you've just learned and prepare you for more advanced Python patterns.
