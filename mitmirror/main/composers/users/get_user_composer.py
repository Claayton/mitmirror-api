"""Montando o caso de uso GetUser"""
from mitmirror.infra.repository import UserRepository
from mitmirror.data.users import GetUser
from mitmirror.presenters.controllers.users import GetUserController


def get_user_composer():
    """Montagem do caso de uso GetUser"""

    user_repository = UserRepository()
    usecase = GetUser(user_repository)
    controller = GetUserController(usecase)

    return controller
