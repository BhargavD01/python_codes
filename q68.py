#Write a recursive function power(base, exp) that computes base^exp.
def power(base, exp):
    if exp == 0:  # Base case: any number to the power of 0 is 1
        return 1
    return base * power(base, exp - 1)  # Recursive case

print(power(2, 3))  # Output: 8