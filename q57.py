#Search for a specific word in a file and replace it with another word, then overwrite the file with the changes.
# Replace a specific word in a file
file_path = 'example.txt'  # Replace with your file path
old_word = 'old'           # Word to be replaced
new_word = 'new'           # Word to replace with

# Read the file, replace the word, and write back to the file
with open(file_path, 'r') as file:
    contents = file.read().replace(old_word, new_word)  # Read and replace in one step

with open(file_path, 'w') as file:
    file.write(contents)  # Overwrite the file with updated contents

print(f"Replaced '{old_word}' with '{new_word}' in '{file_path}'.")