#Write a script that gets the current date and time and formats it as YYYY-MM-DD HH:MM:SS.
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format and print the date and time
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))