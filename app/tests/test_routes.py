def test_if_the_index_route_is_working(client):
    url = "/"
    response = client.get(url)
    assert response.status_code == 200

def test_if_the_root_route_is_working(client):
    url = "/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzYyNzcwNjAsImlhdCI6MTYzNjI2MjY2MCwic3ViIjoxLCJuYW1lIjoiVGVzdCJ9.ZdqQyLHX0MyhPyYkWJdnWAr7dSWtX7UlHESNeK4IFow"
    response = client.get(url)
    assert response.status_code == 200

def test_if_the_auth_route_is_working(client):
    url ="/api/auth/"
    data = {
        "email": "test@test.com",
        "password": "test123"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200

def test_if_the_get_user_route_is_working(client):
    url = "/api/users/1/"
    response = client.get(url)
    print(response.data)
    assert response.status_code == 401

def test_if_the_get_users_route_is_working(client):
    url = "/api/users/"
    response =client.get(url)
    assert response.json["data"]["1"]["name"] == 'Test'

def test_if_the_post_users_route_is_working(client):
    url ="/api/users/"
    data = {
        "name": "Test",
        "email": "test@test.com",
        "username": "test123",
        "password": "test123"
    }
    response = client.post(url, json=data)
    assert response.status_code == 403

def test_if_the_put_users_route_is_working(client):
    url ="/api/users/1/"
    data = {
        "name": "Test",
        "email": "test@test.com",
        "username": "test123",
        "password": "test123"
    }
    response = client.put(url, json=data)
    assert response.status_code == 401

def test_if_the_delete_users_route_is_working(client):
    url = "/api/users/666/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QxMjMiLCJleHAiOjE2MzM1NDA3Mjl9.laQk29KJqGv1ojVEK5-Tgig0xCWfVCoQBNaS10cJI1Y"
    response = client.delete(url)
    assert response.status_code == 401
