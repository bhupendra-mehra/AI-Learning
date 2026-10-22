# Module 6 – `field()`

The `field()` function provides more control over dataclass fields.

```python
from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float
    tags: list[str] = field(default_factory=list)
```

Now:

```python
product = Product(
    "Laptop",
    60000.0
)

print(product)
```

Output:

```text
Product(name='Laptop', price=60000.0, tags=[])
```

---

# Why `default_factory`?

Don't do this:

```python
@dataclass
class Product:
    name: str
    tags: list[str] = []
```

For mutable defaults such as lists and dictionaries, use:

```python
field(default_factory=list)
```

This ensures each object gets its **own list**.

Example:

```python
from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    tags: list[str] = field(default_factory=list)


product1 = Product("Laptop")
product2 = Product("Mouse")

product1.tags.append("computer")

print(product1.tags)
print(product2.tags)
```

Output:

```text
['computer']
[]
```

The two objects have independent lists.

---

