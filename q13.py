#13 Demonstrate various string slicing operations (e.g., reverse a string, skip letters).
# Sample string
sample_string = "Hello, World!"

# 1. Reverse a string
reversed_string = sample_string[::-1]
print("Reversed string:", reversed_string)

# 2. Skip letters (every second letter)
skipped_string = sample_string[::2]
print("Every second letter:", skipped_string)

# 3. Get a substring (first 5 characters)
substring = sample_string[:5]
print("First 5 characters:", substring)

# 4. Get the last 6 characters
last_six = sample_string[-6:]
print("Last 6 characters:", last_six)

# 5. Get every third character
every_third = sample_string[::3]
print("Every third character:", every_third)