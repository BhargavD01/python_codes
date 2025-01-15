#28 Prompt the user for a number (as a string) and compute the sum of its digits.
# Prompt the user for a number as a string
number_str = input("Enter a number: ")

# Compute the sum of its digits
digit_sum = sum(int(digit) for digit in number_str)

# Print the result
print("Sum of the digits:", digit_sum)