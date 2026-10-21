# Exercises
# Exercise 1

# Create

# class Vehicle

# Method

# start()

# Create

# class Car(Vehicle)

# Call

# start()

# using a Car object.


# class Vehicle:

#     def start(self):
#         print("Start")

# class Car(Vehicle):
#     pass

# car = Car()
# car.start()

# Exercise 2

# Add

# drive()

# inside Car.

# Call both

# start()

# drive()

# class Vehicle:

#     def start(self):
#         print("Start")

# class Car(Vehicle):
    
#     def drive(self):
#         print("Drive")

# car = Car()
# car.start()
# car.drive()



# Exercise 3

# Create

# class Person

# Method # show_role()

# Print # Person

# Create

# class Teacher(Person)

# Override # show_role()

# Print # Teacher

# class Person:

#     def show_role(self):
#         print("Person")
    
# class Teacher(Person):

#     def show_role(self):
#         print("Teacher")

# person = Person()
# person.show_role()

# teacher = Teacher()
# teacher.show_role()


# Exercise 4

# Modify the previous exercise.

# Inside

# Teacher.show_role()

# Call

# super().show_role()

# Then print

# Teacher

# Expected Output

# Person

# Teacher

# class Person:

#     def show_role(self):
#         print("Person")
    
# class Teacher(Person):

#     def show_role(self):
#         super().show_role()
#         print("Teacher")

# teacher = Teacher()
# teacher.show_role()



# Mini Project
# Product System

# Create

# class Product

# Constructor # name # price

# Method # show_product()

# Print # Name # Price

# Create

# class Electronics(Product)

# Additional Constructor # brand

# Use # super().__init__()

# Method # show_details()

# Print # Name # Price # Brand

class Product:

    def __init__(self , name ,price):
        self.name = name
        self.price = price
    
    def show_product(self):
        print(f"Name = {self.name}")
        print(f"Price = {self.price}")

class Electronics(Product):

    def __init__(self ,name,price, brand):
        super().__init__(name,price)
        self.brand = brand

    def show_details(self):
        super().show_product()
        print(f"Brand = {self.brand}")


table = Product("Table 1",38.33)
table.show_product()

mobile = Electronics("Iphone",999.99,"Apple")
mobile.show_details()