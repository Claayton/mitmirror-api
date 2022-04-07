"""Arquivo para fixtures"""
from pytest import fixture
from mitmirror.infra.repository import UserRepository
from mitmirror.infra.tests import UserRepositorySpy, mock_user
from mitmirror.data.users import GetUser, GetUsers
from mitmirror.config import CONNECTION_STRING_TEST
from . import GetUserController, GetUsersController


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
