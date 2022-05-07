"""Testes para a classe GetUsers"""  # pylint: disable=E0401
from typing import List
from unittest.mock import patch
from pytest import raises
from mitmirror.errors import DefaultError


def test_all_users(get_users):
    """
    Testando o metodo all_users.
    Deve retornar uma mensagem de sucesso, e uma lista de usuarios.
    """

    response = get_users.all_users()

    # Testando a saida:
    assert response["success"] is True
    assert isinstance(response["data"], List)


def test_all_users_with_on_result_found(get_users):
    """
    Testando o erro no metodo all_users.
    Onde nao e encontrado nenhum usuariono banco de dados.
    Deve retornar um DefaultError.
    """

    with raises(DefaultError) as error:

        with patch(
            "mitmirror.infra.tests.user_repository_spy.UserRepositorySpy.get_users",
            return_value=[],
        ):
            get_users.all_users()

    assert "Nenhum usuario encontrado!" in str(error.value)
