#5 Write a program that swaps the values of two variables without using a temporary variable.
a = input("Enter the first value: ")
b = input("Enter the second value: ")

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)