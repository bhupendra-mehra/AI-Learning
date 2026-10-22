from datetime import datetime

date_string = "22-08-2026"

date_object = datetime.strptime(date_string,"%d-%m-%Y")

print(date_object)


date_string1 = "22/08/2026 18:30"

date_object1 = datetime.strptime(
    date_string1,
    "%d/%m/%Y %H:%M"
)

print(date_object1)