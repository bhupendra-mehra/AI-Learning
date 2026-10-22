# Module 14 – Practical Project

Let's combine everything.

Create an order-processing program.

### Requirements

Each order contains:

```text
order_id → string
amount   → float
```

Create a type alias:

```python
Order = tuple[str, float]
```

Create:

```python
orders: list[Order]
```

Then create these functions:

### `calculate_total()`

```python
def calculate_total(
    amount: float,
    tax: float
) -> float:
```

Return:

```text
amount + tax
```

---

### `find_order()`

Create:

```python
def find_order(
    orders: list[Order],
    order_id: str
) -> Order | None:
```

Return the matching order or `None`.

---

### `get_order_ids()`

Create:

```python
def get_order_ids(
    orders: list[Order]
) -> list[str]:
```

Return only the order IDs.

---

## Starting Data

```python
Order = tuple[str, float]

orders: list[Order] = [
    ("ORD1001", 2500.0),
    ("ORD1002", 1500.0),
    ("ORD1003", 5000.0)
]
```

Your final program should demonstrate:

```text
Basic type hints
Generic types
Optional / None
Union using |
Type aliases
Function return types
```

### Expected behavior

```python
print(get_order_ids(orders))
```

should produce:

```text
['ORD1001', 'ORD1002', 'ORD1003']
```

And:

```python
print(find_order(orders, "ORD1002"))
```

should produce:

```text
('ORD1002', 1500.0)
```

while:

```python
print(find_order(orders, "ORD9999"))
```

should produce:

```text
None
```

---

# Complete Lesson 08 Example

Once you've attempted it yourself, the complete version should look like this:

```python
from typing import TypeAlias


Order: TypeAlias = tuple[str, float]


orders: list[Order] = [
    ("ORD1001", 2500.0),
    ("ORD1002", 1500.0),
    ("ORD1003", 5000.0)
]


def calculate_total(
    amount: float,
    tax: float
) -> float:

    return amount + tax


def find_order(
    orders: list[Order],
    order_id: str
) -> Order | None:

    for order in orders:

        if order[0] == order_id:
            return order

    return None


def get_order_ids(
    orders: list[Order]
) -> list[str]:

    return [
        order_id
        for order_id, amount in orders
    ]


print(get_order_ids(orders))

print(find_order(
    orders,
    "ORD1002"
))

print(find_order(
    orders,
    "ORD9999"
))

print(calculate_total(
    2500.0,
    450.0
))
```

Output:

```text
['ORD1001', 'ORD1002', 'ORD1003']
('ORD1002', 1500.0)
None
2950.0
```

---

# `typing.TypeAlias` vs Simple Alias

You may also see:

```python
Order = tuple[str, float]
```

This is perfectly valid for many situations.

Explicitly declaring:

```python
from typing import TypeAlias

Order: TypeAlias = tuple[str, float]
```

makes it clear that `Order` is intended to be a **type alias**.

For this course, you don't need to overuse `TypeAlias`. Just understand both forms.

---

# Lesson 08 – What You Should Remember

### Basic types

```python
name: str
age: int
price: float
active: bool
```

### Functions

```python
def add(a: int, b: int) -> int:
```

### Collections

```python
list[str]
dict[str, int]
tuple[str, float]
set[int]
```

### Optional

```python
str | None
```

### Union

```python
int | str
```

### Type alias

```python
Order = tuple[str, float]
```

### Static checking

```bash
mypy app.py
```

---

# Lesson 08 – Completion Criteria

* [ ] Basic type hints
* [ ] Function parameter and return hints
* [ ] Generic types
* [ ] `list`, `dict`, `tuple`, `set` type hints
* [ ] `Optional`
* [ ] `Union`
* [ ] Modern `|` syntax
* [ ] `Any`
* [ ] Type aliases
* [ ] Static type checking with `mypy`
* [ ] Type hints with classes
* [ ] Practical order-processing project

**Lesson 08 is complete after you build and run the practical project above.**

Next in the roadmap is **Lesson 09 – Dataclasses**, which should also be manageable in one session.

