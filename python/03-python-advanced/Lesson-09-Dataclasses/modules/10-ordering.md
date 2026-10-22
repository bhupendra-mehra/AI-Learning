# Module 10 – Ordering

You can also enable ordering:

```python
from dataclasses import dataclass


@dataclass(order=True)
class Product:
    name: str
    price: float
```

Now comparison operators can be used:

```python
product1 = Product("Laptop", 60000.0)
product2 = Product("Mouse", 1500.0)

print(product1 < product2)
```

However, be careful.

With:

```python
order=True
```

Python compares fields according to their declaration order.

For:

```python
@dataclass(order=True)
class Product:
    name: str
    price: float
```

`name` is considered before `price`.

If you specifically want to sort by price, it's often better to use:

```python
sorted(products, key=lambda product: product.price)
```

rather than relying on dataclass ordering.

---

