"""Montando o caso de uso UpdateUser"""
from mitmirror.infra.repository import UserRepository
from mitmirror.data.users import UpdateUser
from mitmirror.data.security import PasswordHash
from mitmirror.presenters.controllers.users import UpdateUserController
from mitmirror.config import CONNECTION_STRING


def update_user_composer(connection_string: str = CONNECTION_STRING):
    """Montagem do caso de uso UpdateUser"""

    infra = UserRepository(connection_string)
    password_hash = PasswordHash()
    usecase = UpdateUser(infra, password_hash)
    controller = UpdateUserController(usecase)

    return controller
