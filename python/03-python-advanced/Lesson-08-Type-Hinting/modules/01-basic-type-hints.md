# Module 1 – Basic Type Hints

Python is dynamically typed.

Without type hints:

```python
def add(a, b):
    return a + b
```

Python doesn't explicitly tell us what `a` and `b` should be.

With type hints:

```python
def add(a: int, b: int) -> int:
    return a + b
```

This tells developers and tools:

```text
a       → int
b       → int
return  → int
```

### Important

Type hints **do not automatically enforce types at runtime**.

For example:

```python
def add(a: int, b: int) -> int:
    return a + b

print(add("Hello", "World"))
```

Python will still execute it and produce:

```text
HelloWorld
```

The type hint is mainly information for:

* Developers
* IDEs
* Linters
* Static type checkers
* Documentation

---

