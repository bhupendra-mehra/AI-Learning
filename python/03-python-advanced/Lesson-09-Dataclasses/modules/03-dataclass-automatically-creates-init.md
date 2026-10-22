# Module 3 – Dataclass Automatically Creates `__init__`

Normally, you would need:

```python
class User:

    def __init__(
        self,
        name: str,
        age: int,
        email: str
    ):
        self.name = name
        self.age = age
        self.email = email
```

With:

```python
@dataclass
class User:
    name: str
    age: int
    email: str
```

Python generates the initialization logic for you.

So:

```python
User(
    "Bhupendra",
    30,
    "bhupendra@example.com"
)
```

works automatically.

---

