#Given a dictionary, invert it (keys become values, values become keys).
def invert_dictionary(original_dict):
    # Invert the dictionary using a dictionary comprehension
    inverted_dict = {value: key for key, value in original_dict.items()}
    return inverted_dict

# Example usage
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = invert_dictionary(original_dict)

print("Original dictionary:", original_dict)
print("Inverted dictionary:", inverted_dict)