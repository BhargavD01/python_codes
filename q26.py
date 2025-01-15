#26 Prompt for a string s and a substring sub. Check if sub is present in s.
# Prompt for a string and a substring
s = input("Enter a string: ")
sub = input("Enter a substring: ")

# Check if the substring is in the string
if sub in s:
    print("Yes, the substring is present.")
else:
    print("No, the substring is not present.")