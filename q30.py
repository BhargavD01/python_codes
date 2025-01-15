#30 Prompt the user for a password and print a masked version (e.g., ****** for 6 characters).
# Prompt the user for a password
password = input("Enter your password: ")

# Create a masked version
masked_password = '*' * len(password)

# Print the masked version
print("Masked password:", masked_password)