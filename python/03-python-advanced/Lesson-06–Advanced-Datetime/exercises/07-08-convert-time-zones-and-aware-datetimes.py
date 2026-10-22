from datetime import datetime
from zoneinfo import ZoneInfo

new_york = ZoneInfo("America/New_York")
india = ZoneInfo("Asia/Kolkata")


new_york_time = datetime(2026,8,22,15,45,tzinfo=new_york)
india_time = new_york_time.astimezone(india)

print("New York:", new_york_time)
print("India:", india_time)


#as datetime.now() will return "None" for now.tzinfo

now = datetime.now(ZoneInfo("Asia/Kolkata"))

print(now)
print(now.tzinfo)


