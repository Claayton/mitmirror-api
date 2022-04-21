"""Testes para as rotas de auth"""


def test_authentication(fake_user, client_auth_with_one_user_and_delete):
    """Testando a rota authentication"""

    url = "/api/auth/"
    headers = {"X-Test": "true"}
    data = {"email": fake_user.email, "password": fake_user.password}

    response = client_auth_with_one_user_and_delete.post(
        url=url, json=data, headers=headers
    )

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["message"] is not None
    assert isinstance(response.json()["data"], dict)
    assert "Authorization" in response.json()["data"]
    assert "exp" in response.json()["data"]
    assert "user" in response.json()["data"]
