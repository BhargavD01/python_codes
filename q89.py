#Modify the Car class to have default values for make and model if not provided.
class Car:
    def __init__(self, make="Unknown Make", model="Unknown Model", year=2020):
        self.make = make
        self.model = model
        self.year = year

# Create instances of the Car class
car1 = Car("Toyota", "Camry", 2020)  # All values provided
car2 = Car(year=2021)                 # Only year provided

# Display the car's details
print(f"Car 1: {car1.year} {car1.make} {car1.model}")
print(f"Car 2: {car2.year} {car2.make} {car2.model}")