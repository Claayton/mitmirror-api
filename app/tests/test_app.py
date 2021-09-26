from pytest import mark

def test_if_the_root_route_is_working(client):
    url = "/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IlRlc3RzIiwiZXhwIjoxNjMyNjgyNjQ2fQ.PTyLYv5UM3FVaE62fSIp03thPZflzk19eeNel0UKOqA"
    response = client.get(url)
    assert response.status_code == 200

def test_if_the_auth_route_is_working(client):
    url ="/api/auth/"
    data = {
        "username": "Testsficticio",
        "password": "Testsficticio"
    }
    response = client.post(url, json=data)
    assert response.status_code == 403

def test_if_the_get_user_route_is_working(client):
    url = "/api/users/"
    response =client.get(url)
    assert response.json["data"]["6"]["name"] == 'Tests'

def test_if_the_get_users_route_is_working(client):
    url = "/api/users/1/"
    response = client.get(url)
    assert response.status_code == 200

def test_if_the_post_users_route_is_working(client):
    url ="/api/users/"
    data = {
        "name": "Tests",
        "email": "tests@tests.com",
        "username": "Tests",
        "password": "tests"
    }
    response = client.post(url, json=data)
    assert response.status_code == 403

def test_if_the_put_users_route_is_working(client):
    url ="/api/users/6"
    data = {
        "name": "Tests",
        "email": "tests@tests.com",
        "username": "Tests",
        "password": "tests"
    }
    response = client.put(url, json=data)
    assert response.status_code == 201

def test_if_the_delete_users_route_is_working(client):
    url ="/api/users/666"
    response = client.delete(url)
    assert response.status_code == 403
