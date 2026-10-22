# Module 15 – Why `if __name__ == "__main__"`?

Suppose:

```python
# calculator.py

def add(a, b):
    return a + b


print("Calculator loaded")
```

If another file does:

```python
from calculator import add
```

the `print()` also executes.

Instead:

```python
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(10, 20))
```

Now the test code only runs when you execute:

```bash
python calculator.py
```

It doesn't run just because another module imports `add`.

---

