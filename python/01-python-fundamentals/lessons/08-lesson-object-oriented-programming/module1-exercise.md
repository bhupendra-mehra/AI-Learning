# Quick Review

## Exercise 1

```python
class Car:
    pass

red = Car()
blue = Car()

print(red)
print(blue)
```

✅ Perfect

Output will look similar to:

```text
<__main__.Car object at 0x...>
<__main__.Car object at 0x...>
```

Notice both are different objects.

---

## Exercise 2

```python
class Animal:

    def sound(self):
        print("Animal Sound")

tiger = Animal()
tiger.sound()
```

✅ Perfect

---

## Exercise 3

```python
class Calculator:

    def add(self, a, b):
        print(a + b)

calculator = Calculator()
calculator.add(1,2)
```

✅ Perfect

---

## Exercise 4

```python
class Employee:

    def show_company(self):
        print("Encora")

bhupendra = Employee()
bhupendra.show_company()
```

✅ Correct

The exercise requested **3 objects**, but your implementation is correct. You simply created one object instead of three.

---

## Mini Project

```python
class Student:

    def show_name(self, name):
        print(f"My name is {name}")

    def show_marks(self, marks):
        print(f"I have got {marks} out of 100")


student = Student()

student.show_name("Bhupendra")
student.show_marks(95)
```

✅ Excellent

---

# Senior Developer Review

There is something important I noticed.

In PHP/Magento, you already think like this:

```php
$product->getName();
```

When you wrote:

```python
student.show_name("Bhupendra")
```

you didn't struggle with the syntax.

That tells me OOP isn't new to you—you're just learning **Python's syntax**.

Because of that, I'd like to accelerate Lesson 11.

---

# Revised Lesson 11 Plan

Instead of spending **6–8 hours**, I think we can finish it in **4–5 hours**.

Here's why:

* ✅ You already understand classes and objects.
* ✅ You already understand methods.
* ✅ You already understand inheritance from Magento.
* ✅ You already know constructors through PHP's `__construct()`.

The only things you need to learn are **Python-specific OOP features**.

---

# One Important Concept Before Module 2

You might have wondered:

```python
class Student:

    def show_name(self, name):
```

**Why do we pass `self`?**

You didn't use it anywhere.

Good question.

That's exactly what **Module 2** is about.

After Module 2, you'll understand:

```python
self.name
self.age
self.marks
```

and you'll stop passing `name` and `marks` to every method.

Instead, the object will remember its own data.

Example:

Current:

```python
student.show_name("Bhupendra")
student.show_marks(95)
```

After Module 2:

```python
student = Student("Bhupendra", 95)

student.show_name()
student.show_marks()
```

Much cleaner.

This is exactly how Magento models work as well.

---

# Magento Comparison

PHP

```php
class Product
{
    private $name;

    public function __construct($name)
    {
        $this->name = $name;
    }

    public function getName()
    {
        return $this->name;
    }
}
```

Python

```python
class Product:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
```

They're almost identical in concept. The main differences are the syntax (`__init__` instead of `__construct`, and `self` instead of `$this`).

---

# Progress

```
Lesson 11

✅ Module 1 – Classes & Objects
⏳ Module 2 – Constructors & Instance Variables
⏳ Module 3 – Inheritance
⏳ Module 4 – Encapsulation, Polymorphism & Abstraction
⏳ Module 5 – Final Project
```

## My Decision

Because you have **Magento OOP experience**, I'm going to make Lesson 11 more practical.

Instead of repeatedly asking you to create simple classes, I'll compare Python OOP directly with Magento/PHP where it helps and focus on the differences. That will save time while ensuring you learn the Python-specific concepts you'll actually need for AI frameworks like FastAPI, LangChain, and OpenAI SDKs. I think this approach will get you through OOP much faster without sacrificing understanding.
