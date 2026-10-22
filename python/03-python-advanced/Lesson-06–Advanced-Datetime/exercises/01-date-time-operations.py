from datetime import datetime,date

now = datetime.now()

print("Full: ",now)
print("Year: ",now.year)
print("Month: ",now.month)
print("Day: ",now.day)
print("Hour: ",now.hour)
print("Minute: ",now.minute)
print("Second: ",now.second)

#Date
today = date.today()

print("Today : ",today)

#Create a Specific Date and Time
#datetime(year, month, day, hour, minute, second)

order_date = datetime(2026, 8, 22, 18, 30, 0)

print(order_date)
