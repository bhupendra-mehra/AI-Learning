# Review

## Exercise 1

Your code:

```python
def greet(name):
    print(f"Welcome {name}")

greet("Bhupendra")
```

### ✅ Logic: Correct

The only issue is the requirement said:

> Call it **twice** with different names.

Example:

```python
greet("Bhupendra")
greet("Rohit")
```

Very small miss.

**Rating: 9.8/10**

---

## Exercise 2

```python
def multiply(a,b):
    return a * b

result = multiply(5,6)
print(result)
```

### ✅ Perfect

This is exactly how production code is written.

---

## Exercise 3

```text
100
```

### ✅ Correct

---

## Exercise 4

```text
Python
```

### ✅ Correct

---

## Exercise 5

Your answer:

> Not work, variable has local scope.

### ✅ Correct

I actually like your explanation.

Soon you'll naturally say:

> "`age` is a local variable and is not accessible outside the function."

---

## Mini Project

```python
def calculate_salary(hours, rate):
    return hours * rate

hours = int(input("Enter hours :"))
rate  = int(input("Enter rate :"))

salary = calculate_salary(hours, rate)

print(salary)
```

### ✅ Perfect

---

# Overall Score

| Question     | Result |
| ------------ | ------ |
| Exercise 1   | ✅      |
| Exercise 2   | ✅      |
| Exercise 3   | ✅      |
| Exercise 4   | ✅      |
| Exercise 5   | ✅      |
| Mini Project | ✅      |

**Overall:** **9.9/10**

(The only deduction is because the first exercise asked to call the function twice.)

---

# Important Observation

This is where I see a major improvement in your thinking.

A few lessons ago, you were writing everything in one block:

```python
login

discount

checkout

summary
```

Now you're naturally thinking:

```python
calculate_salary()

multiply()

greet()
```

That's exactly how large software systems are designed.

---

# One Best Practice

When a function returns a value, avoid doing unnecessary work inside it.

Good:

```python
def calculate_salary(hours, rate):
    return hours * rate
```

Not ideal:

```python
def calculate_salary(hours, rate):
    salary = hours * rate
    return salary
```

The second version isn't wrong, but if the variable is only used once, returning the expression directly keeps the code concise.

---

# Performance Review

We've now covered:

* Variables
* Conditions
* Loops
* Functions (Basics)
* Parameters
* Return Values
* Scope

At this point, you can already write programs that are modular, reusable, and much easier to maintain than when we started.

---

# Fast Track Decision for Module 3

Looking at your progress, I don't think we need to spend much time on:

* `*args`
* `**kwargs`
* Lambda
* Recursion

Here's why:

* **`*args` and `**kwargs`** are useful and common enough that we'll cover them.
* **Lambda** is useful, but we can learn it in about 15–20 minutes.
* **Recursion** is an important computer science concept, but it's **rarely used in day-to-day AI engineering or Magento development**. We'll cover the basics so you recognize it, but we won't spend hours on it.

So I'd like to compress Module 3 into a single fast-track session and then move on to the final project for Lesson 9.

I think that's the most efficient use of our time and keeps us aligned with the goal of reaching AI agent development as quickly as possible without skipping the concepts you'll actually use.
