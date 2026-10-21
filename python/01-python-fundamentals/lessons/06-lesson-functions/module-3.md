# Lesson 9 – Module 3

## Advanced Functions (Fast Track)

**Estimated Time:** 30–40 minutes

## Learning Objectives

By the end of this module, you'll understand:

* Default Parameters
* Keyword Arguments
* `*args`
* `**kwargs`
* Lambda Functions (Basics)
* Recursion (Introduction)

---

# 1. Default Parameters

Default parameters let you define a value that will be used if the caller doesn't provide one.

```python
def greet(name="Guest"):
    print(f"Welcome {name}")
```

Usage:

```python
greet()
greet("Bhupendra")
```

Output:

```text
Welcome Guest
Welcome Bhupendra
```

### When to use

Optional values.

Example:

```python
send_email(subject, cc=None)
```

---

# 2. Keyword Arguments

Normally:

```python
def login(username, password):
    print(username, password)

login("admin", "1234")
```

Using keywords:

```python
login(password="1234", username="admin")
```

### Benefits

* More readable
* Order doesn't matter

---

# 3. `*args`

Use when you don't know how many positional arguments will be passed.

```python
def total(*numbers):
    print(numbers)
```

Calling:

```python
total(10, 20)
total(10, 20, 30, 40)
```

Output:

```text
(10, 20)
(10, 20, 30, 40)
```

Loop through them:

```python
def total(*numbers):
    sum_value = 0

    for number in numbers:
        sum_value += number

    return sum_value
```

Example:

```python
print(total(10, 20, 30))
```

Output

```text
60
```

### AI Example

An AI agent may receive any number of search terms:

```python
search_documents(*queries)
```

---

# 4. `**kwargs`

Used when the number of **named arguments** isn't fixed.

```python
def user_details(**data):
    print(data)
```

Calling:

```python
user_details(
    name="Bhupendra",
    age=37,
    city="Mumbai"
)
```

Output:

```text
{
    'name':'Bhupendra',
    'age':37,
    'city':'Mumbai'
}
```

Access values:

```python
print(data["name"])
```

### AI Example

AI models often receive options like:

```python
generate_response(
    model="gpt",
    temperature=0.7,
    max_tokens=500
)
```

Internally, many libraries use `**kwargs` to accept optional configuration.

---

# 5. Lambda Functions

A lambda is an anonymous (unnamed) function.

Normal function:

```python
def square(x):
    return x * x
```

Lambda:

```python
square = lambda x: x * x
```

Usage:

```python
print(square(5))
```

Output

```text
25
```

### When do we use it?

Mostly for short, one-line functions.

We'll see more examples later with sorting and collections.

---

# 6. Recursion (Introduction)

A recursive function calls itself.

Example:

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)
```

Calling:

```python
countdown(5)
```

Output:

```text
5
4
3
2
1
```

### Do you need recursion for AI?

Not much.

It's useful to understand, but you'll rarely write recursive functions in everyday AI engineering or Magento development.

---

# Best Practices

✅ Use default parameters for optional values.

✅ Use keyword arguments when a function has many parameters.

✅ Use `*args` only when the number of inputs is truly unknown.

✅ Use `**kwargs` for optional configuration.

✅ Prefer normal functions over lambda if the logic is more than one line.

---

# Exercises

## Exercise 1

Create

```python
def greet(name="Guest"):
```

Call it:

* Without an argument.
* With your name.

---

## Exercise 2

Create

```python
def employee(name, age):
```

Call it using **keyword arguments**.

---

## Exercise 3

Create

```python
def add_numbers(*numbers):
```

Return the sum of all numbers.

Example:

```python
print(add_numbers(10, 20, 30))
```

Output

```text
60
```

---

## Exercise 4

Create

```python
def product(**details):
```

Print:

* Product Name
* Price

Call it with:

```python
name="Laptop"

price=65000
```

---

## Exercise 5

Convert this function into a lambda:

```python
def double(x):
    return x * 2
```

---

# Senior Developer Notes

Here's what you'll actually use in real projects:

| Feature            | Real Usage |
| ------------------ | ---------- |
| Default Parameters | ⭐⭐⭐⭐⭐      |
| Keyword Arguments  | ⭐⭐⭐⭐⭐      |
| `*args`            | ⭐⭐⭐        |
| `**kwargs`         | ⭐⭐⭐⭐       |
| Lambda             | ⭐⭐⭐        |
| Recursion          | ⭐          |

This isn't saying recursion is unimportant—it's just less common in the kinds of applications you're aiming to build.

---

# Module Summary

Today you learned:

* ✅ Default Parameters
* ✅ Keyword Arguments
* ✅ `*args`
* ✅ `**kwargs`
* ✅ Lambda Functions
* ✅ Recursion (Introduction)

---

## After this

Only one thing remains in Lesson 9:

### **Final Project**

We'll refactor your shopping system into a modular application using functions. That project will tie together everything you've learned about functions and prepare you for the next lesson on collections.
