import json

student = {
    "id": 1,
    "name": "Rahul Sharma",
    "email": "rahul@example.com",
    "age": 22,
    "skills": ["Python", "SQL"],
}

# Convert a Python dictionary to a JSON string.
json_string = json.dumps(student, indent=2)

print("JSON Data:")
print(json_string)

# Convert the JSON string back to a Python dictionary.
parsed_student = json.loads(json_string)

print("\nStudent Name:", parsed_student["name"])
print("Student Age:", parsed_student["age"])
print("Student Skills:", parsed_student["skills"])

# Writing JSON to a File


student = {
    "id": 1,
    "name": "Rahul Sharma",
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=2)


# Reading JSON from a File


with open("student.json", encoding="utf-8") as file:
    student = json.load(file)

print(student["name"])