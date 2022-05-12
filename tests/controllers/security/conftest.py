"""Arquivo para fixtures"""
from pytest import fixture
from mitmirror.data.security import Authentication
from mitmirror.presenters.controllers.security import AuthenticationController
from tests.mocks import UserRepositorySpy, PasswordHashSpy


@fixture
def password_hash():
    """Montando password_hash"""

    return PasswordHashSpy()


@fixture
def authentication_controller(password_hash):  # pylint: disable=W0621
    """Montando o controller"""

    user_repository_spy = UserRepositorySpy()
    usecase = Authentication(user_repository_spy, password_hash)
    controller = AuthenticationController(usecase)

    return controller
