#Write a function that attempts to convert a string to an integer, catching any ValueError and printing a custom message
def convert_to_integer(input_string):
    try:
        print(int(input_string))  # Attempt to convert and print the integer
    except ValueError:
        print("Error: Cannot convert to an integer.")

# Example usage
input_string = input("Enter a string to convert to an integer: ")
convert_to_integer(input_string)