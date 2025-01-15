#Write a Python program that reads a file and counts the number of words in it.
# Specify the file path
file_path = 'example.txt'  # Replace with your file name

# Open the file and count the words
with open(file_path, 'r') as file:
    text = file.read()  # Read the entire file content
    word_count = len(text.split())  # Split the text into words and count them

print(f"The number of words in '{file_path}' is: {word_count}")