"""Fixtures para tests"""
from pytest import fixture
from fastapi import Request as RequestFastApi
from mitmirror.data.security import Authentication, Authorization
from tests.mocks import UserRepositorySpy, PasswordHashSpy


@fixture
def password_hash_spy():
    """Montando o objeto PasswordHashSpy"""

    return PasswordHashSpy()


@fixture
def authentication(password_hash_spy):  # pylint: disable=W0621
    """Montando o objeto Authentication"""

    user_repository_spy = UserRepositorySpy()

    return Authentication(user_repository_spy, password_hash_spy)


@fixture
def authorization():
    """Montando o objeto Authorization"""

    user_repository_spy = UserRepositorySpy()

    return Authorization(user_repository_spy)


@fixture
def request_header(authentication, fake_user):  # pylint: disable=W0621
    """Montando o request com um usuario adicionado e deletando no final."""

    response_token = authentication.authentication(fake_user.email, fake_user.password)
    token = response_token["data"]["Authorization"]

    yield RequestFastApi(
        scope={
            "type": "http",
            "headers": [("authorization".encode("latin-1"), token.encode("latin-1"))],
        }
    )


@fixture
def request_without_authorization_header():
    """Montando o objeto request sem headers"""

    return RequestFastApi(
        scope={"type": "http", "headers": [("token".encode(), "margarina".encode())]}
    )


@fixture
def request_with_invalid_token():
    """Montando o objeto request sem headers"""

    return RequestFastApi(
        scope={
            "type": "http",
            "headers": [("authorization".encode(), "margarina".encode())],
        }
    )


@fixture
def request_without_registered_user():
    """Montando o objeto request sem headers"""

    token = """
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.\
    eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.\
    SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
    """

    return RequestFastApi(
        scope={"type": "http", "headers": [("authorization".encode(), token.encode())]}
    )
