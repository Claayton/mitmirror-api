"""Testes para a classe Authorization"""
from pytest import raises
from mitmirror.domain.models import User
from mitmirror.errors import HttpUnauthorized


def test_token_required(auth, request_header):
    """Testando o metodo token_required"""

    response = auth.token_required(request_header)

    assert isinstance(response, User)


def test_token_required_error_without_authorization_header(
    auth, request_with_wrong_header
):
    """
    Testando o erro no metodo token_required.
    Onde nao e encontrado o header Authorization.
    Deve retornar um erro 401 Unauthorized.
    """

    with raises(HttpUnauthorized) as error:

        auth.token_required(request_with_wrong_header)

    assert "error" in str(error.value)


def test_token_required_error_with_invalid_token(auth, request_with_invalid_token):
    """
    Testando o erro no metodo token_required.
    Onde o token e invalido.
    Deve retornar um erro 401 Unauthorized.
    """

    with raises(HttpUnauthorized) as error:

        auth.token_required(request_with_invalid_token)

    assert "error" in str(error.value)


def test_token_required_error_without_registered_user(
    auth, request_without_registered_user
):
    """
    Testando o erro no metodo token_required.
    Onde o token e invalido.
    Deve retornar um erro 401 Unauthorized.
    """

    with raises(HttpUnauthorized) as error:

        auth.token_required(request_without_registered_user)

    assert "error" in str(error.value)
