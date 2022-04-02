"""Arquivo para fixtures"""
from pytest import fixture
from mitmirror.infra.tests import UserRepositorySpy
from mitmirror.infra.tests import mock_user
from mitmirror.infra.config import DataBaseConnectionHandler
from mitmirror.infra.repository import UserRepository
from mitmirror.config import database_infos
from .register_user import RegisterUser
from .get_user import GetUser
from .get_users import GetUsers
from .update_user import UpdateUser


database = DataBaseConnectionHandler(database_infos["connection_string"])
user = mock_user()


@fixture(scope="module")
def fake_user():
    """Mock de usuario"""

    return user


@fixture
def user_repository():
    """repositorio padrao"""

    return UserRepository(database_infos["connection_string"])


@fixture
def user_repository_spy():
    """Fixture para montar o objeto UserRepository"""

    return UserRepositorySpy()


@fixture
def register_user(user_repository_spy):  # pylint: disable=W0621
    """Fixture para montar o objeto RegisterUser"""

    return RegisterUser(user_repository_spy)


@fixture
def get_user(user_repository):  # pylint: disable=W0621
    """Fixture para montar o objeto GetUser"""

    return GetUser(user_repository)


@fixture
def get_user_with_spy(user_repository_spy):  # pylint: disable=W0621
    """Fixture para montar o objeto Getuser"""

    return GetUser(user_repository_spy)


@fixture
def get_users(user_repository):  # pylint: disable=W0621
    """Fixture para montar o objeto GetUsers"""

    return GetUsers(user_repository)


@fixture
def get_users_with_spy(user_repository_spy):  # pylint: disable=W0621
    """Fixture para montar o objeto Getusers"""

    return GetUsers(user_repository_spy)


@fixture
def update_user(user_repository_spy):  # pylint: disable=W0621
    """Fixture para montar o objeto Updateusers"""

    return UpdateUser(user_repository_spy)
