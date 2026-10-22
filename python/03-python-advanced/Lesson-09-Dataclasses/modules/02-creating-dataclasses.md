# Module 2 – Creating Dataclasses

Basic syntax:

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    email: str
```

Create an object:

```python
user = User(
    "Bhupendra",
    30,
    "bhupendra@example.com"
)

print(user)
```

Output:

```text
User(name='Bhupendra', age=30, email='bhupendra@example.com')
```

You can access fields normally:

```python
print(user.name)
print(user.age)
print(user.email)
```

---

