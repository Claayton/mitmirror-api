"""Montando o caso de uso DeleteUser"""
from mitmirror.infra.repository import UserRepository
from mitmirror.data.users import DeleteUser
from mitmirror.presenters.controllers.users import DeleteUserController
from mitmirror.config import CONNECTION_STRING


def delete_user_composer():
    """Montagem do caso de uso DeleteUser"""

    infra = UserRepository(CONNECTION_STRING)
    usecase = DeleteUser(infra)
    controller = DeleteUserController(usecase)

    return controller
