"""Montando o caso de uso UpdateUser"""
from mitmirror.infra.repository import UserRepository
from mitmirror.data.users import UpdateUser
from mitmirror.data.security import PasswordHash
from mitmirror.presenters.controllers.users import UpdateUserController
from mitmirror.config import CONNECTION_STRING


def update_user_composer():
    """Montagem do caso de uso UpdateUser"""

    infra = UserRepository(CONNECTION_STRING)
    password_hash = PasswordHash()
    usecase = UpdateUser(infra, password_hash)
    controller = UpdateUserController(usecase)

    return controller
