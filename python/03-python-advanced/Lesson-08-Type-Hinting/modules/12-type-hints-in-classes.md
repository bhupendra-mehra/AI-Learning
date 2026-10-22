# Module 12 – Type Hints in Classes

Type hints are also useful with classes.

```python
class Product:

    name: str
    price: float

    def __init__(
        self,
        name: str,
        price: float
    ) -> None:

        self.name = name
        self.price = price
```

Then:

```python
product = Product(
    "Laptop",
    60000.0
)
```

This becomes especially important when we reach **Lesson 09 – Dataclasses**.

---

