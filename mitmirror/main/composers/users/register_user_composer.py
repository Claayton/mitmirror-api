"""montando o caso de uso RegisterUser"""
from mitmirror.infra.repository import UserRepository
from mitmirror.data.users import RegisterUser
from mitmirror.data.security import PasswordHash
from mitmirror.presenters.controllers.users import RegisterUserController
from mitmirror.config import CONNECTION_STRING


def register_user_composer(connection_string: str = CONNECTION_STRING):
    """Montagem do caso de uso RegisterUser"""

    infra = UserRepository(connection_string)
    password_hash = PasswordHash()
    usecase = RegisterUser(infra, password_hash)
    controller = RegisterUserController(usecase)

    return controller
