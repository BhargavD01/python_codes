#40 Write an iterative binary search function to find an element in a sorted list.
# didnt understand
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
            
    return -1  # Target not found

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

result = binary_search(sorted_list, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")