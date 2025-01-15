#Prompt for n and create a dictionary where each key is from 1 to n and each value is the square of the key.
# Prompt the user for n
n = int(input("Enter a number (n): "))

# Create an empty dictionary
squares_dict = {}

# Fill the dictionary with keys and their squares
for x in range(1, n + 1):
    squares_dict[x] = x * x

# Print the resulting dictionary
print(squares_dict)