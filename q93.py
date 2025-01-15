#Demonstrate encapsulation by creating a class with private attributes and use getter and setter methods to access/modify them.
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age >= 0:  # Simple validation
            self.__age = age

# Create an instance of the Person class
person = Person("Alice", 30)

# Accessing private attributes using getter methods
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30

# Modifying private attributes using setter methods
person.set_name("Bob")
person.set_age(35)

# Display updated information
print(person.get_name())  # Output: Bob
print(person.get_age())   # Output: 35