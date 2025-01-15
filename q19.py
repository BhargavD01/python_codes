#19 Prompt the user for 5 integers and store them in a list. Print the list and its length.
# Initialize an empty list
numbers = []

# Prompt the user for 5 integers
for _ in range(5):
    num = int(input("Enter an integer: "))
    numbers.append(num)

print("List of integers:", numbers)
print("Length of the list:", len(numbers))