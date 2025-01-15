#Create a base class Animal and a derived class Dog. The Dog class should inherit attributes and methods from Animal.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Create an instance of the Dog class
my_dog = Dog("Buddy")

# Display the dog's name and sound
print(f"{my_dog.name} says: {my_dog.speak()}")