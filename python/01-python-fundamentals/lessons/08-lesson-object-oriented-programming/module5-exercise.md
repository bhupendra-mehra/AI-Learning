# Output Analysis

Your output will be approximately:

```text
Title : Python , Author : John, Pages : 350
Book(Python,John,350)
6
False
False
```

Let's see why.

---

# 1. `__init__` ✅

```python
def __init__(self,title,author,pages):
```

✔ Correct.

You initialized all instance variables properly.

---

# 2. `__str__` ✅

```python
def __str__(self):
    return f"Title : {self.title} , Author : {self.author}, Pages : {self.pages}"
```

✔ Very good.

This is exactly what `print(book1)` should display.

---

# 3. `__repr__` ✅

```python
def __repr__(self):
    return f"Book({self.title},{self.author},{self.pages})"
```

Works correctly.

However, in Python we usually include quotes around strings because `repr()` is intended to be unambiguous.

A more common implementation is:

```python
def __repr__(self):
    return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"
```

Output:

```text
Book(title='Python', author='John', pages=350)
```

This is more readable and closer to Python conventions.

---

# 4. `__len__` ❌ (One Mistake)

You wrote

```python
def __len__(self):
    return len(self.title)
```

This returns

```text
6
```

because

```python
len("Python")
```

is 6.

---

### But what did the exercise ask?

> Return the number of pages.

So it should be

```python
def __len__(self):
    return self.pages
```

Now

```python
len(book1)
```

returns

```text
350
```

This is the intended behavior.

---

# 5. `__eq__` ✅ (Works, but can be improved)

You wrote

```python
return self.title+self.author+str(self.pages) == other.title+other.author+str(other.pages)
```

This works.

But it has two issues.

### Problem 1

You're converting everything into one long string.

Example:

```python
Book("AB", "C", 12)
```

becomes

```text
ABC12
```

Another combination could accidentally produce the same string.

---

### Better Way

Compare each field individually.

```python
def __eq__(self, other):
    return (
        self.title == other.title
        and self.author == other.author
        and self.pages == other.pages
    )
```

---

### Even Better (Pythonic)

Python allows tuple comparison.

```python
def __eq__(self, other):
    return (
        self.title,
        self.author,
        self.pages
    ) == (
        other.title,
        other.author,
        other.pages
    )
```

This is concise and idiomatic.

---

# 6. Missing Type Check ⭐

Imagine someone writes

```python
book1 == 100
```

Your current code tries

```python
100.title
```

which raises an `AttributeError`.

A safer implementation is:

```python
def __eq__(self, other):
    if not isinstance(other, Book):
        return NotImplemented

    return (
        self.title,
        self.author,
        self.pages
    ) == (
        other.title,
        other.author,
        other.pages
    )
```

Returning `NotImplemented` lets Python decide how to handle comparisons with unrelated types.

---

# Production Version

```python
class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author} ({self.pages} pages)"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented

        return (
            self.title,
            self.author,
            self.pages
        ) == (
            other.title,
            other.author,
            other.pages
        )
```

---

# Interview Questions Based on Your Code

### Q1. Why does `len(book1)` call `__len__()` automatically?

**Answer:** Because `len()` is a built-in function that looks for the object's `__len__()` magic method.

---

### Q2. Why should `__eq__()` return `NotImplemented` for unrelated types?

**Answer:** It tells Python that the comparison isn't supported for that type, allowing Python to try the reverse comparison or return `False` gracefully instead of raising an unexpected error.

---

### Q3. Why is `__repr__()` different from `__str__()`?

**Answer:**

* `__str__()` is for end users and focuses on readability.
* `__repr__()` is for developers and should ideally provide an unambiguous representation of the object.

---

# Evaluation

| Topic                | Score |
| -------------------- | ----: |
| `__init__`           | ⭐⭐⭐⭐⭐ |
| `__str__`            | ⭐⭐⭐⭐⭐ |
| `__repr__`           | ⭐⭐⭐⭐☆ |
| `__len__`            | ⭐⭐☆☆☆ |
| `__eq__`             | ⭐⭐⭐⭐☆ |
| Overall Code Quality | ⭐⭐⭐⭐☆ |

**Overall Score: 8.8/10**

The main issue was `__len__()`, which should have returned the number of pages rather than the length of the title. Apart from that, your implementation is solid, and the suggested improvements are about writing more robust, production-ready Python.

---

## 🎉 Congratulations!

**Lesson 11 is now officially complete.**

By completing Lessons 1–11, you've built a strong Python foundation. You're ready to move on to **Lesson 12: Exception Handling**, where you'll learn:

* `try`
* `except`
* `else`
* `finally`
* `raise`
* Creating custom exceptions
* Exception handling best practices used in real-world applications and AI projects
