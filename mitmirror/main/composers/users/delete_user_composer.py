"""Montando o caso de uso DeleteUser"""
from typing import Type
from mitmirror.infra.repository import UserRepository
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.data.users import DeleteUser
from mitmirror.presenters.controllers.users import DeleteUserController
from mitmirror.config import CONNECTION_STRING_TEST


def delete_user_composer(
    infra: Type[UserRepositoryInterface] = UserRepository(CONNECTION_STRING_TEST),
):
    """Montagem do caso de uso DeleteUser"""

    usecase = DeleteUser(infra)
    controller = DeleteUserController(usecase)

    return controller
