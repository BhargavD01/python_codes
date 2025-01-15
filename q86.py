#Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the Person class
person = Person("Alice", 30)

# Print the attributes
print(person.name)
print(person.age)