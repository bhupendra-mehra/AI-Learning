# Review

## Exercise 1

```python
def greet():
    print("Welcome to Python")

for i in range(3):
    greet()
```

### ✅ Correct

Even better, you used a loop instead of writing

```python
greet()
greet()
greet()
```

That's exactly what a developer would do.

**Senior Tip**

Since `i` isn't used:

```python
for _ in range(3):
    greet()
```

is slightly more Pythonic.

---

## Exercise 2

```python
def show_menu():
    print("1. Login")
    print("2. Register")
    print("3. Exit")

for _ in range(2):
    show_menu()
```

### ✅ Perfect

I like that you've already started using `_` yourself.

That means you're adopting Python conventions naturally.

---

## Exercise 3

```
Hello
Hello
```

### ✅ Correct

---

## Exercise 4

```
Start
Python
End
```

### ✅ Correct

This is actually an important concept.

Execution flow:

```
Start

↓

Print Start

↓

Call test()

↓

Print Python

↓

Return

↓

Print End
```

Later, this same flow will apply to API calls, AI agents, and tool execution.

---

## Mini Project

```python
def show_header():
    print("====================")
    print("Shopping System")
    print("====================")

def show_footer():
    print("====================")
    print("Thank You")
    print("====================")

show_header()
print("...")
show_footer()
```

### ✅ Perfect

This is exactly how reusable code should look.

---

# Overall Score

| Exercise     | Result |
| ------------ | ------ |
| Exercise 1   | ✅      |
| Exercise 2   | ✅      |
| Exercise 3   | ✅      |
| Exercise 4   | ✅      |
| Mini Project | ✅      |

**Score: 10/10**

---

# One Important Observation

I noticed something.

When you wrote:

```python
def greet():
```

you didn't ask

> "How do I define a function?"

You simply wrote it.

That tells me you've understood:

* `def`
* Indentation
* Function call

very quickly.

---

# Another Observation

You're starting to write cleaner code than before.

Earlier you wrote:

```python
for i in range(3):
```

Now you're naturally writing:

```python
for _ in range(2):
```

That's exactly how experienced Python developers write unused loop variables.

It shows you're not just learning syntax—you've started adopting Python coding conventions.

---

# Fast Track Decision

Based on your progress, I'm making another change.

Originally, **Lesson 9** had **5 modules**.

I now think that's unnecessary.

Here's the revised structure:

* ✅ Module 1 – Function Basics (**Completed**)
* 🔄 Module 2 – Parameters, Return Values & Variable Scope (**combined**)
* 🔄 Module 3 – Advanced Functions (`*args`, `**kwargs`, default arguments, keyword arguments, lambda, recursion overview)
* 🔄 Module 4 – Final Project

We're merging **Variable Scope** into **Parameters & Return Values** because scope only makes sense once you've worked with parameters and return values. This keeps related concepts together and reduces unnecessary context switching.

This change shortens the course without removing any important concepts.

---

## Roadmap Progress

* ✅ Lesson 9 – Module 1: Function Basics
* ⏭️ Next: **Lesson 9 – Module 2: Parameters, Return Values & Variable Scope**

We'll continue using Fast Track Mode unless we reach a topic where a deeper explanation genuinely adds value.
