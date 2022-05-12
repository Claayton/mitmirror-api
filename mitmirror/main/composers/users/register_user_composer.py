"""montando o caso de uso RegisterUser"""
from mitmirror.infra.repository import UserRepository
from mitmirror.data.users import RegisterUser
from mitmirror.data.security import PasswordHash
from mitmirror.presenters.controllers.users import RegisterUserController


def register_user_composer():
    """Montagem do caso de uso RegisterUser"""

    user_repository = UserRepository()
    password_hash = PasswordHash()
    usecase = RegisterUser(user_repository, password_hash)
    controller = RegisterUserController(usecase)

    return controller
