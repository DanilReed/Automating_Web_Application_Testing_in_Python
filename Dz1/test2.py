import requests

response = requests.post(url="https://test-stand.gb.ru/gateway/login",
                         data={"username": "Patty Barrows", "password": "625cdcbddc"})
print(response.status_code)
print(response.json()['token'])
