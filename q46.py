#Count how often each element appears in a list and store the result in a dictionary.
from collections import Counter

# Example list
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Count the occurrences of each element
count_dict = Counter(elements)

# Print the result
print("Element counts:", count_dict)