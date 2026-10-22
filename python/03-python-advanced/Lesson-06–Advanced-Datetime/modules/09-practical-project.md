# Module 9 – Practical Project

## Order Timestamp Converter

Suppose an API provides this timestamp:

```python
order_timestamp = "2026-08-22 10:30:00"
```

The timestamp represents New York time.

We need to:

1. Parse the string.
2. Attach the New York timezone.
3. Convert it to India time.
4. Calculate the expiry time after 24 hours.
5. Format the result for display.

---

## Complete Example

```python
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


# Original timestamp from API
order_timestamp = "2026-08-22 10:30:00"


# Time zones
new_york = ZoneInfo("America/New_York")
india = ZoneInfo("Asia/Kolkata")


# 1. Parse string into datetime
order_time = datetime.strptime(
    order_timestamp,
    "%Y-%m-%d %H:%M:%S"
)


# 2. Attach timezone
order_time = order_time.replace(
    tzinfo=new_york
)


# 3. Convert to India time
india_time = order_time.astimezone(india)


# 4. Calculate expiration
expiry_time = order_time + timedelta(hours=24)


# 5. Format for display
formatted_order = india_time.strftime(
    "%d-%m-%Y %I:%M %p"
)

formatted_expiry = expiry_time.strftime(
    "%d-%m-%Y %I:%M %p %Z"
)


print("Original Order Time:", order_time)
print("India Order Time:", formatted_order)
print("Expiry Time:", formatted_expiry)
```

---

# Lesson 06 – Complete Mental Model

The main datetime workflow can be understood as:

```text
                    datetime
                       |
            +----------+----------+
            |                     |
        Formatting             Parsing
        strftime()             strptime()
            |                     |
            v                     v
         string               datetime
```

For durations:

```text
datetime
   |
   +---- timedelta
            |
            +---- add time
            |
            +---- subtract time
            |
            +---- calculate duration
```

For time zones:

```text
datetime
   |
   +---- ZoneInfo
            |
            +---- timezone-aware datetime
            |
            +---- astimezone()
                       |
                       v
                another timezone
```

---

# Important Functions to Remember

```python
datetime.now()
datetime(...)
datetime.strptime()
datetime.strftime()

timedelta(...)
date.today()

ZoneInfo(...)
datetime.astimezone()
```

---

# Final Exercise

Build the following program yourself.

### Input

```text
API timestamp:
2026-08-22 15:45:00

Source timezone:
America/New_York

Target timezone:
Asia/Kolkata
```

### Requirements

1. Parse the timestamp using `strptime()`.
2. Make it timezone-aware.
3. Convert it to India time using `astimezone()`.
4. Add **48 hours** using `timedelta`.
5. Print the converted time in:

```text
DD-MM-YYYY HH:MM AM/PM
```

6. Print the 48-hour deadline.

### Expected structure

```python
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

timestamp = "2026-08-22 15:45:00"

# Parse timestamp


# Create source timezone


# Convert to India timezone


# Calculate 48-hour deadline


# Format and print results
```

## Lesson 06 Completion Criteria

Before marking the lesson complete, you should be comfortable with:

* [ ] Creating `datetime` objects
* [ ] Getting date/time components
* [ ] Comparing dates
* [ ] Formatting with `strftime()`
* [ ] Parsing with `strptime()`
* [ ] Adding/subtracting with `timedelta`
* [ ] Creating timezone-aware datetimes
* [ ] Converting time zones with `ZoneInfo` and `astimezone()`
* [ ] Understanding naive vs timezone-aware datetime
* [ ] Combining all concepts in a practical program

Once you complete the final exercise, **Lesson 06 – Advanced Datetime is complete** and we can move directly to **Lesson 07 – Logging**.

