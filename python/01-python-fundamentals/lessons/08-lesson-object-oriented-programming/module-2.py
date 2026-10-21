# Exercise 1

# Create:

# class Car

# Constructor:

# brand

# Method:

# show_brand()

# Create two objects.

# Example:

# Car("BMW")

# Car("Audi")


# class Car:

#     def __init__(self,brand):
#         self.brand = brand
    
#     def show_brand(self):
#         print(self.brand)

# bmw = Car("BMW")

# bmw.show_brand()

# audi =  Car("Audi")

# audi.show_brand()

# Exercise 2

# Create:

# class Employee

# Constructor

# name

# salary

# Method

# show_details()

# Print:

# Name : Bhupendra

# Salary : 85000

# class Employee:

#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
    
#     def show_details(self):
#         print(f"Name : {self.name}")
#         print(f"Salary : {self.salary}")

# employee = Employee("Bhupendra",85000)

# employee.show_details()



# Exercise 3

# Create:

# class Product

# Constructor

# sku

# name

# price

# Method

# show_product()

# class Product:

#     def __init__(self , sku ,name,price):
#         self.sku = sku
#         self.name = name
#         self.price = price

#     def show_product(self):
#         print(f"SKU = {self.sku}")
#         print(f"Name = {self.name}")
#         print(f"Price = {self.price}")

# product = Product("0001","Laptop",199.99)

# product.show_product()


# Exercise 4

# Create two Product objects with different values.

# Call:

# show_product()

# for both.


# mobile = Product("000002","Iphone",99.99)

# mobile.show_product()

# charger = Product("000003","Charger",9.99)

# charger.show_product()


# Mini Project
# Student Report

# Create

# class Student

# Constructor

# name , age , marks

# Methods  show_details() ,  is_pass()

# Rules If marks  >=35  Print PASS  Else FAIL

class Student:

    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def show_details(self):
        print(f"Name = {self.name}")
        print(f"Age = {int(self.age)}")
        print(f"Marks = {self.marks}")

    def is_pass(self):
        if float(self.marks) >= 35:
            print("PASS")
        else:
            print("FAIL")

student1 = Student("Bhupendra",37,40)

student1.show_details()
student1.is_pass()

student2 = Student("Rahul",24,34)

student2.show_details()
student2.is_pass()