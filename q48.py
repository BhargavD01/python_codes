#Implement a function recursive_sum(lst) that sums all elements in a list using recursion.
def recursive_sum(lst):
    # Base case: if the list is empty, return 0
    if len(lst) == 0:
        return 0
    # Recursive case: add the first element to the sum of the rest
    return lst[0] + recursive_sum(lst[1:])

# Example usage
numbers = [1, 2, 3, 4, 5]
result = recursive_sum(numbers)

print("The sum of the list is:", result)