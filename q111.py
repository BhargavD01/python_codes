#Demonstrate advanced list slicing (e.g., reversing a list with slicing, skipping elements) in a script.
# Sample list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Reversing the list
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)

# Getting every second element
every_second = numbers[::2]
print("Every second element:", every_second)

# Getting a sublist from index 2 to 5
sublist = numbers[2:5]
print("Sublist from index 2 to 5:", sublist)