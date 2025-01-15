#12 Write a program that checks if a given string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]  # Check if the string is equal to its reverse

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("Palindrome")
else:
    print("Not a palindrome")