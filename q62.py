#Create a base class Animal and a derived class Dog. Override a method speak() in the Dog class to print "Woof!".
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Woof!"  # Override the speak method

dog = Dog()  # Create an instance of Dog
print(dog.speak())  # Call the overridden speak method