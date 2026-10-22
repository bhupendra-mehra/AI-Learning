# Module 7 – Convert Between Time Zones

Suppose an event happened at:

```text
2026-08-22 10:00
```

in New York.

We want to convert that same moment to India time.

```python
from datetime import datetime
from zoneinfo import ZoneInfo

new_york = ZoneInfo("America/New_York")
india = ZoneInfo("Asia/Kolkata")

new_york_time = datetime(
    2026,
    8,
    22,
    10,
    0,
    tzinfo=new_york
)

india_time = new_york_time.astimezone(india)

print("New York:", new_york_time)
print("India:", india_time)
```

The important function is:

```python
astimezone()
```

It converts the same moment into another time zone.

---

## Avoid Manual Time Zone Calculations

Do not normally do this:

```python
# Avoid manual timezone arithmetic

india_time = new_york_time + timedelta(hours=9.5)
```

Instead use:

```python
# Correct approach

india_time = new_york_time.astimezone(
    ZoneInfo("Asia/Kolkata")
)
```

Using `ZoneInfo` allows Python to handle the rules associated with the selected time zone.

---

