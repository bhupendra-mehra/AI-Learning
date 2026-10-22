# Module 9 – Type Aliases

Sometimes a type is complicated.

Instead of:

```python
orders: list[tuple[str, float]]
```

everywhere, you can create a type alias.

```python
Order = tuple[str, float]

orders: list[Order] = [
    ("ORD1001", 2500.0),
    ("ORD1002", 1500.0)
]
```

Now:

```python
def process_orders(
    orders: list[Order]
) -> None:
    ...
```

is easier to read.

---

