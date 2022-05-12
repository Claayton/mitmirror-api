"""Arquivo para fixtures"""
from pytest import fixture
from mitmirror.data.security import PasswordHash
from mitmirror.data.users import GetUser, GetUsers, RegisterUser, UpdateUser, DeleteUser
from mitmirror.presenters.controllers.users import (
    GetUserController,
    GetUsersController,
    RegisterUserController,
    UpdateUserController,
    DeleteUserController,
)
from tests.mocks import UserRepositorySpy


@fixture
def user_repository_spy():
    """Montagem de user_repository_spy"""

    return UserRepositorySpy()


@fixture
def get_user_controller(user_repository_spy):  # pylint: disable=W0621
    """Montagem de get_user_controller utilizando o spy"""

    usecase = GetUser(user_repository_spy)
    controller = GetUserController(usecase)

    return controller


@fixture
def get_users_controller(user_repository_spy):  # pylint: disable=W0621
    """Montagem de get_users_controller utilizando o spy"""

    usecase = GetUsers(user_repository_spy)
    controller = GetUsersController(usecase)

    return controller


@fixture
def register_user(user_repository_spy):  # pylint: disable=W0621
    """montagem de register_user_controller utilizando spy"""

    usecase = RegisterUser(user_repository_spy, PasswordHash())
    controller = RegisterUserController(usecase)

    return controller


@fixture
def update_user(user_repository_spy):  # pylint: disable=W0621
    """montagem de update_user_controller utilizando spy"""

    usecase = UpdateUser(user_repository_spy, PasswordHash())
    controller = UpdateUserController(usecase)

    return controller


@fixture
def delete_user(user_repository_spy):  # pylint: disable=W0621
    """montagem de delete_user_controller utilizando spy"""

    usecase = DeleteUser(user_repository_spy)
    controller = DeleteUserController(usecase)

    return controller
