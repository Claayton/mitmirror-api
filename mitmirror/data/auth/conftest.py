"""Fixtures para tests"""
from pytest import fixture
from mitmirror.presenters.helpers import HttpRequest
from mitmirror.data.users import GetUser
from mitmirror.infra.repository import UserRepository
from mitmirror.config import CONNECTION_STRING_TEST
from mitmirror.infra.config import DataBaseConnectionHandler
from mitmirror.infra.tests import mock_user
from mitmirror.data.tests import PasswordHashSpy
from .authentication import Authentication
from .authorization import Authorization


database = DataBaseConnectionHandler(CONNECTION_STRING_TEST)
user = mock_user()


@fixture(scope="module")
def fake_user():
    """Mock de usuario"""

    return user


@fixture
def auth():
    """Montando o objeto Authorization"""

    infra = UserRepository(CONNECTION_STRING_TEST)
    get_user = GetUser(infra)

    return Authorization(get_user)


@fixture
def request_header(fake_user):  # pylint: disable=W0621
    """Montando o request com um usuario adicionado e deletando no final."""

    engine = database.get_engine()
    engine.execute(
        f"""
        INSERT INTO users (
            id,
            name,
            email,
            username,
            password_hash,
            secundary_id,
            is_staff,
            is_active_user,
            last_login,
            date_joined
        )
        VALUES (
            '{fake_user.id}',
            '{fake_user.name}',
            '{fake_user.email}',
            '{fake_user.username}',
            '{fake_user.password}',
            '{fake_user.secundary_id}',
            '{fake_user.is_staff}',
            '{fake_user.is_active_user}',
            '{fake_user.last_login}',
            '{fake_user.date_joined}'
        );
        """
    )

    infra = UserRepository(CONNECTION_STRING_TEST)
    get_user = GetUser(infra)
    password_hash = PasswordHashSpy()
    authentication = Authentication(get_user, password_hash)

    response_token = authentication.authentication(fake_user.email, fake_user.password)
    token = response_token["data"]["Authorization"]

    yield HttpRequest(headers={"Authorization": token})

    engine = database.get_engine()
    engine.execute(f"DELETE FROM users WHERE id='{fake_user.id}';")


@fixture
def request_with_wrong_header():
    """Montando o objeto request sem headers"""

    return HttpRequest(headers={"token": "margarina"})


@fixture
def request_with_invalid_token():
    """Montando o objeto request sem headers"""

    return HttpRequest(headers={"Authorization": "margarina"})


@fixture
def request_without_registered_user():
    """Montando o objeto request sem headers"""

    token = """
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.\
    eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.\
    SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
    """

    return HttpRequest(headers={"Authorization": token})
