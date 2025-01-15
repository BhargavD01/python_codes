#Copy the contents of one text file to another.
# Copy contents from one file to another
source_file = 'source.txt'  # Replace with your source file path
destination_file = 'destination.txt'  # Replace with your destination file path

# Open the source file and read its contents
with open(source_file, 'r') as src:
    contents = src.read()

# Open the destination file and write the contents
with open(destination_file, 'w') as dest:
    dest.write(contents)

print(f"Contents copied from '{source_file}' to '{destination_file}'.")