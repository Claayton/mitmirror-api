"""Testes para a classe DeleteUser"""  # pylint: disable=E0401
from unittest.mock import patch
from pytest import raises
from mitmirror.domain.models import User
from mitmirror.errors import DefaultError


def test_delete(delete_user, user_repository_spy, fake_user):
    """
    Testando o metodo delete.
    Deve retornar uma mensagem de sucesso, e um usuario.
    """

    response = delete_user.delete(user_id=fake_user.id)

    # Testando a entrada:
    assert user_repository_spy.delete_user_params["user_id"] == fake_user.id

    # Testando a saida:
    assert response["success"] is True
    assert isinstance(response["data"], User)


def test_delete_with_invalid_param(delete_user, user_repository_spy, fake_user):
    """
    Testando o erro metodo delete.
    Utilizando um valor invalido para o parametro user_id.
    Deve retornar uma mensagem negativa de sucesso e None.
    """

    response = delete_user.delete(user_id=fake_user.name)

    # Testando a entrada:
    assert not user_repository_spy.delete_user_params

    # Testando a saida:
    assert response["success"] is False
    assert response["data"] is None


def test_delete_with_no_result_found(delete_user, fake_user):
    """
    Testando o erro no metodo delete.
    Onde nao e encontrado nenhum usuario com o ID recebido
    Deve retornar um DefaultError.
    """

    with raises(DefaultError) as error:

        with patch(
            "tests.mocks.user_repository_spy.UserRepositorySpy.delete_user",
            return_value=[],
        ):
            delete_user.delete(user_id=fake_user.id)

    assert "Usuario nao encontrado!" in str(error.value)
