import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)

def login():

    response = requests.post(url=data.get('url_login'),
                         data={"username": data.get('username'), "password": data.get('password')})
    if response.status_code == 200:
        return response.json()['token']

# def get_post(token):
#     print(token)
#     response = requests.post(url=data.get('url_post'),
#                              headers= {"X-Auth-Token":token},
#                              params={"owner": "notMe"})
#     print(response.json())
#     return response.json()

import requests
import yaml


def login():
    with open("config.yaml") as f:
        data = yaml.safe_load(f)

    response = requests.post(url=data.get('url_login'),
                             data={"username": data.get('username'), "password": data.get('password')})
    if response.status_code == 200:
        return response.json()['token']


def get_post(token, post_data):
    with open("config.yaml") as f:
        data = yaml.safe_load(f)

    headers = {"X-Auth-Token": token}
    url = data.get('url_post')

    response = requests.post(url, headers=headers, data=post_data)
    return response


if __name__ == '__main__':
    get_post(login())