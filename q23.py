#23 Given a list of integers, prompt for a specific integer and count how many times it appears.
numbers = [1, 2, 3, 4, 2, 5, 2, 6, 3]

target = int(input("Enter an integer to count its occurrences: "))

# Count occurrences using a simple loop
count = 0
for num in numbers:
    if num == target:
        count += 1