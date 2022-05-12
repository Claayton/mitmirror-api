"""Montando o caso de uso UpdateUser"""
from mitmirror.infra.repository import UserRepository
from mitmirror.data.users import UpdateUser
from mitmirror.data.security import PasswordHash
from mitmirror.presenters.controllers.users import UpdateUserController


def update_user_composer():
    """Montagem do caso de uso UpdateUser"""

    user_repository = UserRepository()
    password_hash = PasswordHash()
    usecase = UpdateUser(user_repository, password_hash)
    controller = UpdateUserController(usecase)

    return controller
