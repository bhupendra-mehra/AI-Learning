# Module 03 – Closures

## Module Overview

In the previous module, you learned that Python functions can be defined inside other functions and that functions can be returned.

Now we'll answer an important question:

> **What happens to the variables inside the outer function after it has finished executing?**

Normally, local variables disappear when a function ends. However, if an inner function still needs those variables, Python preserves them. This mechanism is called a **closure**.

Closures are one of the core building blocks of decorators because decorators often need to remember information from the outer function.

---

# Learning Objectives

After completing this module, you will be able to:

* Understand what a closure is.
* Explain variable capture.
* Understand why variables don't disappear.
* Create simple closures.
* Explain the relationship between closures and decorators.

---

# The Problem

Consider this example:

```python
def outer():

    message = "Hello"

    def inner():
        print(message)

    return inner


task = outer()
task()
```

Output:

```text
Hello
```

Now think about this.

After:

```python
task = outer()
```

the `outer()` function has already finished.

Normally, the local variable:

```python
message = "Hello"
```

should be destroyed.

So why does:

```python
task()
```

still print:

```text
Hello
```

---

# What is a Closure?

A **closure** is an inner function that **remembers variables from its enclosing function even after the enclosing function has finished executing**.

Python automatically keeps those variables alive because the inner function still needs them.

---

# Variable Capture

Example:

```python
def outer():

    username = "Bhupendra"

    def greet():
        print(f"Welcome {username}")

    return greet


welcome = outer()

welcome()
```

Output:

```text
Welcome Bhupendra
```

Notice:

`username` is remembered even though `outer()` has already completed.

This process is called **variable capture**.

---

# Multiple Captured Variables

```python
def calculator():

    number1 = 10
    number2 = 20

    def add():
        print(number1 + number2)

    return add


result = calculator()

result()
```

Output:

```text
30
```

Both variables remain available.

---

# Creating Different Closures

Every call creates its own closure.

```python
def greeting(name):

    def message():
        print(f"Hello {name}")

    return message


john = greeting("John")
alice = greeting("Alice")

john()
alice()
```

Output:

```text
Hello John
Hello Alice
```

Each returned function remembers its own value.

---

# Why Are Closures Useful?

Suppose you need several greeting functions.

Without closures:

```python
def hello_john():
    print("Hello John")


def hello_alice():
    print("Hello Alice")
```

With closures:

```python
john = greeting("John")
alice = greeting("Alice")
```

One reusable function creates many customized functions.

---

# Relationship Between Closures and Decorators

Decorators work like this:

```text
Outer Function

↓

Receives Original Function

↓

Creates Inner Function

↓

Inner Function remembers Original Function

↓

Returns Inner Function
```

That "remembering" behavior is possible because of **closures**.

Without closures, decorators would not work.

---

# Real-World Examples

## Example 1 – Discount Generator

```python
def discount(rate):

    def calculate(price):
        return price - (price * rate)

    return calculate


ten_percent = discount(0.10)

print(ten_percent(1000))
```

Output:

```text
900.0
```

The returned function remembers the discount rate.

---

## Example 2 – Prefix Generator

```python
def prefix(title):

    def display(name):
        print(f"{title} {name}")

    return display


mr = prefix("Mr.")
ms = prefix("Ms.")

mr("John")
ms("Alice")
```

Output:

```text
Mr. John
Ms. Alice
```

Each returned function remembers a different title.

---

# Best Practices

* Keep closures simple.
* Capture only the variables you actually need.
* Use descriptive variable names.
* Prefer closures when creating configurable functions.

---

# Common Mistakes

## Mistake 1

Returning:

```python
return inner()
```

instead of:

```python
return inner
```

The first executes the function immediately.

The second returns the function object.

---

## Mistake 2

Assuming local variables are always destroyed.

If an inner function references them, Python keeps them alive.

---

## Mistake 3

Confusing closures with nested functions.

Every closure is a nested function.

Not every nested function is a closure.

A nested function becomes a closure only when it captures variables from its enclosing scope.

---

# Interview Questions & Answers

## 1. What is a closure?

**Interview Answer**

A closure is an inner function that remembers variables from its enclosing scope even after the outer function has finished executing.

---

## 2. What is variable capture?

**Interview Answer**

Variable capture is the process by which a closure retains access to variables defined in its enclosing function.

---

## 3. Why are closures important?

**Interview Answer**

Closures allow functions to preserve state, create configurable behavior, and form the foundation of decorators.

---

## 4. Are all nested functions closures?

**Interview Answer**

No. A nested function is only a closure if it captures and uses variables from its enclosing function.

---

# Key Takeaways

* Closures remember variables.
* Python preserves captured variables automatically.
* Every closure is a nested function.
* Not every nested function is a closure.
* Closures are one of the foundations of decorators.

---

# Module Summary

Closures allow Python functions to retain access to variables from their enclosing scope even after the enclosing function has finished executing. This ability to preserve state makes closures extremely powerful and is one of the key mechanisms that enables decorators to work.

---

# Knowledge Check

1. What is a closure?
2. Why doesn't the captured variable disappear after the outer function returns?
3. What is variable capture?
4. Are all nested functions closures? Explain.
5. Why are closures important for decorators?
6. What is the difference between a nested function and a closure?

---

# Practical Exercise

Create:

```text
exercises/exercise-05.py
```

### Requirement

Create a function:

```python
def multiplier(number):
```

Inside it, create a nested function:

```python
def multiply(value):
```

The inner function should multiply `value` by the captured `number`.

Example:

```python
double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))
```

Expected Output:

```text
20
30
```

Observe how each returned function remembers its own multiplier value.
