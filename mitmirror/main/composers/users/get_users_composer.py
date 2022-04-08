"""Montando o caso de uso GetUsers"""
from typing import Type
from mitmirror.infra.repository import UserRepository
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.data.users import GetUser
from mitmirror.presenters.controllers.users import GetUsersController
from mitmirror.config import CONNECTION_STRING


def get_users_composer(
    infra: Type[UserRepositoryInterface] = UserRepository(CONNECTION_STRING),
):
    """Montagem do caso de uso GetUsers"""

    usecase = GetUser(infra)
    controller = GetUsersController(usecase)

    return controller
