# Module 9 – Comparison Methods

Dataclasses can automatically generate comparison methods.

Consider:

```python
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
```

Create:

```python
product1 = Product(
    "Laptop",
    60000.0
)

product2 = Product(
    "Laptop",
    60000.0
)

print(product1 == product2)
```

Output:

```text
True
```

Without implementing `__eq__()` yourself.

---

