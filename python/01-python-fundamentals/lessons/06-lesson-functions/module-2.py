# Exercises
# Exercise 1

# Create a function

# greet(name)

# Print

# Welcome Bhupendra

# Call it twice with different names.

# def greet(name):
#     print(f"Welcome {name}")

# greet("Bhupendra")

# Exercise 2

# Create

# multiply(a, b)

# Return the multiplication.

# Example

# result = multiply(5, 6)

# print(result)

# Output

# 30

# def multiply(a,b):
#     return a * b

# result = multiply(5,6)
# print(result)


# Exercise 3

# Predict the output.

# def test(a):
#     print(a)

# test(100)




# Exercise 4

# Predict the output.

# name = "Python"

# def show():
#     print(name)

# show()
# Exercise 5

# Predict whether this works.

# def show():
#     age = 25

# show()

# print(age)

# If not, explain why.

# Mini Project
# Employee Salary Calculator

# Requirements

# Create

# calculate_salary(hours, rate)

# Return

# hours × rate

# Then

# hours = int(input(...))

# rate = int(input(...))

# salary = calculate_salary(hours, rate)

# print(salary)


def calculate_salary(hours, rate):
    return hours * rate

hours = int(input("Enter hours :"))
rate  = int(input("Enter rate :"))
salary = calculate_salary(hours , rate)

print(salary)