"""Arquivo para montar o caso de uso Authentication"""
from mitmirror.infra.repository import UserRepository
from mitmirror.data.auth import Authentication
from mitmirror.data.users import GetUser
from mitmirror.data.security import PasswordHash
from mitmirror.presenters.controllers.auth import AuthenticationController
from mitmirror.config import CONNECTION_STRING


def authentication_composer(connection_string: str = CONNECTION_STRING):
    """Montagem do caso de uso Authentication"""

    infra = UserRepository(connection_string)
    get_user = GetUser(infra)
    password_hash = PasswordHash()
    usecase = Authentication(get_user, password_hash)
    controller = AuthenticationController(usecase)

    return controller
