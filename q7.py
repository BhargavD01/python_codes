#7 Prompt the user for three numbers and determine which one is the largest.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = max(num1, num2, num3)

print("The largest number is:", largest)