#Create a class Person with attributes name and age. Include a method greet() that prints "Hello, my name is <name>."
class Person:
    def __init__(self, name, age):
        self.name = name  # Initialize the name attribute
        self.age = age    # Initialize the age attribute

    def greet(self):
        print(f"Hello, my name is {self.name}.")  # Greet method

if __name__ == "__main__":
    person1 = Person("Alice", 30)  # Create an instance of Person
    person1.greet()  # Call the greet method