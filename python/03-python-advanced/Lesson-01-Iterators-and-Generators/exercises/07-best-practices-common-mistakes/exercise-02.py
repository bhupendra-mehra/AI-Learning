# Create a text file with at least 10 lines.

# Write a Python program that reads and prints each line using a for loop.

with open("exercise-02.txt","r") as file:
    for line in file:
        print(line.strip())