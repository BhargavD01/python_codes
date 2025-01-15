#Define classes Circle, Square, and Triangle each with a draw() method. Call draw() on a list of shape objects to demonstrate polymorphism.
class Circle:
    def draw(self):
        print("Circle")

class Square:
    def draw(self):
        print("Square")

class Triangle:
    def draw(self):
        print("Triangle")

shapes = [Circle(), Square(), Triangle()]  # List of shape objects

for shape in shapes:
    shape.draw()  # Call the draw method on each shape