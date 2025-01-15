#Write a recursive function that returns the number of vowels in a string.
def count_vowels(s):
    if not s:  # Base case: if the string is empty
        return 0
    
    # Check if the first character is a vowel
    if s[0].lower() in 'aeiou':
        return 1 + count_vowels(s[1:])  # Count this vowel and recurse
    else:
        return count_vowels(s[1:])  # Just recurse

print(count_vowels("Hello, World!"))  # Output: 3