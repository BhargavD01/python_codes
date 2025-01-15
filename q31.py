#31 Calculate the factorial of a number using a for loop.
# Prompt for a number
n = int(input("Enter a number: "))

# Initialize factorial
factorial = 1

# Calculate factorial
for i in range(1, n + 1):
    factorial *= i

# Print the result
print("Factorial:", factorial)