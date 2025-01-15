#42 Find the second largest element in a list of unique integers.
def second_largest(numbers):
    # Sort the list in descending order
    sorted_numbers = sorted(numbers, reverse=True)
    # Return the second element
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None

unique_numbers = [10, 20, 4, 45, 99]
result = second_largest(unique_numbers)

if result is not None:
    print("The second largest element is:", result)
else:
    print("The list does not have enough elements.")