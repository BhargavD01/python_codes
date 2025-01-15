#18 Format a string using f-strings (or format()) to display user info (e.g., name, age).
name = input("Enter your name: ")
age = int(input("Enter your age: "))

user_info = f"Hello, my name is {name} and I am {age} years old."
print(user_info)