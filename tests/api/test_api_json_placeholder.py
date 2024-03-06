import pytest
import requests
from faker import Faker
import allure

fake = Faker()


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com/"


# Тест на проверку статуса кода при GET запросе к /posts
@allure.feature('API Testing')
@allure.title('Verify status code for GET request to /posts endpoint')
def test_get_posts_status_code(base_url):
    response = requests.get(base_url + "posts")
    assert response.status_code == 200


# Тест на проверку количества постов в GET запросе к /posts
@allure.feature('API Testing')
@allure.title('Verify number of posts in GET request to /posts endpoint')
def test_get_posts_count(base_url):
    response = requests.get(base_url + "posts")
    posts = response.json()
    assert len(posts) == 100


# Тест на создание нового пользователя с помощью POST запроса к /users
@allure.feature('API Testing')
@allure.title('Verify creation of a new user using POST request to /users endpoint')
def test_create_new_user(base_url):
    data = {
        "name": fake.name(),
        "username": fake.user_name(),
        "email": fake.email()
    }
    response = requests.post(base_url + "users", json=data)
    assert response.status_code == 201


# Тест на получение информации о пользователе по его id
@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
@allure.feature('API Testing')
@allure.title('Verify retrieval of user information by ID')
def test_get_user_by_id(base_url, user_id):
    response = requests.get(base_url + f"users/{user_id}")
    assert response.status_code == 200


# Тест на получение информации о случайном пользователе
@allure.feature('API Testing')
@allure.title('Verify retrieval of information about a random user')
def test_get_random_user(base_url):
    random_user_id = fake.random_int(min=1, max=10)
    response = requests.get(base_url + f"users/{random_user_id}")
    assert response.status_code == 200


# Тест на удаление поста с помощью DELETE запроса
@allure.feature('API Testing')
@allure.title('Verify deletion of a post using DELETE request')
def test_delete_post(base_url):
    response = requests.delete(base_url + "posts/1")
    assert response.status_code == 200


# Тест на обновление информации о пользователе с помощью PUT запроса
@allure.feature('API Testing')
@allure.title('Verify update of user information using PUT request')
def test_update_user(base_url):
    data = {
        "name": fake.name(),
        "username": fake.user_name(),
        "email": fake.email()
    }
    response = requests.put(base_url + "users/1", json=data)
    assert response.status_code == 200


# Тест на создание нового поста с помощью POST запроса
@allure.feature('API Testing')
@allure.title('Verify creation of a new post using POST request')
def test_create_new_post(base_url):
    data = {
        "userId": fake.random_int(min=1, max=10),
        "title": fake.sentence(),
        "body": fake.paragraph()
    }
    response = requests.post(base_url + "posts", json=data)
    assert response.status_code == 201


# Тест на получение комментариев к посту по его id
@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
@allure.feature('API Testing')
@allure.title('Verify retrieval of comments by post ID')
def test_get_comments_for_post(base_url, post_id):
    response = requests.get(base_url + f"posts/{post_id}/comments")
    assert response.status_code == 200


# Тест на получение списка дел (todos) для случайного пользователя
@allure.feature('API Testing')
@allure.title('Verify retrieval of todos for a random user')
def test_get_todos_for_random_user(base_url):
    random_user_id = fake.random_int(min=1, max=10)
    response = requests.get(base_url + f"users/{random_user_id}/todos")
    assert response.status_code == 200


# Тест на попытку создания нового пользователя с недопустимыми данными
@allure.feature('API Testing')
@allure.title('Verify creation of a new user with invalid data using POST request to /users endpoint')
def test_invalid_data_user(base_url):
    data = {
        "name": "John Doe",
        "username": "johndoe123",
        "email": "invalid_email"
    }
    response = requests.post(base_url + "users", json=data)
    assert response.status_code != 200


# Тест на попытку получения информации о несуществующем пользователе
@allure.feature('API Testing')
@allure.title('Verify retrieval of user information for a non-existent user ID')
@pytest.mark.parametrize("user_id", [1000, 2000, 3000])
def test_non_exist_user(base_url, user_id):
    response = requests.get(base_url + f"users/{user_id}")
    assert response.status_code == 404
