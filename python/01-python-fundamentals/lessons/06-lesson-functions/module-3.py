# Exercise 1

# Create

# def greet(name="Guest"):

# Call it:

# Without an argument.
# With your name.

# def greet(name = "Guest"):
#     print(name)

# greet()
# greet("Bhupendra")

# Exercise 2

# Create

# def employee(name, age):

# Call it using keyword arguments.


# def employee(name = "Bhupendra", age = 37):
#     print(name,age)

# employee("Rahul",44)
# employee(age = 32 , name = "Tester")


# Exercise 3

# Create

# def add_numbers(*numbers):

# Return the sum of all numbers.

# Example:

# print(add_numbers(10, 20, 30))

# Output

# 60


# def add_numbers(*numbers):
#     sum_value = 0

#     for number in numbers:
#         sum_value += number
    
#     return sum_value

# print(add_numbers(10, 20, 30))


# Exercise 4

# Create

# def product(**details):

# Print:

# Product Name
# Price

# Call it with:

# name="Laptop"

# price=65000

# def product(**details):
#     return details

# data = product(name="Laptop",price ="111.99")

# print(f"Product Name {data['name']}")
# print(f"Price {data['price']}")


# Exercise 5

# Convert this function into a lambda:

# def double(x):
#     return x * 2

double = lambda x : x * 2

print(double(3))