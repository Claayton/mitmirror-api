"""Arquivo para fixtures"""
from pytest import fixture
from faker import Faker
from mitmirror.config import database_infos
from . import UserRepository
from ..config import DataBaseConnectionHandler


fake = Faker()
database = DataBaseConnectionHandler(database_infos["connection_string"])


@fixture(scope="module")
def mock_user():
    """Mock de usuario"""

    return {
        "user_id": fake.random_number(),
        "name": fake.name(),
        "email": f"{fake.name()}@test.com",
        "username": f"{fake.name()}_vidaloka",
        "password_hash": fake.pystr(),
        "secundary_id": fake.random_number(),
        "is_staff": False,
        "is_active_user": False,
        "last_login": fake.date_time(),
        "date_joined": fake.date_time(),
    }


@fixture
def user_repository():  # pylint: disable=W0621
    """Fixture para montar o objeto UserRepository"""

    return UserRepository(database_infos["connection_string"])


@fixture
def user_repository_with_delete_user(
    user_repository, mock_user
):  # pylint: disable=W0621
    """Fixture para montar o objeto e deletar um usuario no final"""

    username = mock_user["username"]

    yield user_repository

    engine = database.get_engine()
    engine.execute(f"DELETE FROM users WHERE username='{username}';")


@fixture
def user_repository_with_one_user_registered(
    user_repository, mock_user
):  # pylint: disable=W0621
    """Fixture para montar o objeto UserRepository com usuario registrado"""

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
            '{mock_user["user_id"]}',
            '{mock_user["name"]}',
            '{mock_user["email"]}',
            '{mock_user["username"]}',
            '{mock_user["password_hash"]}',
            '{mock_user["secundary_id"]}',
            '{mock_user["is_staff"]}',
            '{mock_user["is_active_user"]}',
            '{mock_user["last_login"]}',
            '{mock_user["date_joined"]}'
        );
        """
    )

    username = mock_user["username"]

    yield user_repository

    engine = database.get_engine()
    engine.execute(f"DELETE FROM users WHERE username='{username}';")


@fixture
def user_repository_with_two_users_registered(
    user_repository, mock_user
):  # pylint: disable=W0621
    """Fixture para montar o objeto UserRepository com usuarios registrados"""

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
            '{mock_user["user_id"]}',
            '{mock_user["name"]}',
            '{mock_user["email"]}',
            '{mock_user["username"]}',
            '{mock_user["password_hash"]}',
            '{mock_user["secundary_id"]}',
            '{mock_user["is_staff"]}',
            '{mock_user["is_active_user"]}',
            '{mock_user["last_login"]}',
            '{mock_user["date_joined"]}'
        );
        """
    )
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
            '{mock_user["user_id"]}2',
            '{mock_user["name"]}2',
            '{mock_user["email"]}2',
            '{mock_user["username"]}2',
            '{mock_user["password_hash"]}2',
            '{mock_user["secundary_id"]}2',
            '{mock_user["is_staff"]}2',
            '{mock_user["is_active_user"]}2',
            '{mock_user["last_login"]}2',
            '{mock_user["date_joined"]}2'
        );
        """
    )

    username1 = mock_user["username"]
    username2 = f'{mock_user["username"]}2'

    yield user_repository

    engine = database.get_engine()
    engine.execute(f"DELETE FROM users WHERE username='{username1}';")
    engine.execute(f"DELETE FROM users WHERE username='{username2}';")
