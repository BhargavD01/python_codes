#34 Using is_prime(), display all prime numbers between two integers start and end.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Get the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Print prime numbers in the range
print("Prime numbers between", start, "and", end, ":")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=' ')