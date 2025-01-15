#Write a program that appends a user-input line to an existing file without overwriting it.
# Specify the file path
file_path = 'example.txt'  # Replace with your file name

# Get user input and append it to the file
with open(file_path, 'a') as file:  # Open the file in append mode
    file.write(input("Enter a line to append: ") + '\n')  # Write the input followed by a newline

print(f"Line appended to '{file_path}'.")