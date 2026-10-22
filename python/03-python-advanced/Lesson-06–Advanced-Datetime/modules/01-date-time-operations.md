# Module 1 – Date & Time Operations

Python provides date and time functionality through the built-in `datetime` module.

## Current Date and Time

```python
from datetime import datetime

now = datetime.now()

print(now)
```

Example output:

```text
2026-08-22 18:30:25.123456
```

The structure is:

```text
YYYY-MM-DD HH:MM:SS.microseconds
```

---

## Access Individual Components

```python
from datetime import datetime

now = datetime.now()

print("Full:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
```

Example output:

```text
Full: 2026-08-22 18:30:25.123456
Year: 2026
Month: 8
Day: 22
Hour: 18
Minute: 30
Second: 25
```

These are attributes, not functions:

```python
now.year
now.month
now.day
```

Do not use:

```python
now.year()    # Incorrect
now.month()   # Incorrect
```

---

## Current Date Only

```python
from datetime import date

today = date.today()

print(today)
```

Example:

```text
2026-08-22
```

---

## Create a Specific Date and Time

```python
from datetime import datetime

order_date = datetime(2026, 8, 22, 18, 30, 0)

print(order_date)
```

Output:

```text
2026-08-22 18:30:00
```

The order of arguments is:

```python
datetime(year, month, day, hour, minute, second)
```

For example:

```python
datetime(2026, 8, 22, 18, 30, 0)
```

means:

```text
Year   = 2026
Month  = 8
Day    = 22
Hour   = 18
Minute = 30
Second = 0
```

---

