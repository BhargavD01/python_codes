#Write a script that reads a CSV file and prints each row. (Assume the file exists and is properly formatted.)
import csv

# Read and print each row of a CSV file
with open('example.csv', 'r') as csvfile:  # Replace with your CSV file path
    reader = csv.reader(csvfile)  # Create a CSV reader object
    for row in reader:  # Iterate through each row in the CSV
        print(row)  # Print the current row