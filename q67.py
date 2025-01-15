#Implement a function fib(n) to return the nth Fibonacci number using recursion.
def fib(n):
    if n <= 0:
        return 0  # Fibonacci of 0
    elif n == 1:
        return 1  # Fibonacci of 1
    return fib(n - 1) + fib(n - 2)  # Recursive case

# Example usage
print(fib(5))  # Change the number to test with other values