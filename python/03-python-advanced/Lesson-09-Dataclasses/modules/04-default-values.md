# Module 4 – Default Values

Dataclasses allow fields to have default values.

```python
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    category: str = "General"
```

Now:

```python
product = Product(
    "Mouse",
    1500.0
)

print(product)
```

Output:

```text
Product(name='Mouse', price=1500.0, category='General')
```

You can still provide the value:

```python
product = Product(
    "Laptop",
    60000.0,
    "Electronics"
)
```

---

