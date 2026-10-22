# Module 1 – What Is a Dataclass?

A **dataclass** is a convenient way to create classes that mainly store data.

Without a dataclass, you might write:

```python
class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
```

Then:

```python
product = Product(
    "Laptop",
    60000.0,
    "Electronics"
)

print(product.name)
print(product.price)
```

This works, but there is a lot of repetitive code.

With a dataclass:

```python
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    category: str
```

Now:

```python
product = Product(
    "Laptop",
    60000.0,
    "Electronics"
)

print(product)
```

Output:

```text
Product(name='Laptop', price=60000.0, category='Electronics')
```

The dataclass automatically generates useful methods such as `__init__()` and `__repr__()`.

---

