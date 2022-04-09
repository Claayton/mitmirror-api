"""montando o caso de uso RegisterUser"""
from typing import Type
from mitmirror.infra.repository import UserRepository
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.data.users import RegisterUser
from mitmirror.data.security import PasswordHash
from mitmirror.presenters.controllers.users import RegisterUserController
from mitmirror.config import CONNECTION_STRING_TEST


def register_user_composer(
    infra: Type[UserRepositoryInterface] = UserRepository(CONNECTION_STRING_TEST),
):
    """Montagem do caso de uso RegisterUser"""

    password_hash = PasswordHash()
    usecase = RegisterUser(infra, password_hash)
    controller = RegisterUserController(usecase)

    return controller
