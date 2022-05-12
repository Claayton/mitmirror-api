"""Montando o caso de uso DeleteUser"""
from mitmirror.infra.repository import UserRepository
from mitmirror.data.users import DeleteUser
from mitmirror.presenters.controllers.users import DeleteUserController


def delete_user_composer():
    """Montagem do caso de uso DeleteUser"""

    user_repository = UserRepository()
    usecase = DeleteUser(user_repository)
    controller = DeleteUserController(usecase)

    return controller
