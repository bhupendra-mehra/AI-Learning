from datetime import datetime

now = datetime.now()

formatted = now.strftime("%d-%m-%Y")

print(formatted)

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%d %B %Y"))
print(now.strftime("%A, %d %B %Y"))
print(now.strftime("%d-%m-%Y %H:%M:%S"))
print(now.strftime("%d-%m-%Y %I:%M %p"))