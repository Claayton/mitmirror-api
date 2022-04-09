"""Montando o caso de uso UpdateUser"""
from typing import Type
from mitmirror.infra.repository import UserRepository
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.data.users import UpdateUser
from mitmirror.data.security import PasswordHash
from mitmirror.presenters.controllers.users import UpdateUserController
from mitmirror.config import CONNECTION_STRING


def update_user_composer(
    infra: Type[UserRepositoryInterface] = UserRepository(CONNECTION_STRING),
):
    """Montagem do caso de uso UpdateUser"""

    password_hash = PasswordHash()
    usecase = UpdateUser(infra, password_hash)
    controller = UpdateUserController(usecase)

    return controller
