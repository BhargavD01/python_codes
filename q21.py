#21 Find the minimum and maximum values in a list without using built-in min() or max().
numbers = [10, 20, 5, 40, 15]

# Initialize min and max with the first element
minimum = maximum = numbers[0]

# Iterate through the list
for num in numbers:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print("Minimum value:", minimum)
print("Maximum value:", maximum)