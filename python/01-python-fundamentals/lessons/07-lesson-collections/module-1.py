# Exercises
# Exercise 1

# Create a list of 5 fruits and print the entire list.

fruits = ['Apple','Banana','Cherry','Papaya','Watermelon']

print(fruits)


# Exercise 2

# Print:

# First fruit
# Last fruit

print(fruits[0])
print(fruits[-1])


# Exercise 3

# Replace the third fruit with "Mango" and print the updated list.

fruits[2] = 'Mango'

print(fruits)

# Exercise 4

# Add "Orange" to the list, remove the first fruit, and print the final list.

fruits.append('Orange')
fruits.remove('Apple')
print(fruits)


# Exercise 5

# Create a list of 5 numbers and print each number using a for loop.

numbers = [1,2,3,4,5]
for number in numbers:
    print(number)