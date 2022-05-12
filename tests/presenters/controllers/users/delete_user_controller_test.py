"""Testes para DeleteUserController"""
from pytest import raises
from mitmirror.errors import HttpNotFound, HttpBadRequestError, HttpUnprocessableEntity
from mitmirror.infra.tests import mock_user
from mitmirror.presenters.helpers.http_models import HttpRequest


user = mock_user()


def test_handler(delete_user_with_spy, user_repository_spy, fake_user):
    """Testando o metodo handler"""

    param = fake_user.id

    response = delete_user_with_spy.handler(param=param, http_request=HttpRequest())

    # Testando as entradas:
    assert user_repository_spy.delete_user_params["user_id"] == param

    # Testando as saidas:
    assert response.status_code == 204
    assert "error" not in response.body


def test_handler_error_with_invalid_user_id(delete_user_with_spy, fake_user):
    """
    Testando o error no metodo handler.
    Onde e passado um valor invalido para o parametro user_id.
    Deve retornar um erro HttpUnprocessableEntity.
    """

    with raises(HttpUnprocessableEntity) as error:

        param = fake_user.name

        delete_user_with_spy.handler(param=param, http_request=HttpRequest())

    # Testando as saidas:
    assert "error" in str(error.value)


def test_handler_error_without_user_id_param(delete_user_with_spy):
    """
    Testando o erro no metodo handler.
    Onde nao e passado o parametro de user_id.
    Deve retornar um erro HttpBadRequestError.
    """

    with raises(HttpBadRequestError) as error:

        delete_user_with_spy.handler(http_request=HttpRequest())

    # Testando as saidas:
    assert "error" in str(error.value)


def test_handler_error_not_found(delete_user, fake_user):
    """
    Testando o erro no metodo handler.
    Onde nao e passado o parametro de user_id.
    Deve retornar um erro HttpNotFound.
    """

    with raises(HttpNotFound) as error:

        param = fake_user.id

        delete_user.handler(param=param, http_request=HttpRequest())

    # Testando as saidas:
    assert "error" in str(error.value)
