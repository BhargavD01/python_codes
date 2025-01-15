#Write a recursive function that takes a list which may contain nested lists and returns a flat list of all elements.
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):  # If the item is a list
            flat_list.extend(flatten(item))  # Recursively flatten it
        else:
            flat_list.append(item)  # Otherwise, add the item directly
    return flat_list

nested_list = [1, [2, 3], [4, [5, 6]], 7]
print(flatten(nested_list))  # Output: [1, 2, 3, 4, 5, 6, 7]