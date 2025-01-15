#Write a program that counts how many lines are in a file.
# Specify the file path
file_path = 'example.txt'  # Replace with your file name

# Open the file and count the lines
with open(file_path, 'r') as file:
    line_count = sum(1 for line in file)  # Count lines using a generator expression

print(f"The number of lines in '{file_path}' is: {line_count}")