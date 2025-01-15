#Create a class that uses the @property decorator to get/set an attribute with some validation logic.
class Person:
    def __init__(self, name, age):
        self._name = name  # Private attribute
        self._age = age    # Private attribute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

# Create an instance of the Person class
person = Person("Alice", 30)

# Access the attributes
print("Name:", person.name)  # Output: Name: Alice
print("Age:", person.age)    # Output: Age: 30

# Update the attributes
person.name = "Bob"
person.age = 35

# Display updated values
print("Updated Name:", person.name)  # Output: Updated Name: Bob
print("Updated Age:", person.age)    # Output: Updated Age: 35

# Attempt to set invalid values
try:
    person.name = ""  # This will raise a ValueError
except ValueError as e:
    print(e)  # Output: Name cannot be empty.

try:
    person.age = -5  # This will raise a ValueError
except ValueError as e:
    print(e)  # Output: Age cannot be negative.