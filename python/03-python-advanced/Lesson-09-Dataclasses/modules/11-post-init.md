# Module 11 – `__post_init__()`

Sometimes you want to perform additional processing after the dataclass has been initialized.

Use:

```python
__post_init__()
```

Example:

```python
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        self.name = self.name.strip()
```

Now:

```python
product = Product(
    "  Laptop  ",
    60000.0
)

print(product.name)
```

Output:

```text
Laptop
```

`__post_init__()` runs automatically after the generated `__init__()`.

---

