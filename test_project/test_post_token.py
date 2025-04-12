import requests

url = 'http://127.0.0.1:8000/api/token/'

data = {
    'username': 'chika',
    'password': 'zxcvbnm123',
}

response = requests.post(url, json=data)
print(response.json())