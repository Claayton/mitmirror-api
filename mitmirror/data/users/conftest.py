"""Arquivo para fixtures"""
from pytest import fixture
from mitmirror.infra.tests import UserRepositorySpy
from mitmirror.infra.tests import mock_user
from .register_user import RegisterUser


user = mock_user()


@fixture(scope="module")
def fake_user():
    """Mock de usuario"""

    return user


@fixture
def user_repository_spy():
    """Fixture para montar o objeto UserRepository"""

    return UserRepositorySpy()


@fixture
def register_user(user_repository_spy):  # pylint: disable=W0621
    """Fixture para montar o objeto RegisterUser"""

    return RegisterUser(user_repository_spy)
