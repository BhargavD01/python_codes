#Write a script that reads a JSON file, modifies a value, and writes the updated data back to the file.
import json

# Read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Modify a value
data['example_key'] = 'new_value'  # Change 'example_key' to the new value

# Write the updated data back to the JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("JSON file updated successfully.")