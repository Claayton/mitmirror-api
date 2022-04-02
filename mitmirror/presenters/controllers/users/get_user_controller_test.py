"""Testes para GetUserController"""
from mitmirror.infra.tests import mock_user
from mitmirror.presenters.helpers import HttpRequest


user = mock_user()


def test_handler_with_query_params_user_id(
    get_user_controller, user_repository, fake_user
):
    """Testando o metodo handler, buscando pelo id do usuario"""

    attributes = {"user_id": fake_user.id}

    response = get_user_controller.handler(HttpRequest(query=attributes))

    # Testando as entradas:
    assert user_repository.get_user_params["user_id"] == attributes["user_id"]

    # Testando as saidas:
    assert response.status_code == 200
    assert "error" not in response.body


def test_handler_with_query_param_email(
    get_user_controller, user_repository, fake_user
):
    """Testando o metodo handler, buscando pelo email do usuario"""

    attributes = {"email": fake_user.email}

    response = get_user_controller.handler(HttpRequest(query=attributes))

    # Testando as entradas:
    assert user_repository.get_user_params["email"] == attributes["email"]

    # Testando as saidas:
    assert response.status_code == 200
    assert "error" not in response.body


def test_handler_with_query_param_username(
    get_user_controller, user_repository, fake_user
):
    """Testando o metodo handler, buscando pelo email do email"""

    attributes = {"username": fake_user.username}

    response = get_user_controller.handler(HttpRequest(query=attributes))

    # Testando as entradas:
    assert user_repository.get_user_params["username"] == attributes["username"]

    # Testando as saidas:
    assert response.status_code == 200
    assert "error" not in response.body
