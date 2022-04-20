"""Arquivo para fixtures"""
from pytest import fixture
from mitmirror.infra.tests import UserRepositorySpy
from mitmirror.data.users import GetUser
from mitmirror.data.tests import PasswordHashSpy
from mitmirror.data.auth import Authentication
from .authentication_controller import AuthenticationController


@fixture
def password_hash():
    """Montando password_hash"""

    return PasswordHashSpy()


@fixture
def authentication_controller(password_hash):  # pylint: disable=W0621
    """Montando o controller"""

    infra = UserRepositorySpy()
    get_user = GetUser(infra)
    usecase = Authentication(get_user, password_hash)
    controller = AuthenticationController(usecase)

    return controller
