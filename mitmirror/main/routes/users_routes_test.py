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
