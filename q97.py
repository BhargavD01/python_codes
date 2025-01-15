#Create a class Point that overloads the + operator (using __add__) to add the coordinates of two Point objects.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Create two Point objects
point1 = Point(2, 3)
point2 = Point(4, 5)

# Add the two points
result = point1 + point2

# Print the result
print(result)  # Output: Point(6, 8)