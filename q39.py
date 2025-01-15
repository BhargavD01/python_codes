#39 Implement the bubble sort algorithm to sort a list of numbers in ascending order.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the current element is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", numbers)

bubble_sort(numbers)
print("Sorted list:", numbers)