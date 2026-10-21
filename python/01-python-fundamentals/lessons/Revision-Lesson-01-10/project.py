# Project: Student Management System

# Estimated Time: 30–45 minutes

# Objective

# Build a console-based application that uses everything you've learned in Lessons 1–10.

# Requirements

# Create a menu:

# ========= MENU =========

# 1. Add Student
# 2. Show Students
# 3. Search Student
# 4. Update Marks
# 5. Delete Student
# 6. Exit
# Student Structure

# Store each student as a dictionary inside a list.

# Example:

# {
#     "roll_no": 101,
#     "name": "Rahul",
#     "age": 20,
#     "marks": 85
# }
# Functions

# Implement these functions:

# add_student()

# show_students()

# search_student()

# update_marks()

# delete_student()

# main_menu()
# Concepts Covered
# Variables
# Input/Output
# Data Types
# Operators
# Conditions
# Loops
# Functions
# Lists
# Dictionaries
# Bonus (Optional)
# Prevent duplicate roll_no.
# Show "Student Not Found" when appropriate.
# Display the average marks of all students.

#     "roll_no": 101,
#     "name": "Rahul",
#     "age": 20,
#     "marks": 85

students = []
def add_student():
    roll_no = input("Enter your roll no :")
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    marks = float(input("Enter your marks : "))

    for student in students:
        if student['roll_no'] == roll_no:
            print("Student already added")
            return

    students.append({
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "marks": marks
    })

    print("Student is added successfully")

def show_students():
    # print(students) instead use below
    if not students:
        print("No students found.")
        return

    print("\n===== STUDENT LIST =====")

    for student in students:
        print(f"Roll No : {student['roll_no']}")
        print(f"Name    : {student['name']}")
        print(f"Age     : {student['age']}")
        print(f"Marks   : {student['marks']}")
        print("------------------------")

def search_student():
    roll_no = input("Enter Roll no to search : ")
    for student in students:
        if student['roll_no'] == roll_no:
            print(student)
            return
    
    print("No student found.")

def update_marks():
    roll_no = input("Enter roll no to update : ")
    marks = float(input("Enter marks to update : "))
    for student in students:
        if student['roll_no'] == roll_no:
            student['marks'] = marks
            print(student)
            print("Student marked updated successfully")
            return
        else:
            print("No student found.")

def delete_student():
    roll_no = input("Enter roll no to delete student: ")
    for student in students:
        if student['roll_no'] == roll_no:
            students.remove(student)
            print("Student deleted successfully")
            return


def main_menu():
    while True:
        print("========= MENU =========")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")
        option = int(input("Choose any one option from above : "))
        if option == 1:
            add_student()
        elif option == 2:
            show_students()
        elif option == 3:
            search_student()
        elif option == 4:
            update_marks()
        elif option == 5:
            delete_student()
            show_students()
        elif option == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid option")
        
main_menu()
    

# Optional Enhancement

# Since you've already learned functions, you can reduce duplicate code.

# Instead of searching in three different functions, create one helper:

# def find_student(roll_no):
#     for student in students:
#         if student["roll_no"] == roll_no:
#             return student
#     return None

# Then use it like this:

# student = find_student(roll_no)

# if student:
#     student["marks"] = marks
# else:
#     print("Student not found.")