"""Testes para as rotas de users"""


def test_get_users(client_with_one_user):
    """Testando a rota get_users"""

    url = "/api/users/"

    response = client_with_one_user.get(url=url)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "id" in response.json()["data"][0]
    assert "name" in response.json()["data"][0]


def test_get_user(client_with_one_user, fake_user):
    """Testando a rota get_user"""

    url = f"/api/users/{fake_user.id}"

    response = client_with_one_user.get(url=url)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], dict)
    assert "id" in response.json()["data"]
    assert "name" in response.json()["data"]


def test_register_user(client_with_delete_user, fake_user):
    """Testando a rota register_user"""

    url = "/api/users/"
    json = {
        "name": fake_user.name,
        "email": fake_user.email,
        "username": fake_user.username,
        "password": fake_user.password_hash,
    }

    response = client_with_delete_user.post(url=url, json=json)

    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], dict)
    assert "id" in response.json()["data"]
    assert "name" in response.json()["data"]
