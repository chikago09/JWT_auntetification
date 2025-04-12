import requests

url = "http://127.0.0.1:8000/api/product/"

data = {
    'category': 1,
    'name': 'Samsung Galaxy S24 Ultra',
    'price': 170000,
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print("Товар создан успешно!")
else:
    print("Не получилось создать товар!", response.status_code)