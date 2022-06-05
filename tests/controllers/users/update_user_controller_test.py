"""Testes para UpdateUserController"""
from unittest.mock import patch
from pytest import raises, mark
from mitmirror.errors import HttpNotFound, HttpBadRequestError, HttpUnprocessableEntity
from tests.mocks import mock_user


user = mock_user()


@mark.parametrize(
    "user_id, name, email, username, password",
    [
        (user.id, user.name, user.email, user.username, user.password_hash),
        (user.id, user.name, None, None, None),
        (user.id, None, user.email, None, None),
        (user.id, None, None, user.username, None),
        (user.id, None, None, None, user.password_hash),
    ],
)
def test_handler(
    user_id,
    name,
    email,
    username,
    password,
    update_user_controller,
    user_repository_spy,
):
    """Testando o metodo handler"""

    attributes = {
        "name": name,
        "email": email,
        "username": username,
        "password": password,
    }

    response = update_user_controller.handler(
        user_id=user_id, params=attributes)

    # Testando as entradas:
    assert user_repository_spy.update_user_params["name"] == attributes["name"]
    assert user_repository_spy.update_user_params["email"] == attributes["email"]
    assert user_repository_spy.update_user_params["username"] == attributes["username"]

    # Testando as saidas:
    assert response.status_code == 200
    assert "error" not in response.body


def test_handler_error_with_invalid_user_id(update_user_controller, fake_user):
    """
    Testando o error no metodo handler.
    Onde e passado um valor invalido para o parametro user_id.
    Deve retornar um erro HttpUnprocessableEntity.
    """

    with raises(HttpUnprocessableEntity) as error:

        update_user_controller.handler(user_id=fake_user.name, params={})

    # Testando as saidas:
    assert "error" in str(error.value)


def test_handler_error_without_user_id_param(update_user_controller):
    """
    Testando o erro no metodo handler.
    Onde nao e passado o parametro de user_id.
    Deve retornar um erro HttpBadRequestError.
    """

    with raises(HttpBadRequestError) as error:

        update_user_controller.handler(user_id=None, params={})

    # Testando as saidas:
    assert "error" in str(error.value)


def test_handler_error_not_found(update_user_controller, fake_user):
    """
    Testando o erro no metodo handler.
    Onde nao e passado o parametro de user_id.
    Deve retornar um erro HttpNotFound.
    """

    with raises(HttpNotFound) as error:

        attributes = {
            "name": fake_user.name,
            "email": fake_user.email,
            "username": fake_user.username,
            "password": fake_user.password_hash,
        }

        with patch(
            "tests.mocks.user_repository_spy.UserRepositorySpy.update_user",
            return_value=[],
        ):
            update_user_controller.handler(
                user_id=fake_user.id, params=attributes)

    # Testando as saidas:
    assert "error" in str(error.value)
