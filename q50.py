#Using the GCD function, write a function lcm(a, b) that returns the least common multiple.
def euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // euclidean_gcd(a, b)

# Example usage
num1 = 48
num2 = 18
least_common_multiple = lcm(num1, num2)

print(f"The LCM of {num1} and {num2} is: {least_common_multiple}")