# Module 3 – Formatting with `strftime()`

Formatting converts a Python `datetime` object into a readable string.

```python
from datetime import datetime

now = datetime.now()

formatted = now.strftime("%d-%m-%Y")

print(formatted)
```

Example:

```text
22-08-2026
```

---

## Common `strftime()` Codes

| Code | Meaning                | Example    |
| ---- | ---------------------- | ---------- |
| `%Y` | 4-digit year           | `2026`     |
| `%y` | 2-digit year           | `26`       |
| `%m` | Month                  | `08`       |
| `%d` | Day                    | `22`       |
| `%H` | Hour in 24-hour format | `18`       |
| `%I` | Hour in 12-hour format | `06`       |
| `%M` | Minute                 | `30`       |
| `%S` | Second                 | `25`       |
| `%p` | AM/PM                  | `PM`       |
| `%A` | Full weekday           | `Saturday` |
| `%B` | Full month             | `August`   |

---

## Formatting Examples

```python
from datetime import datetime

now = datetime.now()

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%d %B %Y"))
print(now.strftime("%A, %d %B %Y"))
print(now.strftime("%d-%m-%Y %H:%M:%S"))
print(now.strftime("%d-%m-%Y %I:%M %p"))
```

Possible output:

```text
22-08-2026
22/08/2026
22 August 2026
Saturday, 22 August 2026
22-08-2026 18:30:25
22-08-2026 06:30 PM
```

---

