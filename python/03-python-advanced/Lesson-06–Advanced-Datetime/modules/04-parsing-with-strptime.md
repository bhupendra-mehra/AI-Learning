# Module 4 – Parsing with `strptime()`

Parsing performs the opposite operation of formatting.

```text
datetime → string
```

uses:

```python
strftime()
```

Whereas:

```text
string → datetime
```

uses:

```python
strptime()
```

---

## Parse a Date String

```python
from datetime import datetime

date_string = "22-08-2026"

date_object = datetime.strptime(
    date_string,
    "%d-%m-%Y"
)

print(date_object)
```

Output:

```text
2026-08-22 00:00:00
```

---

## Parse Date and Time

```python
from datetime import datetime

date_string = "22/08/2026 18:30"

date_object = datetime.strptime(
    date_string,
    "%d/%m/%Y %H:%M"
)

print(date_object)
```

Output:

```text
2026-08-22 18:30:00
```

---

## Remember

```text
strftime → datetime TO string

strptime → string TO datetime
```

A simple way to remember:

```text
strftime = format
strptime = parse
```

---

