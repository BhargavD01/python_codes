#Write a recursive function that checks if a string is a palindrome.
def is_palindrome(s):
    # Base case: if the string is empty or has one character, it's a palindrome
    if len(s) <= 1:
        return True
    
    # Check the first and last characters
    if s[0] != s[-1]:  # Direct comparison
        return False
    
    # Recur on the substring that excludes the first and last characters
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
print(is_palindrome("A man a plan a canal Panama".replace(" ", "").lower()))  # Output: True