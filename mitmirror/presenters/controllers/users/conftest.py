"""Arquivo para fixtures"""
from pytest import fixture
from mitmirror.infra.repository import UserRepository
from mitmirror.infra.tests import UserRepositorySpy, mock_user
from mitmirror.data.security import PasswordHash
from mitmirror.config import CONNECTION_STRING_TEST
from mitmirror.data.users import GetUser, GetUsers, RegisterUser, UpdateUser, DeleteUser
from . import (
    GetUserController,
    GetUsersController,
    RegisterUserController,
    UpdateUserController,
    DeleteUserController,
)


user = mock_user()


@fixture(scope="module")
def fake_user():
    """Mock de usuario"""

    return user


@fixture
def user_repository():
    """Montagem de user_repository"""

    return UserRepository(CONNECTION_STRING_TEST)


@fixture
def user_repository_spy():
    """Montagem de user_repository_spy"""

    return UserRepositorySpy()


@fixture
def get_user_controller(user_repository):  # pylint: disable=W0621
    """Montagem de get_user_controller"""

    usecase = GetUser(user_repository)
    controller = GetUserController(usecase)

    return controller


@fixture
def get_user_controller_with_spy(user_repository_spy):  # pylint: disable=W0621
    """Montagem de get_user_controller utilizando o spy"""

    usecase = GetUser(user_repository_spy)
    controller = GetUserController(usecase)

    return controller


@fixture
def get_users_controller(user_repository):  # pylint: disable=W0621
    """montagem de get_users_controller"""

    usecase = GetUsers(user_repository)
    controller = GetUsersController(usecase)

    return controller


@fixture
def get_users_controller_with_spy(user_repository_spy):  # pylint: disable=W0621
    """Montagem de get_users_controller utilizando o spy"""

    usecase = GetUsers(user_repository_spy)
    controller = GetUsersController(usecase)

    return controller


@fixture
def register_user_with_spy(user_repository_spy):  # pylint: disable=W0621
    """montagem de register_user_controller utilizando spy"""

    usecase = RegisterUser(user_repository_spy, PasswordHash())
    controller = RegisterUserController(usecase)

    return controller


@fixture
def update_user(user_repository):  # pylint: disable=W0621
    """montagem de update_user_controller"""

    usecase = UpdateUser(user_repository, PasswordHash())
    controller = UpdateUserController(usecase)

    return controller


@fixture
def update_user_with_spy(user_repository_spy):  # pylint: disable=W0621
    """montagem de update_user_controller utilizando spy"""

    usecase = UpdateUser(user_repository_spy, PasswordHash())
    controller = UpdateUserController(usecase)

    return controller


@fixture
def delete_user(user_repository):  # pylint: disable=W0621
    """montagem de delete_user_controller"""

    usecase = DeleteUser(user_repository)
    controller = DeleteUserController(usecase)

    return controller


@fixture
def delete_user_with_spy(user_repository_spy):  # pylint: disable=W0621
    """montagem de delete_user_controller utilizando spy"""

    usecase = DeleteUser(user_repository_spy)
    controller = DeleteUserController(usecase)

    return controller
