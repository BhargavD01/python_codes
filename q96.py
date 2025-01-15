#Implement a Python class that overloads the __str__ method to return a string representation of the object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

# Create an instance of the Person class
person = Person("Alice", 30)

# Print the string representation of the person object
print(person)