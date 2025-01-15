#Write a program that prompts the user for a line of text and writes that line to a file.
# Get user input
text = input("Enter a line of text: ")

# Write the input to a file
with open('output.txt', 'w') as file:
    file.write(text)

print("Text has been written to 'output.txt'.")