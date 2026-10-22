# Module 7 – `Union`

`Union` means a value can be **one of several types**.

Older syntax:

```python
from typing import Union

def process_id(
    value: Union[int, str]
) -> str:

    return str(value)
```

The parameter can be:

```text
int
```

or:

```text
str
```

Modern Python:

```python
def process_id(value: int | str) -> str:
    return str(value)
```

This is generally easier to read.

---

## Example

```python
def format_order_id(
    order_id: int | str
) -> str:

    return f"ORD-{order_id}"
```

Both work:

```python
print(format_order_id(12345))
print(format_order_id("12345"))
```

Output:

```text
ORD-12345
ORD-12345
```

---

