#Implement a function factorial(n) that calculates n! using recursion.
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

# Example usage
number = 5  # You can change this number to test with other values
print(f"The factorial of {number} is {factorial(number)}.")