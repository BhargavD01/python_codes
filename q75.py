#Write a recursive function to compute the Greatest Common Divisor (GCD) of two numbers.
def gcd(a, b):
    if b == 0:  # Base case: if b is 0, GCD is a
        return a
    return gcd(b, a % b)  # Recursive case

print(gcd(48, 18))  # Output: 6
print(gcd(56, 98))  # Output: 14