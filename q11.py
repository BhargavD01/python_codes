#11 Write a function that returns the length of a string without using the built-in len().
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

input_string = input("Enter a string: ")
length = string_length(input_string)
print("The length of the string is:", length)