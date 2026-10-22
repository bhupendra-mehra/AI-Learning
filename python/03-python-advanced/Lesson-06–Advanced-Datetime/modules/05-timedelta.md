# Module 5 – `timedelta`

`timedelta` represents a duration or difference between dates and times.

```python
from datetime import datetime, timedelta

now = datetime.now()

future = now + timedelta(days=7)

print("Now:", now)
print("After 7 days:", future)
```

---

## Supported `timedelta` Arguments

```python
timedelta(
    days=,
    seconds=,
    minutes=,
    hours=,
    weeks=
)
```

---

## Subtract Time

```python
from datetime import datetime, timedelta

now = datetime.now()

yesterday = now - timedelta(days=1)

print(yesterday)
```

---

## Add Hours

```python
from datetime import datetime, timedelta

now = datetime.now()

future = now + timedelta(hours=5)

print(future)
```

---

## Calculate Difference Between Dates

```python
from datetime import datetime

start = datetime(2026, 8, 20)
end = datetime(2026, 8, 22)

difference = end - start

print(difference)
print(difference.days)
```

Output:

```text
2 days, 0:00:00
2
```

`timedelta` is useful for:

* Order processing time
* Delivery estimates
* Expiration
* Token lifetime
* Retry delays
* Job scheduling

---

