"""Testes para GetUserController"""
from pytest import raises
from mitmirror.errors import HttpNotFound, HttpBadRequestError, HttpUnprocessableEntity
from mitmirror.infra.tests import mock_user


user = mock_user()


def test_handler(get_user_controller_with_spy, user_repository_spy, fake_user):
    """Testando o metodo handler, buscando pelo id do usuario"""

    param = fake_user.id

    response = get_user_controller_with_spy.handler(param=param)

    # Testando as entradas:
    assert user_repository_spy.get_user_params["user_id"] == param

    # Testando as saidas:
    assert response.status_code == 200
    assert "error" not in response.body


def test_handler_error_with_invalid_user_id(get_user_controller_with_spy, fake_user):
    """
    Testando o erro no metodo handler.
    Onde e passado um valor invalido para o parametro user_id.
    Deve retornar um erro HttpUnprocessableEntity.
    """

    with raises(HttpUnprocessableEntity) as error:

        param = fake_user.name

        get_user_controller_with_spy.handler(param=param)

    # Testando as saidas:
    assert "error" in str(error.value)


def test_handler_error_without_user_id_param(get_user_controller_with_spy):
    """
    Testando o erro no metodo handler.
    Onde nao e passado o parametro de user_id.
    Deve retornar um erro HttpBadRequestError.
    """

    with raises(HttpBadRequestError) as error:

        get_user_controller_with_spy.handler()

    # Testando as saidas:
    assert "error" in str(error.value)


def test_handler_error_not_found(get_user_controller, fake_user):
    """
    Testando o erro no metodo handler.
    Onde nenhum usuario e encontrado no banco de dados.
    Deve retornar um erro HttpNotFound.
    """

    with raises(HttpNotFound) as error:

        param = fake_user.id

        get_user_controller.handler(param=param)

    # Testando as saidas:
    assert "error" in str(error.value)
