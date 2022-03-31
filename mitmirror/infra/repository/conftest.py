"""Arquivo para fixtures"""
from pytest import fixture
from mitmirror.config import database_infos
from . import UserRepository
from ..tests import mock_user
from ..config import DataBaseConnectionHandler


database = DataBaseConnectionHandler(database_infos["connection_string"])
user = mock_user()


@fixture(scope="session")
def fake_user():
    """Mock de usuario"""

    return user


@fixture
def user_repository():  # pylint: disable=W0621
    """Fixture para montar o objeto UserRepository"""

    return UserRepository(database_infos["connection_string"])


@fixture
def user_repository_with_delete_user(
    user_repository, fake_user
):  # pylint: disable=W0621
    """Fixture para montar o objeto e deletar um usuario no final"""

    username = fake_user.username

    yield user_repository

    engine = database.get_engine()
    engine.execute(f"DELETE FROM users WHERE username='{username}';")


@fixture
def user_repository_with_one_user_registered(
    user_repository, fake_user
):  # pylint: disable=W0621
    """Fixture para montar o objeto UserRepository com usuario registrado"""
    print(f"\nNa fixture: {fake_user.username}")
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
            '{fake_user.password_hash}',
            '{fake_user.secundary_id}',
            '{fake_user.is_staff}',
            '{fake_user.is_active_user}',
            '{fake_user.last_login}',
            '{fake_user.date_joined}'
        );
        """
    )

    username = fake_user.username

    yield user_repository

    engine = database.get_engine()
    engine.execute(f"DELETE FROM users WHERE username='{username}';")


@fixture
def user_repository_with_two_users_registered(
    user_repository, fake_user
):  # pylint: disable=W0621
    """Fixture para montar o objeto UserRepository com usuarios registrados"""

    engine = database.get_engine()

    for index in range(0, 2):

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
                '{fake_user.id}{index}',
                '{fake_user.name}{index}',
                '{fake_user.email}{index}',
                '{fake_user.username}{index}',
                '{fake_user.password_hash}{index}',
                '{fake_user.secundary_id}{index}',
                '{fake_user.is_staff}{index}',
                '{fake_user.is_active_user}{index}',
                '{fake_user.last_login}{index}',
                '{fake_user.date_joined}{index}'
            );
            """
        )
    username1 = f"{fake_user.username}0"
    username2 = f"{fake_user.username}1"

    yield user_repository

    engine = database.get_engine()
    engine.execute(f"DELETE FROM users WHERE username='{username1}';")
    engine.execute(f"DELETE FROM users WHERE username='{username2}';")
