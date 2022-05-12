"""Testes para RegisterUsersController"""
from pytest import raises, mark
from mitmirror.errors import HttpBadRequestError
from mitmirror.infra.tests import mock_user
from mitmirror.presenters.helpers.http_models import HttpRequest


user = mock_user()


def test_handler(register_user_with_spy, user_repository_spy, fake_user):
    """Testando o metodo handler"""

    attributes = {
        "name": fake_user.name,
        "email": fake_user.email,
        "username": fake_user.username,
        "password": fake_user.password_hash,
    }

    response = register_user_with_spy.handler(http_request=HttpRequest(body=attributes))

    # Testando as entradas:
    assert user_repository_spy.insert_user_params["name"] == attributes["name"]
    assert user_repository_spy.insert_user_params["email"] == attributes["email"]
    assert user_repository_spy.insert_user_params["username"] == attributes["username"]
    assert user_repository_spy.insert_user_params["password_hash"] is not None

    # Testando as saidas:
    assert response.status_code == 201
    assert "error" not in response.body


def test_handler_error_without_body_params(register_user_with_spy):
    """
    Testando o erro no metodo handler.
    Sem utilizar body params.
    Deve retornar um erro HttpBadRequestError.
    """

    with raises(HttpBadRequestError) as error:

        register_user_with_spy.handler(http_request=HttpRequest())

    assert "error" in str(error.value)


@mark.parametrize(
    "name, email, username, password",
    [
        (None, user.email, user.username, user.password_hash),
        (user.name, None, user.username, user.password_hash),
        (user.name, user.email, None, user.password_hash),
        (user.name, user.email, user.username, None),
    ],
)
def test_handler_error_missing_some_of_the_body_params(
    name, email, username, password, register_user_with_spy
):
    """
    Testando o erro no metodo handler.
    Faltando algum dos parametros.
    Deve retornar um erro HttpBadRequestError.
    """

    attributes = {
        "name": name,
        "email": email,
        "username": username,
        "password": password,
    }

    with raises(HttpBadRequestError) as error:

        register_user_with_spy.handler(http_request=HttpRequest(body=attributes))

    assert "error" in str(error.value)
