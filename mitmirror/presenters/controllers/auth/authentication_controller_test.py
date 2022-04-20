"""Testes para AuthenticationController"""
from pytest import raises
from faker import Faker
from mitmirror.errors import HttpBadRequestError, HttpUnprocessableEntity
from mitmirror.presenters.helpers import HttpRequest

fake = Faker()


def test_handler(authentication_controller, password_hash):
    """Testando o metodo handler"""

    attributes = {"email": fake.email(), "password": fake.password()}

    response = authentication_controller.handler(
        http_request=HttpRequest(body=attributes)
    )

    # Testando as entradas:
    assert password_hash.verify_params["password"] == attributes["password"]

    # Testando as saidas:
    assert response.status_code == 200
    assert "error" not in response.body


def test_handler_error_without_body_params(authentication_controller):
    """
    Testando o erro no metodo handler.
    Onde nao e passado nenhum body-param.
    Deve retornar um erro 400, BadRequest.
    """

    with raises(HttpBadRequestError) as error:

        authentication_controller.handler(http_request=HttpRequest())

    assert "error" in str(error.value)


def test_handler_error_with_invalid_body_params(authentication_controller):
    """
    Testando o erro no metodo handler.
    Onde sao passados parametros invalidos para a requisicao.
    Deve retornar um erro 422 UnprocessableEntity
    """

    with raises(HttpUnprocessableEntity) as error:

        attributes = {"username": fake.user_name(), "pass": fake.password()}

        authentication_controller.handler(http_request=HttpRequest(body=attributes))

    assert "error" in str(error.value)
