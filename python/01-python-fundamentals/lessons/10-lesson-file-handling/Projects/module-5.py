import json

# with open("student.json","r") as file:

#     data = json.load(file)

# print(data['name'])

# student = {
#     "name": "Rahul",
#     "age": 25,
#     "course": "AI"
# }

# with open("student.json","w") as file:

#     json.dump(student,file,indent=4)

employee = {
    "name": "John",
    "department": "IT",
    "salary": 5000
}

# with open("employee.json","w") as file:

#     json.dump(employee,file,indent=4)

with open("employee.json","r") as file:

    data = json.load(file)

print(data["name"])