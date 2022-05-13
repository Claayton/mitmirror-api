"""Testes para GetUsersController"""
from unittest.mock import patch
from pytest import raises
from mitmirror.errors import HttpNotFound
from tests.mocks import mock_user


user = mock_user()


def test_handler(get_users_controller):
    """Testando o metodo handler"""

    response = get_users_controller.handler(None)

    # Testando as saidas:
    assert response.status_code == 200
    assert "error" not in response.body


def test_handler_error_not_found(get_users_controller):
    """
    Testando o erro no metodo handler.
    Onde nenhum usuario e encontrado cadastrado.
    Deve retornar um erro HttpNotFound.
    """

    with raises(HttpNotFound) as error:

        with patch(
            "tests.mocks.user_repository_spy.UserRepositorySpy.get_users",
            return_value=[],
        ):
            get_users_controller.handler()

    assert "error" in str(error.value)
