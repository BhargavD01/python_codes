#Define a class Point(x, y) that overloads the + operator to add the coordinates of two Point objects
class Point:
    def __init__(self, x, y):
        self.x = x  # x coordinate
        self.y = y  # y coordinate

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)  # Add coordinates

    def __repr__(self):
        return f"Point({self.x}, {self.y})"  # String representation

p1 = Point(2, 3)  # Create first Point
p2 = Point(4, 5)  # Create second Point
p3 = p1 + p2     # Add the two Points

print(p3)  # Output the result