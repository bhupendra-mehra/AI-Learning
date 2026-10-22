# Module 7 – Other `field()` Options

You can control how fields behave.

For example:

```python
from dataclasses import dataclass, field


@dataclass
class User:
    username: str
    password: str = field(repr=False)
```

Now:

```python
user = User(
    "bhupendra",
    "secret123"
)

print(user)
```

The password won't appear in the generated representation.

You might get:

```text
User(username='bhupendra')
```

This is useful when a field shouldn't appear in `repr()` output.

---

