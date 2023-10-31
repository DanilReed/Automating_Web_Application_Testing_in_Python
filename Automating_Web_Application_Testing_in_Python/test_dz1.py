from login import login, get_post
import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)

def test_step():
    token = login()
    post_data = {
        "title": data.get("title"),
        "description": data.get("description "),
        "content": data.get("content")
    }

    response = get_post(token, post_data)
    assert response.status_code == 200

    # Получение списка постов
    posts_response = requests.get(data.get("url_post"))
    posts = posts_response.json()
    post_found = any(post.get("description") == data.get("description") for post in posts)

    # Проверка наличия созданного поста на сервере по описанию
    assert post_found, "Созданный пост не найден по описанию"





