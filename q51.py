#Write a program that reads a text file and prints its contents to the screen.
def read_file(file_path):
    with open(file_path, 'r') as file:  # Open the file in read mode
        print(file.read())  # Read and print the entire file content

# Example usage
file_path = 'example.txt'  # Replace with your file path
read_file(file_path)