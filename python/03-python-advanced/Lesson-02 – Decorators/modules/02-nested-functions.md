# Module 02 – Nested Functions

## Module Overview

Before Python decorators existed, Python already supported **functions inside other functions**. These are called **nested functions**.

Nested functions are one of the core building blocks of decorators because decorators internally create and return functions.

This module explains how nested functions work, how they access variables from their enclosing scope, and why they are useful.

---

# Learning Objectives

After completing this module, you will be able to:

* Understand nested functions.
* Explain why functions can be defined inside other functions.
* Call inner functions.
* Return functions from functions.
* Recognize how nested functions lead to decorators.

---

# What is a Nested Function?

A nested function is simply a function defined inside another function.

Example:

```python
def outer():

    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()


outer()
```

Output:

```text
Outer Function
Inner Function
```

The function `inner()` exists only inside `outer()`.

---

# Why Use Nested Functions?

Instead of creating many helper functions globally:

```python
def validate():
    ...

def process():
    ...

def calculate():
    ...
```

Sometimes a helper function is only useful inside one function.

Instead of exposing it globally, keep it inside:

```python
def process_order():

    def validate_order():
        ...

    validate_order()
```

This improves encapsulation and keeps related logic together.

---

# Scope of Nested Functions

Consider:

```python
def outer():

    def inner():
        print("Inside Inner")

    inner()

outer()
```

Works perfectly.

Now try:

```python
def outer():

    def inner():
        print("Inside Inner")

outer()

inner()
```

Output:

```text
NameError:
name 'inner' is not defined
```

Why?

Because `inner()` only exists while `outer()` is executing.

It cannot be accessed directly from outside.

---

# Returning Functions

One of Python's most powerful features is that functions are **first-class objects**.

That means a function can:

* Be assigned to a variable.
* Be passed as an argument.
* Be returned from another function.

Example:

```python
def outer():

    def inner():
        print("Hello from Inner")

    return inner


message = outer()

message()
```

Output:

```text
Hello from Inner
```

Notice:

```python
message = outer()
```

stores a **function**, not a string or number.

Later:

```python
message()
```

executes the returned function.

This concept is the foundation of decorators.

---

# Functions Are Objects

You already know:

```python
x = 10
```

Stores an integer.

Similarly:

```python
def greet():
    print("Hello")


message = greet
```

Now:

```python
message()
```

Output:

```text
Hello
```

Notice:

```python
message = greet
```

There are **no parentheses**.

You are assigning the function itself, not calling it.

---

# Nested Functions + Returning Functions

Now combine both ideas.

```python
def outer():

    def inner():
        print("Python")

    return inner


function = outer()

function()
```

Execution Flow:

```text
outer()

↓

Create inner()

↓

Return inner()

↓

Store in function

↓

function()

↓

Execute inner()
```

This is exactly how decorators begin.

---

# Why Is This Important?

A decorator does not modify your function directly.

Instead, it:

1. Receives a function.
2. Creates another function.
3. Returns the new function.

Today's module teaches Steps 2 and 3.

---

# Real-World Examples

### Example 1 – Login Message

```python
def login():

    def welcome():
        print("Welcome User")

    welcome()


login()
```

---

### Example 2 – Returning Different Functions

```python
def operation(choice):

    def add():
        print("Addition")

    def subtract():
        print("Subtraction")

    if choice == "add":
        return add

    return subtract


task = operation("add")

task()
```

Output:

```text
Addition
```

Python returns different functions based on the condition.

---

# Best Practices

* Keep nested functions small.
* Use them only when they are relevant to the enclosing function.
* Return functions only when needed.
* Use meaningful function names.

---

# Common Mistakes

## Mistake 1

Calling instead of returning.

Incorrect:

```python
return inner()
```

This executes the function immediately.

Correct:

```python
return inner
```

Return the function object itself.

---

## Mistake 2

Trying to call the inner function directly.

```python
inner()
```

Outside `outer()` results in:

```text
NameError
```

---

## Mistake 3

Confusing:

```python
greet
```

with

```python
greet()
```

Remember:

* `greet` → Function object.
* `greet()` → Execute the function.

---

# Interview Questions & Answers

### 1. What is a nested function?

**Interview Answer**

A nested function is a function defined inside another function. It is typically used to encapsulate helper logic that is only needed within the enclosing function.

---

### 2. Why do we use nested functions?

**Interview Answer**

Nested functions improve encapsulation, reduce global namespace pollution, and keep related logic together.

---

### 3. Can Python return a function?

**Interview Answer**

Yes. Functions are first-class objects in Python, so they can be assigned to variables, passed as arguments, and returned from other functions.

---

### 4. What is the difference between `return inner` and `return inner()`?

**Interview Answer**

`return inner` returns the function object without executing it, while `return inner()` executes the function immediately and returns its result.

---

# Key Takeaways

* Functions can exist inside other functions.
* Inner functions are only accessible within their enclosing function.
* Python functions are first-class objects.
* Functions can be returned just like any other object.
* Returning functions is one of the foundations of decorators.

---

# Module Summary

This module introduced nested functions and demonstrated that Python functions are first-class objects. You learned how to define functions inside other functions, how scope affects inner functions, and how to return a function instead of executing it. These concepts are essential because decorators work by creating and returning new functions.

---

# Knowledge Check

Answer these questions before moving to Module 03.

1. What is a nested function?
2. Why would you define a function inside another function?
3. Why can't an inner function usually be called from outside its outer function?
4. What does `return inner` do?
5. What is the difference between:

   * `message = greet`
   * `message = greet()`
6. Why are Python functions called first-class objects?
7. What is the difference between:

   * `return inner`
   * `return inner()`

---

# Practical Exercise

Create:

```text
exercises/exercise-04.py
```

Write a program that contains:

* An `outer()` function.
* Two nested functions:

  * `welcome()`
  * `goodbye()`
* Return one of them based on a parameter:

```python
task = outer("welcome")
task()
```

Then try:

```python
task = outer("goodbye")
task()
```

Observe how Python returns different functions depending on the input.
