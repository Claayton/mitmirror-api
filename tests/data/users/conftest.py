"""Arquivo para fixtures"""  # pylint: disable=E0401
from pytest import fixture
from mitmirror.infra.tests import UserRepositorySpy
from mitmirror.data.security import PasswordHash
from mitmirror.data.users import (
    RegisterUser,
    GetUser,
    GetUsers,
    UpdateUser,
    DeleteUser,
)


@fixture
def user_repository_spy():
    """Fixture para montar o objeto UserRepository"""

    return UserRepositorySpy()


@fixture
def register_user(user_repository_spy):  # pylint: disable=W0621
    """Fixture para montar o objeto RegisterUser"""

    return RegisterUser(user_repository_spy, PasswordHash)


@fixture
def get_user(user_repository_spy):  # pylint: disable=W0621
    """Fixture para montar o objeto Getuser"""

    return GetUser(user_repository_spy)


@fixture
def get_users(user_repository_spy):  # pylint: disable=W0621
    """Fixture para montar o objeto GetUsers"""

    return GetUsers(user_repository_spy)


@fixture
def update_user(user_repository_spy):  # pylint: disable=W0621
    """Fixture para montar o objeto UpdateUser"""

    return UpdateUser(user_repository_spy, PasswordHash)


@fixture
def delete_user(user_repository_spy):  # pylint: disable=W0621
    """Fixture para montar o objeto DeleteUser"""

    return DeleteUser(user_repository_spy)
