"""Arquivo para fixtures"""
from fastapi.testclient import TestClient
from pytest import fixture
from mitmirror.infra.tests import mock_user
from mitmirror.infra.config import DataBaseConnectionHandler
from mitmirror.config import CONNECTION_STRING_TEST
from .users_routes import users


user = mock_user()
data_base_connection_handler = DataBaseConnectionHandler(CONNECTION_STRING_TEST)


@fixture(scope="module")
def fake_user():
    """Mock de usuario"""

    return user


@fixture
def client_with_one_user(fake_user):  # pylint: disable=W0621
    """
    Montando o client com um usuario cadastrado,
    E deletando no final.
    """

    engine = data_base_connection_handler.get_engine()
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
            '{fake_user.password_hash}',
            '{fake_user.secundary_id}',
            '{fake_user.is_staff}',
            '{fake_user.is_active_user}',
            '{fake_user.last_login}',
            '{fake_user.date_joined}'
        );
        """
    )

    yield TestClient(users)

    engine.execute(f"DELETE FROM users WHERE username='{fake_user.username}';")


@fixture
def client_with_delete_user(fake_user):  # pylint: disable=W0621
    """Montando o client e deletando usuario no final"""

    yield TestClient(users)

    engine = data_base_connection_handler.get_engine()
    engine.execute(f"DELETE FROM users WHERE username='{fake_user.username}';")
