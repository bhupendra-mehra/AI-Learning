# Module 6 — `namedtuple`

A `namedtuple` is like a tuple whose values have meaningful names.

Normal tuple:

```python
user = ("Bhupendra", 37, "Magento Developer")

print(user[0])
print(user[1])
```

The problem is that:

```text
user[0]
user[1]
```

isn't very readable.

With `namedtuple`:

```python
from collections import namedtuple

User = namedtuple("User", ["name", "age", "role"])

user = User("Bhupendra", 37, "Magento Developer")

print(user.name)
print(user.age)
print(user.role)
```

Output:

```text
Bhupendra
37
Magento Developer
```

### Note

In modern Python projects, **dataclasses are usually preferred** for richer data models. We'll learn `dataclass` later in Part 3, Lesson 9.