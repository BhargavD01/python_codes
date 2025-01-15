#Write a script that extracts all email addresses from a given string using the re module.
import re

# Sample string containing email addresses
text = "Contact us at example1@test.com or example2@test.org."

# Extract email addresses using a regular expression
emails = re.findall(r'\S+@\S+', text)

# Print the extracted email addresses
print("Extracted email addresses:", emails)