#27 Prompt for a string and replace all occurrences of a specific character with another.
# Prompt for a string
s = input("Enter a string: ")

# Prompt for the character to replace and the new character
old_char = input("Character to replace: ")
new_char = input("New character: ")

# Replace the character
s = s.replace(old_char, new_char)

# Print the result
print("Updated string:", s)