# Module 8 – `Any`

You may also encounter:

```python
from typing import Any
```

Example:

```python
def process_data(data: Any) -> None:
    print(data)
```

`Any` essentially says:

> Don't perform strict type checking for this value.

Use it carefully.

Avoid doing this everywhere:

```python
def process_data(data: Any) -> Any:
    ...
```

because you're losing much of the benefit of type hints.

---

