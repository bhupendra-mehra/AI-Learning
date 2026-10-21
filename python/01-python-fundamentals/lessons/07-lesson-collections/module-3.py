# Exercises
# Exercise 1

# Create a dictionary:

# student = {
#     "name": "Bhupendra",
#     "age": 37,
#     "city": "Mumbai"
# }

# Print:

# Name
# City

student = {
    "name": "Bhupendra",
    "age" : 37,
    "city" : "Mumbai"
}

# print(student.get('name'))
# print(student.get('city'))



# Exercise 2

# Update:

# city → Pune

# Add:

# profession → Magento Developer

# Print the dictionary.

student["city"] = "Pune"
student["profession"] = "Magento Developer"

print(student)

# Exercise 3

# Remove:

# age

# Print the updated dictionary.

student.pop("age")

print(student)



# Exercise 4

# Loop through the dictionary using:

# items()

# Print:

# name : Bhupendra
# city : Pune
# profession : Magento Developer

for key,value in student.items():
    print(f"{key}:{value}")

# Exercise 5

# Create:

# product = {
#     "sku": "ABC123",
#     "name": "Laptop",
#     "price": 50000
# }

# Print:

# product.get("price")

# Then try:

# product.get("qty")

# Observe the output.


product = {
    "sku" :"ABC123",
    "name" :"Laptop",
    "price" :"50000"  #store this as int instead of str
}

print(product.get("price"))
print(product.get("qty"))

# Mini Project
# Employee Information System

# Requirements

# Create a dictionary:

# employee = {
#     "id":101,
#     "name":"Bhupendra",
#     "department":"IT",
#     "salary":85000
# }

# Display all employee information using:

# for key, value in employee.items():

employee = {
    "id" :"101", #store this as int instead of str
    "name" :"Bhupendra",
    "department" :"IT",
    "salary" :85000
}

print("======Employee Information")
for key,value in employee.items():
    print(f"{key} : {value}")
print("==========================")