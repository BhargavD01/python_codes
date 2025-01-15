#Read data from a JSON file, modify a value, and write the updated data back to the file.
import json

# Read the JSON data from the file
with open('data.json', 'r') as file:
    data = json.load(file)  # Load the JSON data

# Modify the value (e.g., change age to 31)
data['age'] = 31  # Update the age

# Write the updated data back to the file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)  # Write the updated data

print("Updated 'age' to 31 in 'data.json'.")