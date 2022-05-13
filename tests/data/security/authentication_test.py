"""Testes para a classe Authentication"""
from unittest.mock import patch
from pytest import raises
from mitmirror.errors import HttpUnauthorized, HttpForbidden


def test_authentication(authentication, password_hash_spy, fake_user):
    """Testando o metodo authentication"""

    response = authentication.authentication(fake_user.email, fake_user.password)

    # Testando a entrada:
    assert password_hash_spy.verify_params["password"] == fake_user.password

    # Testando a saida:
    assert isinstance(response, dict)
    assert "exp" in response["data"]
    assert "Authorization" in response["data"]
    assert "user" in response["data"]


def test_authentication_without_registered_user(authentication, fake_user):
    """
    Testando o erro no metodo authentication.
    Onde nao e encontrado nenhum usuario.
    Deve retornar um erro HttpUnauthorized.
    """

    with raises(HttpUnauthorized) as error:

        with patch(
            "tests.mocks.user_repository_spy.UserRepositorySpy.get_user",
            return_value=[],
        ):
            authentication.authentication(fake_user.email, fake_user.password)

    assert "Credenciais nao autorizadas!" in str(error.value)


def test_authentication_with_token_invalid_or_expired(authentication, fake_user):
    """
    Testando o erro no metodo authentication.
    Onde o token e invalido ou ja expirou.
    Deve retornar um erro HttpForbidden.
    """

    with raises(HttpForbidden) as error:

        with patch(
            "tests.mocks.password_hash_spy.PasswordHashSpy.verify",
            return_value=False,
        ):
            authentication.authentication(fake_user.email, fake_user.password)

    assert "Erro de autenticacao!" in str(error.value)
