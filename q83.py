#Write a program to search for a specific substring in a file and print the lines where it appears.
# Specify the file path and the substring to search for
file_path = 'example.txt'  # Replace with your file name
substring = 'search_term'   # Replace with the substring you want to search for

try:
    # Open the file and search for the substring
    with open(file_path, 'r') as file:
        for line in file:
            if substring in line:
                print(line.strip())  # Print the line if the substring is found

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")