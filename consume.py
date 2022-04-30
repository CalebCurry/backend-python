import requests

response = requests.get('http://localhost:8000/api/files/14')

print(response.json())