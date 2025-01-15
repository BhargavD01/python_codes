#Prompt the user for a string and write it to a new text file.
# Prompt the user for a string
user_input = input("Please enter a string to write to the file: ")

# Write the user input to a new text file
with open('output.txt', 'w') as file:  # Open the file in write mode
    file.write(user_input)  # Write the input to the file

print("The string has been written to 'output.txt'.")