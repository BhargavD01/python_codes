#16 Compute  without using built-in functions (like pow).
# Function to compute base raised to the power of exponent
# didnt understand fully
def compute_power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    return result if exponent >= 0 else 1 / result