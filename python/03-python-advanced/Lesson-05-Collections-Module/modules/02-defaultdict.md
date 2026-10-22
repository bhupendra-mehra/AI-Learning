# Module 3 — `defaultdict`

A normal dictionary raises an error when you access a missing key:

```python
users = {}

print(users["admin"])
```

You get:

```text
KeyError
```

`defaultdict` automatically creates a default value.

```python
from collections import defaultdict

users = defaultdict(list)

users["admin"].append("Bhupendra")
users["admin"].append("Rahul")

print(users)
```

Output:

```text
defaultdict(<class 'list'>, {
    'admin': ['Bhupendra', 'Rahul']
})
```

Without `defaultdict`, you would need:

```python
if "admin" not in users:
    users["admin"] = []

users["admin"].append("Bhupendra")
```

---