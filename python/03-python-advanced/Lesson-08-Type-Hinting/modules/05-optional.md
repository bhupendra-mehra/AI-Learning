# Module 5 – `Optional`

`Optional` means a value can either contain a particular type **or `None`**.

For example:

```python
from typing import Optional

username: Optional[str] = None
```

This means:

```text
username → string OR None
```

A function:

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:

    if user_id == 1:
        return "Bhupendra"

    return None
```

The return value can be:

```text
str
```

or:

```text
None
```

---

## Modern Python Syntax

In modern Python, you can write:

```python
def find_user(user_id: int) -> str | None:
    ...
```

instead of:

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    ...
```

Both communicate the same concept.

For modern Python projects, you'll frequently see:

```python
str | None
```

---

