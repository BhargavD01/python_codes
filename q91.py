#In the Dog class, override a method speak defined in Animal (e.g., Animal says “Some sound”, but Dog says “Woof!”).
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):  # Overriding the speak method
        return "Woof!"

# Create an instance of the Dog class
my_dog = Dog()

# Display the sound the dog makes
print(f"The dog says: {my_dog.speak()}")