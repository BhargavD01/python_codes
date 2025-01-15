#Use the statistics module to compute the mean, median, and mode of a list of numbers.
import statistics

# List of numbers
numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6]

# Calculate and print mean, median, and mode
print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
print("Mode:", statistics.mode(numbers))