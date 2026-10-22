# Module 6 – Time Zones

Time zone handling is especially important for applications that work with users, APIs, orders, logs, and distributed systems.

Python's modern approach is to use:

```python
zoneinfo
```

Import it using:

```python
from zoneinfo import ZoneInfo
```

---

## Current Time in India

```python
from datetime import datetime
from zoneinfo import ZoneInfo

india_time = datetime.now(
    ZoneInfo("Asia/Kolkata")
)

print(india_time)
```

---

## Current Time in New York

```python
from datetime import datetime
from zoneinfo import ZoneInfo

new_york_time = datetime.now(
    ZoneInfo("America/New_York")
)

print(new_york_time)
```

---

