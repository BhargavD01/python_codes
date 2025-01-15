#Write a Python program to copy the contents of one file to another.
# Copy contents from one file to another
with open('source.txt', 'r') as src, open('destination.txt', 'w') as dest:
    dest.write(src.read())

print("Contents copied from 'source.txt' to 'destination.txt'.")