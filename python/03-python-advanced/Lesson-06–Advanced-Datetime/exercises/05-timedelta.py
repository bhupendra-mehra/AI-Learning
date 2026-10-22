from datetime import datetime,timedelta

now = datetime.now()

future = now + timedelta(days = 7)

print("Now:", now)
print("After 7 days:", future)

yesterday = now - timedelta(days=1)

print("Yesterday :" , yesterday)

now = datetime.now()

future = now + timedelta(hours=5)

print(future)

start = datetime(2026, 8, 20)
end = datetime(2026, 8, 22)

difference = end - start

print(difference)
print(difference.days)