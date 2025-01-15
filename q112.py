#Use a lambda function inside map to transform a list of numbers (e.g., multiply each by 2).
# Sample list of numbers
numbers = [1, 2, 3, 4, 5]

# Multiply each number by 2 using map and a lambda function
doubled_numbers = list(map(lambda x: x * 2, numbers))

# Print the result
print(doubled_numbers)