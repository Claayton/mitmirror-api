"""Arquivo para fixtures"""
from fastapi.testclient import TestClient
from pytest import fixture
from mitmirror.infra.entities import User as UserModel
from mitmirror.infra.config.database_config import get_session
from mitmirror.main.routes.users_routes import users
from mitmirror.main.routes.auth_routes import auth


@fixture
def client_users_with_one_user(fake_user):  # pylint: disable=W0621
    """
    Montando o client com um usuario cadastrado,
    """

    with get_session() as session:
        new_user = UserModel(
            id=fake_user.id,
            name=fake_user.name,
            email=fake_user.email,
            username=fake_user.username,
            password_hash=fake_user.password_hash,
            secundary_id=fake_user.secundary_id,
            is_staff=fake_user.is_staff,
            is_active_user=fake_user.is_active_user,
            date_joined=fake_user.date_joined,
            last_login=fake_user.last_login,
        )
        session.add(new_user)
        session.commit()

    yield TestClient(users)


@fixture
def client_users_with_one_user_and_delete(
    client_users_with_one_user, fake_user
):  # pylint: disable=W0621
    """
    Montando o client com um usuario cadastrado,
    """

    yield client_users_with_one_user

    engine = data_base_connection_handler.get_engine()
    engine.execute(f"DELETE FROM users WHERE id='{fake_user.id}';")


@fixture
def client_users_with_delete_user(fake_user):  # pylint: disable=W0621
    """Montando o client e deletando usuario no final"""

    yield TestClient(users)

    engine = data_base_connection_handler.get_engine()
    engine.execute(f"DELETE FROM users WHERE username='{fake_user.username}';")


@fixture
def client_auth_with_one(fake_user):  # pylint: disable=W0621
    """
    Montando o client com um usuario cadastrado,
    """

    with get_session() as session:
        new_user = UserModel(
            id=fake_user.id,
            name=fake_user.name,
            email=fake_user.email,
            username=fake_user.username,
            password_hash=fake_user.password_hash,
            secundary_id=fake_user.secundary_id,
            is_staff=fake_user.is_staff,
            is_active_user=fake_user.is_active_user,
            date_joined=fake_user.date_joined,
            last_login=fake_user.last_login,
        )
        session.add(new_user)
        session.commit()

    yield TestClient(auth)
