# Module 3 – Generic Types

Generic types describe the types contained inside collections.

Modern Python allows:

```python
list[str]
dict[str, int]
tuple[str, int]
set[int]
```

---

## List

```python
products: list[str] = [
    "Laptop",
    "Mouse",
    "Keyboard"
]
```

This means:

> `products` is a list containing strings.

---

## List of Integers

```python
prices: list[int] = [
    1000,
    2000,
    3000
]
```

---

## Dictionary

```python
product_prices: dict[str, float] = {
    "Laptop": 60000.0,
    "Mouse": 1500.0
}
```

Meaning:

```text
key   → str
value → float
```

---

## Tuple

```python
product: tuple[str, float] = (
    "Laptop",
    60000.0
)
```

---

## Set

```python
product_ids: set[int] = {
    101,
    102,
    103
}
```

---

