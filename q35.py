#35 Check if a number is a palindrome (e.g., 121 → palindrome).
# Function to check if a number is a palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Get a number from the user
number = int(input("Enter a number: "))

# Check and print if the number is a palindrome
if is_palindrome(number):
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")