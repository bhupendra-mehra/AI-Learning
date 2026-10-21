# Exercises
# Exercise 1

# Create a tuple of 5 cities.

# Print:

# First city
# Last city

cities = ("Bhopal","Indore","Gwalior","Jabalpur","Ujjain")

print(cities[0])
print(cities[-1])


# Exercise 2

# Try changing the first city.

# Observe the error and tell me why it occurs.

cities[0] = 'Raipur'

# Exercise 3

# Create a set:

# {"Apple", "Banana", "Apple", "Orange"}

# Print the result.

fruits = {"Apple", "Banana", "Apple", "Orange"}

print(fruits)

# Exercise 4

# Add "Mango" to the set.

# Remove "Banana".

# Print the final set.

fruits.add("Mango")
fruits.remove("Banana")

print(fruits)

# Exercise 5

# Create:

# A = {1, 2, 3, 4}

# B = {3, 4, 5, 6}

# Print:

# Union
# Intersection

A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

print(A | B)

print(A & B)


# Mini Project
# Student Registration System

# Requirements

# Create a set containing student names.

# Rahul
# Amit
# Rahul
# Priya
# Amit

students = {"Rahul","Amit","Rahul","Priya","Amit"}

print(students)

# Print the final set.

# Observe that duplicate names are automatically removed.