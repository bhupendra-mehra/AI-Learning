# Module 8 – Frozen Dataclasses

A frozen dataclass is **immutable**.

Use:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    name: str
    price: float
```

Create:

```python
product = Product(
    "Laptop",
    60000.0
)
```

Trying to change it:

```python
product.price = 65000.0
```

will raise an error.

The object is intended to behave as immutable data.

This is useful when you want configuration or data objects that shouldn't accidentally be modified.

---

