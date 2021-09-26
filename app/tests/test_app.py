from pytest import mark

def test_if_the_root_route_is_working(client):
    assert client.get("/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IlRlc3RzIiwiZXhwIjoxNjMyNjgyNjQ2fQ.PTyLYv5UM3FVaE62fSIp03thPZflzk19eeNel0UKOqA").status_code == 200

def test_if_the_auth_route_is_working(client):
    assert client.post("/api/auth/").status_code == 401

def test_if_the_get_user_route_is_working(client):
    # response = client.get('/api/users/')
    # print(f'\033[34m{response.data}\033[m')
    assert client.get("/api/users/").status_code == 200

def test_if_the_get_users_route_is_working(client):
    assert client.get("/api/users/1/").status_code == 200

# def test_if_the_get_users_route_is_working(client):
#     assert client.post("/api/users/").status_code == 500
