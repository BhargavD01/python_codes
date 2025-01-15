#Modify the file-reading program to handle exceptions (e.g., file not found) gracefully.
# Specify the file path
file_path = 'example.txt'  # Replace with your file name

try:
    # Open the file and count the lines
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)

    print(f"Number of lines in '{file_path}': {line_count}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")