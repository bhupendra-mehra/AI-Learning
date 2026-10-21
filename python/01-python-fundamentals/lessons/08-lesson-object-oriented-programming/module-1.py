# Exercise 1

# Create an empty class:

# class Car:
#     pass

# Create two objects of Car.

# Print both objects.

# class Car:
#     pass


# red = Car()
# print(red)
# blue = Car()
# print(blue)


# Exercise 2

# Create:

# class Animal:

#     def sound(self):
#         print("Animal Sound")

# Create an object and call sound().


# class Animal:

#     def sound(self):
#         print("Animal Sound")

# tiger = Animal()
# tiger.sound()


# Exercise 3

# Create:

# class Calculator:

#     def add(self, a, b):
#         print(a + b)

# Call:

# calculator.add(10, 20)

# class Calculator:

#     def add(self, a, b):
#         print(a + b)

# calculator = Calculator()
# calculator.add(1,2)

# Exercise 4

# Create a class:

# class Employee:

#     def show_company(self):
#         print("Encora")

# Create three objects and call the method using each object.

# class Employee:

#     def show_company(self):
#         print("Encora")


# bhupendra = Employee()
# bhupendra.show_company()



# Mini Project

# Create a Student class.

# Methods:

# show_name(name)

# show_marks(marks)

# Example:

# student = Student()

# student.show_name("Bhupendra")

# student.show_marks(95)

class Student:

    def show_name(self,name):
        print(f"My name is {name}")
    
    def show_marks(self, marks):
        print(f"I have got {marks} out of 100")


student = Student()

student.show_name("Bhupendra")
student.show_marks(95)