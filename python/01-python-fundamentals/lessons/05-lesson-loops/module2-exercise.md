# Code Review

## Part 1

## Exercise 1

```python
for i in range(5):
    print("Python")
```

### ✅ Correct

Output

```text
Python
Python
Python
Python
Python
```

---

## Exercise 2

You wrote:

```python
#Print the numbers 1 to 21.
for i in range(1,21):
    print(i)
```

Your **code is correct**, but your **comment is incorrect**.

The question was:

> Print numbers **1 to 20**

Your code:

```python
range(1,21)
```

prints

```text
1
2
...
20
```

because **21 is excluded**.

So simply update the comment:

```python
# Print numbers from 1 to 20
```

This is something senior developers notice during code reviews.

---

## Exercise 3

```python
for i in range(10):
    print(i)
```

### ✅ Perfect

Output

```text
0
1
2
3
4
5
6
7
8
9
```

---

## Exercise 4

```python
for i in range(2,6):
    print(i)
```

Your answer

```text
2
3
4
5
```

### ✅ Correct

---

## Exercise 5

```python
for i in range(3):
    print("AI")
```

Your answer

```text
AI
AI
AI
```

### ✅ Correct

---

# Score

| Exercise | Result                       |
| -------- | ---------------------------- |
| 1        | ✅                            |
| 2        | ✅ (comment needs correction) |
| 3        | ✅                            |
| 4        | ✅                            |
| 5        | ✅                            |

**Overall:** **10/10**

---

# One Important Teaching Point

I noticed something interesting.

You didn't ask:

> "Why does `range(21)` print only up to 20?"

That tells me you've already internalized one of the most important Python rules:

> **The stop value is excluded.**

That's excellent, because many beginners struggle with this for a while.

---

# One Small Python Best Practice

Currently you're writing:

```python
for i in range(5):
    print("Python")
```

Since `i` isn't being used inside the loop, experienced Python developers often write:

```python
for _ in range(5):
    print("Python")
```

### Why `_`?

It tells anyone reading the code:

> "This loop variable exists, but I don't need its value."

This isn't a new concept—just a style improvement. For now, you're perfectly fine continuing with `i`. We'll adopt `_` naturally as you become more comfortable with Python.

---

# Part 2


# Exercise 1

```python
name = "Bhupendra"

for ch in name:
    print(ch)
```

### ✅ Correct

No improvements needed.

---

# Exercise 2

Output

```text
A
I
```

### ✅ Correct

---

# Exercise 3

Your answer

```text
00
01
10
11
```

### ✅ Correct

More clearly:

```text
0 0
0 1
1 0
1 1
```

---

# Exercise 4

```python
name = input("Enter any word :")

for ch in name:
    print(ch)
```

### ✅ Perfect

---

# Exercise 5

Your code

```python
students = int(input("Number of students in class :"))

for student in range(1,students):
    print("Student",student,"Present")

classname = input("Enter classroom name :")

for ch in classname:
    print(ch)
```

### Almost Correct (9.5/10)

There is one small bug.

Suppose user enters

```text
5
```

Expected output

```text
Student 1 Present
Student 2 Present
Student 3 Present
Student 4 Present
Student 5 Present
```

Your program prints only

```text
Student 1 Present
Student 2 Present
Student 3 Present
Student 4 Present
```

Because

```python
range(1, students)
```

becomes

```python
range(1,5)
```

which excludes `5`.

Correct version:

```python
for student in range(1, students + 1):
```

or

```python
for student in range(1, students+1):
```

---

# Senior Developer Review

I'm starting to notice your coding style.

### ✅ Good Habits

* Good variable names

```python
student
classname
name
```

instead of

```python
x
y
z
```

---

You understand

* `range()`
* loop variables
* string iteration

without hesitation.

---

You rarely make syntax mistakes.

That's a good sign.

---

# One Best Practice

Instead of

```python
print("Student", student, "Present")
```

We'll soon learn **f-strings**, which are the preferred Python style.

It becomes:

```python
print(f"Student {student} Present")
```

We'll cover them properly later, so don't worry about changing your code now.

---

# Module 2 Status

## ✅ Completed

You now know:

* `for`
* `range()`
* Loop variable
* String iteration
* Nested loops

That is everything important about the `for` loop for now.

---

# Roadmap Progress

* ✅ Lesson 8 – Module 1: Understanding Loops
* ✅ Lesson 8 – Module 2: `for` Loop
* ⏭️ Next: **Lesson 8 – Module 3: `while` Loop**

---

## Performance Review

Based on Lessons 1–8, here's my assessment:

| Topic           | Confidence |
| --------------- | ---------- |
| Variables       | ⭐⭐⭐⭐⭐      |
| Input/Output    | ⭐⭐⭐⭐⭐      |
| Operators       | ⭐⭐⭐⭐⭐      |
| Conditions      | ⭐⭐⭐⭐⭐      |
| `for` Loop      | ⭐⭐⭐⭐⭐      |
| Problem Solving | ⭐⭐⭐⭐⭐      |

You're progressing faster than I expected. You're making logical mistakes (like the `range(1, students)` off-by-one issue) rather than syntax mistakes, and that's a normal part of programming. Those become easier to catch with practice.

I also noticed something encouraging: you're no longer asking "What syntax do I use?" Instead, you're writing the code first and letting me review it. That's exactly how a professional developer works. From here on, I'll continue acting more like a code reviewer and mentor than a lecturer, especially for the remaining Python fundamentals.

