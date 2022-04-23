"""Montando o caso de uso GetUser"""
from mitmirror.infra.repository import UserRepository
from mitmirror.data.users import GetUser
from mitmirror.presenters.controllers.users import GetUserController
from mitmirror.config import CONNECTION_STRING


def get_user_composer():
    """Montagem do caso de uso GetUser"""

    infra = UserRepository(CONNECTION_STRING)
    usecase = GetUser(infra)
    controller = GetUserController(usecase)

    return controller
