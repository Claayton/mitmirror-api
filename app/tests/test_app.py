def test_if_the_root_route_is_working(client):
    url = "/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IlRlc3RzIiwiZXhwIjoxNjMzMjM0MDU1fQ.62H8YHAIJwlT08KSN7E26fJCtlFJqLNg5v_n4BAQSpU"
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
    url = "/api/users/5/"
    response = client.get(url)
    assert response.status_code == 200

def test_if_the_get_users_route_is_working(client):
    url = "/api/users/"
    response =client.get(url)
    assert response.json["data"]["5"]["name"] == 'Tests'

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
    url ="/api/users/5"
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
