"""Montando o caso de uso DeleteUser"""
from mitmirror.infra.repository import UserRepository
from mitmirror.data.users import DeleteUser
from mitmirror.presenters.controllers.users import DeleteUserController
from mitmirror.config import CONNECTION_STRING


def delete_user_composer(connection_string: str = CONNECTION_STRING):
    """Montagem do caso de uso DeleteUser"""

    infra = UserRepository(connection_string)
    usecase = DeleteUser(infra)
    controller = DeleteUserController(usecase)

    return controller
