# Module 2 – Common Basic Type Hints

## Variables

```python
name: str = "Bhupendra"
age: int = 30
price: float = 25999.50
is_active: bool = True
```

---

## Function Parameters

```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

Another example:

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
```

---

## Functions Without a Return Value

Use:

```python
-> None
```

Example:

```python
def print_order(order_id: str) -> None:
    print(f"Order: {order_id}")
```

This means the function doesn't return a value.

---

