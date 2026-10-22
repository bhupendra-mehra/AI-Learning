from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


timestamp = "2026-08-22 15:45:00"

new_york = ZoneInfo("America/New_York")
india = ZoneInfo("Asia/Kolkata")


# 1. Parse timestamp
date_object = datetime.strptime(
    timestamp,
    "%Y-%m-%d %H:%M:%S"
)


# 2. Create source timezone
new_york_time = date_object.replace(
    tzinfo=new_york
)


# 3. Convert to India timezone
india_time = new_york_time.astimezone(india)


# 4. Calculate 48-hour deadline
deadline = india_time + timedelta(hours=48)


# 5. Format and print results
print(
    "New York:",
    new_york_time.strftime("%d-%m-%Y %I:%M %p")
)

print(
    "India:",
    india_time.strftime("%d-%m-%Y %I:%M %p")
)

print(
    "48-hour Deadline:",
    deadline.strftime("%d-%m-%Y %I:%M %p")
)