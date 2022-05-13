"""Montando o caso de uso GetUsers"""
from mitmirror.infra.repository import UserRepository
from mitmirror.data.users import GetUsers
from mitmirror.presenters.controllers.users import GetUsersController


def get_users_composer():
    """Montagem do caso de uso GetUsers"""

    user_repository = UserRepository()
    usecase = GetUsers(user_repository)
    controller = GetUsersController(usecase)

    return controller
