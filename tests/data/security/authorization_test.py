"""Testes para a classe Authorization"""
from pytest import raises
from mitmirror.errors import HttpUnauthorized, HttpForbidden


def test_token_required(authorization, request_header):
    """Testando o metodo token_required"""

    response = authorization.token_required(request_header)

    assert response.id is not None
    assert response.name is not None
    assert response.email is not None


def test_token_required_error_without_authorization_header(
    authorization, request_without_authorization_header
):
    """
    Testando o erro no metodo token_required.
    Onde nao e encontrado o header Authorization.
    Deve retornar um erro 401 Unauthorized.
    """

    with raises(HttpUnauthorized) as error:

        authorization.token_required(request_without_authorization_header)

    assert "error" in str(error.value)


def test_token_required_error_with_invalid_token(
    authorization, request_with_invalid_token
):
    """
    Testando o erro no metodo token_required.
    Onde o token e invalido.
    Deve retornar um erro 401 Unauthorized.
    """

    with raises(HttpForbidden) as error:

        authorization.token_required(request_with_invalid_token)

    assert "error" in str(error.value)


def test_token_required_error_without_registered_user(
    authorization, request_without_registered_user
):
    """
    Testando o erro no metodo token_required.
    Onde o token e invalido.
    Deve retornar um erro 401 Unauthorized.
    """

    with raises(HttpForbidden) as error:

        authorization.token_required(request_without_registered_user)

    assert "error" in str(error.value)
