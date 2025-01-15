#41 Given a list with duplicates, create a new list with unique elements only.
def unique_elements(input_list):
    # Use a set to store unique elements
    unique_set = set(input_list)
    # Convert the set back to a list
    return list(unique_set)

original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_list = unique_elements(original_list)

print("Original list:", original_list)
print("List with unique elements:", unique_list)