#Write a recursive function that computes the sum of all elements in a list.
def sum_list(lst):
    if not lst:  # Base case: if the list is empty
        return 0
    return lst[0] + sum_list(lst[1:])  # Add the first element to the sum of the rest

print(sum_list([1, 2, 3, 4, 5]))  # Output: 15