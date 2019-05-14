import requests

url = "https:///:account.api-us1.com/api/3/contactAutomations"

response = requests.get('https://api.github.com/events')

print(response.text)