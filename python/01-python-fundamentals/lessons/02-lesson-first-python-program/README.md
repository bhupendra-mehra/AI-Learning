# Lesson 5 - Writing Your First Python Program

## Goal of Today's Lesson

By the end of this lesson, you will understand:

* What a Python program is
* How Python executes a file
* What an Interpreter is
* How to run Python code
* Variables
* Functions
* Input & Output
* Build your first chatbot (without AI yet)

> **Notice:** We are **not connecting to OpenAI today.**
>
> Before learning AI, we first need to understand how Python programs work.

---

# Before We Write Code

Let's compare PHP and Python.

## PHP

Suppose you have:

```php
<?php

echo "Hello Magento";
```

You execute:

```bash
php index.php
```

Output

```text
Hello Magento
```

Easy.

---

## Python

Exactly the same idea.

Create a file:

```text
app.py
```

Inside:

```python
print("Hello AI")
```

Execute:

```bash
python3 app.py
```

Output

```text
Hello AI
```

Notice anything?

Almost identical.

---

# What is app.py?

Many beginners think:

> app.py is Python.

No.

Think about Magento.

When you create

```text
Observer.php
```

Is that PHP?

No.

It is just **your code** written in PHP.

Similarly,

```text
app.py
```

is simply **your code written in Python**.

---

# What is the Python Interpreter?

This is the most important concept today.

Imagine you write

```python
print("Hello")
```

Can the CPU understand Python?

No.

The CPU only understands machine instructions.

So something sits in between.

```text
app.py

↓

Python Interpreter

↓

Machine Instructions

↓

CPU
```

Exactly like PHP.

```text
index.php

↓

PHP Interpreter

↓

CPU
```

So remember:

> **Python is a language.**
>
> **Python Interpreter is the program that runs Python code.**

---

# Let's Create Our First Program

Inside WSL:

```bash
mkdir -p ~/AI-Learning/lesson-5
cd ~/AI-Learning/lesson-5
```

Check:

```bash
pwd
```

Output

```text
/home/ubuntu/AI-Learning/lesson-5
```

---

# Open VS Code

Run

```bash
code .
```

Question:

Does VS Code open?

If **Yes**, continue.

If **No**, tell me the error.

---

# Create app.py

Inside VS Code

Create

```text
app.py
```

---

# First Line of Python

Write

```python
print("Hello AI")
```

Save the file.

---

# What is print()?

Imagine PHP.

```php
echo "Hello";
```

Python

```python
print("Hello")
```

Both display text on the screen.

---

# Run the Program

In the terminal

```bash
python3 app.py
```

Expected

```text
Hello AI
```

Congratulations 🎉

You just wrote your first Python application.

---

# Let's Improve It

Replace

```python
print("Hello AI")
```

with

```python
print("Welcome to AI Engineering")
print("My name is Bhupendra")
print("I am learning AI Agents")
```

Run again.

Output

```text
Welcome to AI Engineering
My name is Bhupendra
I am learning AI Agents
```

---

# What is a Variable?

Imagine Magento.

PHP

```php
$name = "Bhupendra";

echo $name;
```

Python

```python
name = "Bhupendra"

print(name)
```

Notice

Python has **no $**.

That's one of the biggest syntax differences.

---

# Let's Create Variables

Write

```python
name = "Bhupendra"
role = "Magento Developer"
experience = 8

print(name)
print(role)
print(experience)
```

Output

```text
Bhupendra
Magento Developer
8
```

---

# What is input()?

Until now

You gave data in code.

Now

Let's ask the user.

```python
name = input("Enter your name: ")

print(name)
```

Run

```bash
python3 app.py
```

Output

```text
Enter your name:
```

Type

```text
Bhupendra
```

Output

```text
Bhupendra
```

---

# Congratulations

You have just built your first interactive program.

No AI.

Just Python.

---

# How Does This Relate to AI?

Suppose tomorrow we replace

```python
print(name)
```

with

```python
answer = OpenAI(question)

print(answer)
```

Now

Your program becomes

```text
User

↓

Python

↓

OpenAI

↓

LLM

↓

Python

↓

Answer
```

That's why we're learning Python first.

---

# Think Like a Magento Developer

Today

```python
name = input()

print(name)
```

Tomorrow

```python
question = input()

answer = AI(question)

print(answer)
```

The structure remains the same.

Only the **processing step** changes.

---

# Homework

Create **app.py** with the following program:

```python
print("Welcome to AI Learning")

name = input("Enter your name: ")

role = input("Enter your profession: ")

print("Hello", name)

print("Profession:", role)

print("Welcome to AI Engineering")
```

Run:

```bash
python3 app.py
```

Paste:

1. Your `app.py` code (even if unchanged).
2. The terminal output.
3. Whether `code .` opened VS Code successfully.

---

# Why We Didn't Touch OpenAI Today

This is intentional.

Many tutorials jump straight to:

```python
from openai import OpenAI
```

without explaining:

* What Python is.
* What a `.py` file is.
* What an interpreter is.
* How a program runs.

By understanding these basics first, you'll be able to debug and build AI applications confidently instead of just copying code.

---

## Mentor Note

I'm also going to slightly adjust our roadmap based on your progress.

Instead of teaching Python as a separate subject, **I'll teach only the Python concepts needed to build AI applications**. Since you're already an experienced developer, you don't need a full Python course—you need *Python for AI*. That will make the learning faster, more practical, and directly connected to our goal of building a real AI agent.
