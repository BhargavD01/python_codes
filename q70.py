#Implement binary search recursively to find an element in a sorted list.
#doubt
def binary_search(arr, target):
    def search(low, high):
        if low > high:  # Base case: target not found
            return -1

        mid = (low + high) // 2  # Find the middle index

        if arr[mid] == target:  # Target found
            return mid
        elif arr[mid] < target:  # Search in the right half
            return search(mid + 1, high)
        else:  # Search in the left half
            return search(low, mid - 1)

    return search(0, len(arr) - 1)  # Start the search

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(sorted_list, target)

if result != -1:
    print(f"Element {target} found at index: {result}")
else:
    print(f"Element {target} not found in the list.")