#Write a program that finds the longest word in a text file and prints it.
# Specify the file path
file_path = 'example.txt'  # Replace with your file name

try:
    # Open the file and read its contents
    with open(file_path, 'r') as file:
        text = file.read()  # Read the entire file content
        words = text.split()  # Split the text into words
        longest_word = max(words, key=len)  # Find the longest word

    print(f"The longest word in '{file_path}' is: '{longest_word}'")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")