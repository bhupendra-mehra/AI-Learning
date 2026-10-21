# Mini Exercise

# Create a small program with:

# An abstract class Shape containing an abstract method area().
# Two child classes:
# Rectangle
# Circle
# Use encapsulation by making dimensions private.
# Create objects of both classes and print their areas.
# Store both objects in a list and call area() on each to demonstrate polymorphism.

from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self,__length = 10,__width = 20):
        self.__length = __length
        self.__width = __width
    
    def area(self):
        return self.__length * self.__width


class Circle(Shape):

    def __init__(self ,__radius = 10):
        self.__radius = __radius
    
    def area(self):
        return 3.14 * (self.__radius ** 2)

shapes = [Rectangle(5,6),Circle(5)]

for shape in shapes:
    print(shape.area())