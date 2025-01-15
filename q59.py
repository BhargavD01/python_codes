#Write a script that takes command-line arguments (e.g., file paths) and prints them.
import sys

# Get the command-line arguments
file_paths = sys.argv[1:]  # Exclude the first argument (script name)

# Print the file paths
for path in file_paths:
    print(path)