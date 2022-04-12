"""Montando o caso de uso GetUsers"""
from mitmirror.infra.repository import UserRepository
from mitmirror.data.users import GetUsers
from mitmirror.presenters.controllers.users import GetUsersController
from mitmirror.config import CONNECTION_STRING


def get_users_composer(connection_string: str = CONNECTION_STRING):
    """Montagem do caso de uso GetUsers"""

    infra = UserRepository(connection_string)
    usecase = GetUsers(infra)
    controller = GetUsersController(usecase)

    return controller
