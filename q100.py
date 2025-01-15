#Demonstrate multiple inheritance with two parent classes providing different functionalities to a child class.
class Flyer:
    def fly(self):
        return "I can fly!"

class Swimmer:
    def swim(self):
        return "I can swim!"

class Duck(Flyer, Swimmer):
    pass

# Create an instance of Duck
duck = Duck()

# Use methods from both parent classes
print(duck.fly())   # Output: I can fly!
print(duck.swim())  # Output: I can swim!