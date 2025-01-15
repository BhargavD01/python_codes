#32 Print the first n Fibonacci numbers using iteration.
# Prompt for the number of Fibonacci numbers
n = int(input("Enter the number of Fibonacci numbers to print: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Print the Fibonacci numbers
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b