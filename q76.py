#Write a Python script that reads a text file and prints its contents.
# Specify the file path
file_path = 'example.txt'  # Replace with your file path

# Open the file and print its contents
with open(file_path, 'r') as file:
    print(file.read())