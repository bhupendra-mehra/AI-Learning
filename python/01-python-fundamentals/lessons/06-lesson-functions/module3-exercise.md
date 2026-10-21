# Exercise 1

```python
def greet(name="Guest"):
    print(name)

greet()
greet("Bhupendra")
```

### ✅ Correct

Output

```
Guest
Bhupendra
```

One small improvement:

The requirement was

```python
print(f"Welcome {name}")
```

instead of

```python
print(name)
```

Your understanding of **default parameters** is correct.

---

# Exercise 2

```python
def employee(name="Bhupendra", age=37):
    print(name, age)

employee("Rahul", 44)

employee(age=32, name="Tester")
```

### ✅ Correct

However, I noticed something important.

The requirement was:

> Call it using **keyword arguments**.

Your second call:

```python
employee(age=32, name="Tester")
```

is exactly what I wanted.

The first call:

```python
employee("Rahul", 44)
```

is a **positional argument** call.

Both are correct, but the exercise was specifically about keyword arguments.

---

# Exercise 3

```python
def add_numbers(*numbers):
    sum_value = 0

    for number in numbers:
        sum_value += number

    return sum_value

print(add_numbers(10,20,30))
```

### ✅ Perfect

This is exactly how I'd write it.

---

# Exercise 4

```python
def product(**details):
    return details

data = product(name="Laptop", price="111.99")

print(f"Product Name {data['name']}")
print(f"Price {data['price']}")
```

### ✅ Correct

One small suggestion.

Instead of

```python
return details
```

you could also print directly inside the function:

```python
def product(**details):
    print(details["name"])
    print(details["price"])
```

But I actually **prefer your solution**.

Returning data instead of printing it makes the function reusable.

That's a better design.

---

# Exercise 5

```python
double = lambda x: x * 2

print(double(3))
```

### ✅ Perfect

---

# Overall Score

| Exercise | Result |
| -------- | ------ |
| 1        | ✅      |
| 2        | ✅      |
| 3        | ✅      |
| 4        | ✅      |
| 5        | ✅      |

**Score: 10/10**

---

# Senior Developer Review

I noticed a very positive change in your coding style.

Earlier in the course, your approach was:

```text
Write code
↓
Print immediately
```

Now your instinct is becoming:

```text
Function

↓

Return value

↓

Store result

↓

Use result later
```

That's a big step forward because it's how real applications are designed.

---

# One Thing I Want You to Remember Forever

This is probably the most important lesson from today's module:

## `print()` vs `return`

A lot of beginners think they're interchangeable.

They're not.

### `print()`

Displays a value.

```python
def add(a, b):
    print(a + b)
```

Good for debugging or showing information to a user.

---

### `return`

Sends a value back to the caller.

```python
def add(a, b):
    return a + b
```

Now you can do:

```python
total = add(10, 20)

discount = total * 0.2

print(discount)
```

This is why production code relies heavily on `return`.

---

# Roadmap Progress

## ✅ Lesson 9 – Module 1: Function Basics

## ✅ Lesson 9 – Module 2: Parameters, Return Values & Scope

## ✅ Lesson 9 – Module 3: Advanced Functions

Only one module remains:

### Module 4 – Final Project

---

# One Improvement for Future Lessons

I also want to make one more optimization to the course.

From **Lesson 10 onward**, I won't ask prediction questions like:

> "What is the output?"

unless they teach something genuinely tricky.

Instead, most exercises will be:

* Write the code.
* Solve a practical problem.
* Refactor existing code.
* Small projects.

Reason: Based on the last two lessons, you're much stronger at writing code than answering isolated prediction questions. Since your goal is AI engineering, hands-on coding will give you more value than spending time on too many output-tracing exercises.

I think this will make the remaining lessons even more practical and aligned with how you'll actually work on AI projects.
