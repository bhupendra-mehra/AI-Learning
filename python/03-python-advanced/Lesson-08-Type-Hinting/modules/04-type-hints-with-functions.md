# Module 4 – Type Hints with Functions

Consider:

```python
orders = [
    ("ORD1001", 2500),
    ("ORD1002", 1500)
]
```

We can define:

```python
def calculate_total(
    price: float,
    quantity: int
) -> float:

    return price * quantity
```

And:

```python
def get_order_ids(
    orders: list[tuple[str, float]]
) -> list[str]:

    return [
        order_id
        for order_id, amount in orders
    ]
```

The type hint tells us exactly what the function expects.

---

