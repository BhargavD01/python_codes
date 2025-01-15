#Implement the Euclidean algorithm to find the greatest common divisor of two numbers
def euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Update a and b
    return a

# Example usage
num1 = 48
num2 = 18
gcd = euclidean_gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is: {gcd}")