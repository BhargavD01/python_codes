#Add a method greet to the Person class that prints "Hello, my name is <name>".
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Create an instance of the Person class
person = Person("Alice", 30)

# Call the greet method
person.greet()