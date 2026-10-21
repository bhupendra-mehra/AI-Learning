# 🚀 Lesson 6 – Variables & Data Types

**Roadmap Position**

* **Phase 1:** Python for AI Engineers
* **Lesson:** 6
* **Goal:** Understand how Python stores and works with data.

---

# Before We Start

I'm going to ask you one question.

Suppose I ask you:

> **What is your name?**

You reply:

> **Bhupendra**

Now after 5 minutes I ask again:

> **What is your name?**

You still answer:

> **Bhupendra**

How did your brain remember it?

Because it **stored** the information somewhere.

A computer works the same way.

---

# What is a Variable?

A **variable** is simply a **named storage location** that holds a value.

Think of it as a labeled box.

```
┌────────────────────┐
│ Name               │
│ Bhupendra          │
└────────────────────┘
```

The label is **name**.

The value inside is **Bhupendra**.

---

# Magento Example

Suppose you have:

```php
$productName = "iPhone 16";
```

What happens?

PHP creates a variable called:

```
$productName
```

and stores:

```
iPhone 16
```

Exactly the same in Python.

```python
product_name = "iPhone 16"
```

Notice two differences:

PHP

```php
$productName
```

Python

```python
product_name
```

### Difference 1

Python has **no `$`**.

---

### Difference 2

Python uses **snake_case**.

PHP/Magento usually uses:

```php
$productName
$customerEmail
$orderId
```

Python convention is:

```python
product_name
customer_email
order_id
```

This is called **snake_case**.

It isn't a language rule—you *can* use `productName`—but following Python conventions makes your code easier for other Python developers to read.

---

# How Does Memory Work?

Suppose we write:

```python
name = "Bhupendra"
```

The computer stores it like this (conceptually):

```
Memory

┌────────────────────┐
│ name               │
│ Bhupendra          │
└────────────────────┘
```

Now write:

```python
city = "Mumbai"
```

Memory becomes:

```
┌────────────────────┐
│ name               │
│ Bhupendra          │
└────────────────────┘

┌────────────────────┐
│ city               │
│ Mumbai             │
└────────────────────┘
```

The computer now remembers both.

---

# Data Types

A computer needs to know **what kind of value** it is storing.

Imagine Magento.

Suppose:

```
Price = 1000
```

Can price be:

```
"Hello"
```

No.

Different values have different meanings.

Python classifies them into **data types**.

---

## 1. String (str)

A string is **text**.

```python
name = "Bhupendra"
```

Examples:

```python
city = "Mumbai"

framework = "Magento"

language = "Python"
```

Everything inside quotes is text.

---

## 2. Integer (int)

Whole numbers.

```python
age = 37

products = 100

quantity = 5
```

No quotes.

---

## 3. Float

Decimal numbers.

```python
price = 999.99

discount = 10.5
```

Notice the decimal point.

---

## 4. Boolean (bool)

Only two values.

```python
True

False
```

Examples:

```python
is_logged_in = True

is_admin = False
```

Think Magento.

```
Customer Logged In?

Yes

No
```

That's a Boolean.

---

# Why Are Data Types Important?

Suppose you write:

```python
age = "37"
```

Notice the quotes.

This is **not** a number.

It is **text**.

Whereas:

```python
age = 37
```

is a number.

Although both *look* similar, Python treats them differently.

---

# Let's Check the Type

Python provides a function:

```python
type()
```

Example:

```python
name = "Bhupendra"

print(type(name))
```

Output:

```python
<class 'str'>
```

Another example:

```python
age = 37

print(type(age))
```

Output:

```python
<class 'int'>
```

---

# PHP Comparison

PHP:

```php
var_dump($name);
```

Python:

```python
print(type(name))
```

Both help you inspect the value's type.

---

# Why did we use `type()`?

Imagine tomorrow you're debugging an AI application.

You receive:

```python
age = input("Enter Age")
```

User types:

```text
37
```

You think:

```python
age is int
```

But Python actually stores:

```python
age = "37"
```

If you don't know the data type, your program may behave unexpectedly.

That's why professional Python developers frequently use:

```python
print(type(variable))
```

while debugging.

This is very similar to how you might inspect values while debugging PHP or Magento.

---

# Mini Project

Create a new file:

```
lesson-6.py
```

Write:

```python
name = "Bhupendra"
age = 37
salary = 50000.50
is_magento_developer = True

print(name)
print(age)
print(salary)
print(is_magento_developer)

print(type(name))
print(type(age))
print(type(salary))
print(type(is_magento_developer))
```

---

# Expected Output

```
Bhupendra
37
50000.5
True

<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

# Challenge 1 (Think Like a Developer)

Tell me the data type of each variable.

```python
customer_name = "John"

order_id = 1001

price = 2500.75

is_paid = False

quantity = 10
```

Don't use Python yet.

Just tell me:

```
customer_name → ?

order_id → ?

price → ?

is_paid → ?

quantity → ?
```

---

# Challenge 2

Which of these are **Strings**?

```python
A = "100"

B = 100

C = "Magento"

D = True

E = 25.6
```

---

# Mini Challenge 3 (No Python Yet)

Predict the output.

```python
age = "37"

print(type(age))
```

What will Python print?

Choose one:

**A**

```text
<class 'int'>
```

**B**

```text
<class 'str'>
```

---

# Mini Challenge 4

Again, don't run the code.

Predict the output:

```python
age = 37

print(age + 10)
```

---

# Mini Challenge 5

Predict what will happen:

```python
age = "37"

print(age + "10")
```

Will the output be:

**A**

```text
47
```

**B**

```text
3710
```

**C**

Error

Don't guess randomly. Explain **why** you chose your answer.

---

# Homework (Exercise 1)

1. Create `lesson-6.py`.
2. Run it.
3. Paste:

   * Your code.
   * The output.
4. Answer Challenges 1 , 2 , 3 , 4 and 6.

---

## Type Conversion

This is one of the most important concepts for AI.

Let's use a real-world example.

---

# Imagine You're Registering on a Website

The form asks:

```text
Enter your age:
```

You type:

```text
37
```

Did you type a number?

From a human perspective:

> Yes.

From Python's perspective:

> No.

Why?

Because the keyboard sends **characters**, not numeric types.

So Python receives:

```python
"37"
```

This is called a **string**.

---

# Why Is This a Problem?

Suppose we write:

```python
age = input("Enter your age: ")

print(age + 10)
```

What do you think happens?

Many beginners expect:

```text
47
```

But it won't work because:

```python
age
```

contains:

```python
"37"
```

not

```python
37
```

Python won't automatically convert it.

---

# The Solution: Type Conversion

We tell Python:

> Convert this string into an integer.

Example:

```python
age = int(input("Enter your age: "))

print(age + 10)
```

Now the flow becomes:

```text
User types

37

↓

Python receives

"37"

↓

int()

↓

37

↓

age + 10

↓

47
```

---

# Magento Comparison

Suppose Magento receives data from a REST API.

The JSON might contain:

```json
{
  "qty": "10"
}
```

Even though it looks like a number, it's actually a string.

Before performing calculations, backend code often converts it to an integer or float.

Python follows the same idea.

---

# Python Type Conversion Functions

| Function  | Converts To    |
| --------- | -------------- |
| `int()`   | Integer        |
| `float()` | Decimal number |
| `str()`   | String         |
| `bool()`  | Boolean        |

Examples:

```python
number = int("25")
price = float("99.95")
text = str(100)
```

---

# Mini Project

Create a new file named:

```text
lesson-6-conversion.py
```

Write:

```python
print("Age Calculator")

age = int(input("Enter your age: "))

print("Next year you will be:", age + 1)
```

Expected run:

```text
Age Calculator
Enter your age:
37

Next year you will be:
38
```

---

# Final Challenge for Lesson 6 (Excercise 2)

Without running Python, answer these:

### Q1

What is the data type?

```python
age = input("Enter age: ")
```

---

### Q2

How do you convert `"100"` into an integer?

---

### Q3

Predict the output:

```python
number = int("50")

print(number + 20)
```

---

### Q4

Predict the output:

```python
price = float("99.99")

print(type(price))
```

---

### Q5

Why do AI applications often need type conversion?

Think about:

* User input
* API responses
* JSON data

Explain it in your own words.

---

**Lesson 6 is almost complete.**

Once you:

* complete the type conversion mini project, and
* answer the final five questions,

### Lesson 6 → AI Connection

```python
age = int(input("Enter your age: "))
```

Why is this important?

Because when you build an AI chatbot:

```python
user_age = input("Enter your age: ")
```

the chatbot receives `"37"` (a string), not `37`.

Before using it in business logic, you'll convert it:

```python
user_age = int(user_age)
```

This shows that every Python concept we learn has a direct application in AI development.

# Real AI Example

Now look at this code:

```python
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("Adult")
```

Two lessons ago, this might have looked confusing.

Now you understand every line:

* `input()` → receives text
* `int()` → converts text to a number
* Variable stores the value
* `if` compares the number

This is exactly why we learned the fundamentals first.

# 🎯 Lesson 6 Summary

Today you learned:

* ✅ Variables
* ✅ Memory concept
* ✅ Data Types

  * `str`
  * `int`
  * `float`
  * `bool`
* ✅ `type()`
* ✅ Type Conversion

  * `int()`
  * `float()`
  * `str()`
* ✅ Why `input()` returns a string
* ✅ Why AI applications require type conversion
* ✅ String concatenation vs numeric addition

---

### Next Lesson

➡ **Lesson 7 – Operators & Conditions**

We'll learn:

* Arithmetic operators (`+`, `-`, `*`, `/`, `%`, `//`, `**`)
* Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
* Logical operators (`and`, `or`, `not`)
* `if`, `elif`, `else`
* Nested conditions
* Truthy and Falsy values (very useful in Python)
* Mini Project: **Smart Eligibility Checker**

---

