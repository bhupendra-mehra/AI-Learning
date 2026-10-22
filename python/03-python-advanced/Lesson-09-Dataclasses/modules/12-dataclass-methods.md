# Module 12 – Dataclass Methods

A dataclass can contain normal methods.

```python
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float

    def apply_discount(self, percentage: float) -> float:
        return self.price - (
            self.price * percentage / 100
        )
```

Use it:

```python
product = Product(
    "Laptop",
    60000.0
)

discounted_price = product.apply_discount(10)

print(discounted_price)
```

Output:

```text
54000.0
```

So a dataclass isn't limited to storing data. It can also contain behavior.

---

