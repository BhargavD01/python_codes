#Use the abc module to define an abstract base class Shape with an abstract method area(). Implement subclasses Circle and Rectangle
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Print the area of each shape
print("Area of Circle:", circle.area())      # Output: Area of Circle: 78.53981633974483
print("Area of Rectangle:", rectangle.area()) # Output: Area of Rectangle: 24