#22 Reverse a list in-place (without using reversed() or slicing).
numbers = [1, 2, 3, 4, 5]

# Reverse the list in-place
for i in range(len(numbers) // 2):
    # Swap the elements
    numbers[i], numbers[len(numbers) - 1 - i] = numbers[len(numbers) - 1 - i], numbers[i]

# Print the reversed list
print("Reversed list:", numbers)