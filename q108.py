#Write a program (assuming you have internet access) that fetches data from a public API using the requests module and prints part of the JSON response.
import requests

# Fetch and print data from the API
data = requests.get("http://api.open-notify.org/astros.json").json()

print("Number of people currently in space:", data['number'])
for person in data['people']:
    print(person['name'])