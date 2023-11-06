import requests
import yaml
import pytest

with open("config.yaml") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():

    response = requests.post(url=data.get('url_login'),
                         data={"username": data.get('username'), "password": data.get('password')})
    if response.status_code == 200:
        return response.json()['token']
