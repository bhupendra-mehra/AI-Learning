# Module 16 – Final Exercise

Before marking Lesson 09 complete, create your own `Product` dataclass.

Requirements:

```text
Product
├── name: str
├── price: float
├── category: str
├── quantity: int = 1
└── tags: list[str]
```

Use:

```python
field(default_factory=list)
```

Add a method:

```python
total_price()
```

which returns:

```text
price × quantity
```

Also add:

```python
__post_init__()
```

to remove whitespace from `name` and `category`.

Example:

```python
product = Product(
    name="  Laptop  ",
    price=60000.0,
    category="  Electronics  ",
    quantity=2
)

print(product)
print(product.total_price())
```

Expected:

```text
Product(
    name='Laptop',
    price=60000.0,
    category='Electronics',
    quantity=2,
    tags=[]
)

120000.0
```

---

# Lesson 09 – What You Should Remember

### Basic dataclass

```python
@dataclass
class Product:
    name: str
    price: float
```

### Default value

```python
category: str = "General"
```

### Mutable default

```python
tags: list[str] = field(default_factory=list)
```

### Immutable dataclass

```python
@dataclass(frozen=True)
class Product:
    ...
```

### Comparison

```python
product1 == product2
```

### Ordering

```python
@dataclass(order=True)
```

### Post initialization

```python
def __post_init__(self):
    ...
```

### Methods

```python
def total_price(self) -> float:
    return self.price * self.quantity
```

---

# Lesson 09 – Completion Criteria

* [ ] Create basic dataclasses
* [ ] Understand automatically generated `__init__()`
* [ ] Use type hints with dataclasses
* [ ] Use default values
* [ ] Understand field ordering
* [ ] Use `field()`
* [ ] Use `default_factory`
* [ ] Understand `frozen=True`
* [ ] Understand equality/comparison
* [ ] Understand `order=True`
* [ ] Use `__post_init__()`
* [ ] Add methods to dataclasses
* [ ] Understand dataclass vs `namedtuple`
* [ ] Understand dataclasses in AI/application development
* [ ] Complete the Product/Order project

## 🎯 Lesson 09 Status

**Lesson 09 – Dataclasses can be completed in one session.**

Once you run the final `Product` exercise successfully, **Lessons 01–09 of Part 3 will be complete**.

The only remaining lesson is:

# Lesson 10 – Project Structure

Topics:

* Professional Folder Structure
* Configuration Management
* Utilities
* Package Organization
* Best Practices

That final lesson will bring everything together into a **production-style Python project structure**, which is particularly useful before moving into APIs, data engineering, and AI/LLM development.

