#Write a script that uses the math module to compute the square root, floor, and ceiling of a user-input number.
import math

# Get user input
number = float(input("Enter a number: "))

# Calculate square root, floor, and ceiling
square_root = math.sqrt(number)
floor_value = math.floor(number)
ceiling_value = math.ceil(number)

# Print the results
print("Square root:", square_root)
print("Floor:", floor_value)
print("Ceiling:", ceiling_value)