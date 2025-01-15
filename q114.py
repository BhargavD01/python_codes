#Write a script that demonstrates the difference between a list comprehension and a generator expression for large data.
import sys

# Define a small range of numbers
numbers = range(1, 1001)  # 1 to 1,000

# List comprehension
list_comprehension = [x * 2 for x in numbers]
print("List comprehension created.")
print("Size of list comprehension in bytes:", sys.getsizeof(list_comprehension))

# Generator expression
generator_expression = (x * 2 for x in numbers)
print("Generator expression created.")
print("Size of generator expression in bytes:", sys.getsizeof(generator_expression))

# Demonstrating the use of generator expression
print("First 5 values from generator expression:")
for value in generator_expression:
    print(value)
    if value >= 10:  # Stop after printing a few values
        break