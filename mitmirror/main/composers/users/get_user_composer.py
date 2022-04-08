"""Montando o caso de uso GetUser"""
from typing import Type
from mitmirror.infra.repository import UserRepository
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.data.users import GetUser
from mitmirror.presenters.controllers.users import GetUserController
from mitmirror.config import CONNECTION_STRING


def get_user_composer(
    infra: Type[UserRepositoryInterface] = UserRepository(CONNECTION_STRING),
):
    """Montagem do caso de uso GetUser"""

    usecase = GetUser(infra)
    controller = GetUserController(usecase)

    return controller
