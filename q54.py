#Read a file and count how many lines it contains.
# Count the number of lines in a file
file_path = 'example.txt'  # Replace with your file path

# Open the file and count the lines
with open(file_path, 'r') as file:
    line_count = sum(1 for line in file)  # Count lines using a generator expression

print(f"The file '{file_path}' contains {line_count} lines.")