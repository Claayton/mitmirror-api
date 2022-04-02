"""Arquivo para fixtures"""
from pytest import fixture
from mitmirror.infra.tests import mock_user
from mitmirror.data.users import GetUser
from mitmirror.infra.tests import UserRepositorySpy
from .get_user_controller import GetUserController


user = mock_user()


@fixture(scope="module")
def fake_user():
    """Mock de usuario"""

    return user


@fixture
def user_repository():
    """Montagem de user_repository"""

    return UserRepositorySpy()


@fixture
def get_user_controller(user_repository):  # pylint: disable=W0621
    """Montagem de get_user_controller"""

    usecase = GetUser(user_repository)
    controller = GetUserController(usecase)

    return controller
