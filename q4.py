#4 Prompt the user for two numbers and display their sum, difference, product, and quotient.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)")