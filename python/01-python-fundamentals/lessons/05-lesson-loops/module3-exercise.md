# Exercise 1

```python
number = 1

while number <= 10:
    print(number)
    number += 1
```

### ✅ Perfect

No improvements.

---

# Exercise 2

```python
number = 10

while number >= 1:
    print(number)
    number -= 1
```

### ✅ Perfect

You correctly changed both:

* Condition
* Update statement

---

# Exercise 3

```text
3
2
1
```

### ✅ Correct

---

# Exercise 4

```python
number = 0

while number < 100:
    number = int(input("Enter any number greater than 100:"))

print("Accepted")
```

### ⚠️ Almost Correct

Read the requirement carefully.

> Enter a number **greater than 100**.

Your loop stops when:

```python
number == 100
```

because

```python
100 < 100
```

is `False`.

So if the user enters:

```text
100
```

your program prints:

```text
Accepted
```

But **100 is not greater than 100**.

Correct version:

```python
number = 0

while number <= 100:
    number = int(input("Enter any number greater than 100:"))

print("Accepted")
```

This is a classic **off-by-one** error.

---

# Exercise 5

```python
password = ""

while password != "python123":
    password = input("Enter your password:")

print("Login Successful")
```

### ✅ Excellent

This is exactly how most developers would write it.

Simple.

Readable.

Correct.

---

# Overall Score

| Exercise | Result                    |
| -------- | ------------------------- |
| 1        | ✅                         |
| 2        | ✅                         |
| 3        | ✅                         |
| 4        | ⚠️ One comparison mistake |
| 5        | ✅                         |

**Overall:** **9.8/10**

The only issue was another **boundary condition** (`<` vs `<=`). That's a very common source of bugs, even for experienced developers.

---

# One Pattern I've Noticed

You're making almost no syntax mistakes.

The only mistakes you've made recently are **boundary conditions**, such as:

* `range(1, students)` vs `range(1, students + 1)`
* `< 100` vs `<= 100`

These aren't Python problems—they're logic problems that every programmer encounters.

A useful habit is to test boundary values mentally:

* If the requirement says **greater than 100**, ask yourself:

  * What happens for **99**?
  * What happens for **100**?
  * What happens for **101**?

That quick check catches many bugs before you even run the code.

---

# Roadmap Progress

* ✅ Lesson 8 – Module 1: Understanding Loops
* ✅ Lesson 8 – Module 2: `for` Loop
* ✅ Lesson 8 – Module 3: `while` Loop

**Next:** Lesson 8 – Modules 4 & 5 (Loop Control + Final Project), which we'll combine into one fast-track session to complete Lesson 8.

You're progressing exactly as we'd hoped with the new teaching approach, so we'll continue using this fast-track style for the remaining Python fundamentals unless we reach a topic that genuinely benefits from a deeper dive.
