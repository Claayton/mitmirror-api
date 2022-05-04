"""Arquivo para fixtures"""
from pytest import fixture
from mitmirror.config import CONNECTION_STRING
from ....mitmirror.infra.repository import UserRepository
from ....mitmirror.infra.tests import mock_user
from ....mitmirror.infra.config import DataBaseConnectionHandler


database = DataBaseConnectionHandler(CONNECTION_STRING)
user = mock_user()


@fixture
def mock_sqlalchemy(mocker):
    """teste de mocks"""

    mock = mocker.patch("")


@fixture(scope="module")
def fake_user():
    """Mock de usuario"""

    return user


@fixture
def user_repository():  # pylint: disable=W0621
    """Fixture para montar o objeto UserRepository"""

    return UserRepository(CONNECTION_STRING)


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
def user_repository_with_one_user_registered_and_delete_user(
    user_repository, fake_user
):  # pylint: disable=W0621
    """
    Fixture para montar o objeto UserRepository com usuario registrado,
    E deleta o usuario no final do teste.
    """

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

    yield user_repository

    engine = database.get_engine()
    engine.execute(f"DELETE FROM users WHERE id='{fake_user.id}';")


@fixture
def user_repository_with_two_users_registered_and_delete_user(
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
                '{int(fake_user.id + index)}',
                '{fake_user.name}{index}',
                '{fake_user.email}{index}',
                '{fake_user.username}{index}',
                '{fake_user.password}{index}',
                '{fake_user.secundary_id}{index}',
                '{fake_user.is_staff}',
                '{fake_user.is_active_user}',
                '{fake_user.last_login}',
                '{fake_user.date_joined}'
            );
            """
        )

    yield user_repository

    engine = database.get_engine()
    engine.execute(f"DELETE FROM users WHERE id='{fake_user.id}';")
    engine.execute(f"DELETE FROM users WHERE id='{fake_user.id + 1}';")
