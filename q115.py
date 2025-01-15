#Write a simple decorator timer that measures the execution time of a function.
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # End time
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result  # Return the result
    return wrapper

# Example usage
@timer_decorator
def example_function(n):
    total = sum(range(n))  # Sum numbers from 0 to n-1
    return total

# Call the decorated function
result = example_function(1000000)
print("Result:", result)