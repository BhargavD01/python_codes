#Use filter to filter out even numbers from a list, then use functools.reduce to sum the filtered numbers.
from functools import reduce

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter out even numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Sum the filtered numbers
sum_of_odds = reduce(lambda x, y: x + y, odd_numbers)

# Print the result
print("Sum of odd numbers:", sum_of_odds)