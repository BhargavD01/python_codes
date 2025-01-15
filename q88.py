#Define a class Car with a constructor that sets make, model, and year. Create an instance and display its details.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Display the car's details
print(f"Car Details: {my_car.year} {my_car.make} {my_car.model}")