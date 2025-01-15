#Demonstrate polymorphism by defining a method draw() in multiple classes (Circle, Triangle, etc.) and calling draw() on a list of shapes.
class Circle:
    def draw(self):
        return "Drawing a Circle"

class Triangle:
    def draw(self):
        return "Drawing a Triangle"

class Square:
    def draw(self):
        return "Drawing a Square"

# List of shapes
shapes = [Circle(), Triangle(), Square()]

# Call the draw method on each shape
for shape in shapes:
    print(shape.draw())