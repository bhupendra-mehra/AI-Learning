from datetime import datetime
from zoneinfo import ZoneInfo

new_york_time = datetime.now(ZoneInfo("America/New_York"))

print(new_york_time)


