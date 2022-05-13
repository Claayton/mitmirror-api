"""Arquivo para montar o caso de uso Authentication"""
from mitmirror.infra.repository import UserRepository
from mitmirror.data.security import Authentication, PasswordHash
from mitmirror.presenters.controllers.security import AuthenticationController


def authentication_composer():
    """Montagem do caso de uso Authentication"""

    user_repository = UserRepository()
    password_hash = PasswordHash()
    usecase = Authentication(user_repository, password_hash)
    controller = AuthenticationController(usecase)

    return controller
