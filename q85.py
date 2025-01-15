#Write a Python script to read a CSV file and print each row.
import csv

# Specify the file path
file_path = 'example.csv'  # Replace with your CSV file name

# Open the CSV file and read its contents
with open(file_path, 'r') as file:
    for row in csv.reader(file):  # Read and iterate through each row
        print(row)  # Print the current row