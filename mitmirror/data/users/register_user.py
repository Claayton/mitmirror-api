"""Caso de uso RegisterUser"""
from typing import Type, Dict
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.domain.usecases import RegisterUserInterface
from mitmirror.domain.models import User
from mitmirror.errors import DefaultError


class RegisterUser(RegisterUserInterface):
    """Classe responsavel pelo registro de novos usuarios no sistema"""

    def __init__(self, user_repository: Type[UserRepositoryInterface]) -> None:

        self.__user_repository = user_repository

    def register(
        self, name: str, email: str, username: str, password: any
    ) -> Dict[bool, User]:
        """
        Realiza o registro de novos usuarios no sistema.
        :param name: Nome do usuario.
        :param email: Email do usuario.
        :param username: Nome de usuario unico para cada um.
        :param password: Senha do usuario.
        """

        validate_entry = (
            isinstance(name, str)
            and isinstance(email, str)
            and isinstance(username, str)
            and isinstance(password, str)
        )

        if validate_entry:

            # Falta password_hash
            user_insertion = self.__user_repository.insert_user(
                name=name, email=email, username=username, password_hash=password
            )

            return {
                "success": validate_entry,
                "data": self.__format_response(user_insertion),
            }

        raise DefaultError(
            "Esta requisicao necessita dos parametros: name, email, username, password",
            400,
        )

    @classmethod
    def __format_response(cls, data) -> User:
        """Realiza a formatacao da resposta"""

        response = User(
            id=data.id,
            name=data.name,
            email=data.email,
            username=data.username,
            password_hash=data.password_hash,
            secundary_id=data.secundary_id,
            is_staff=data.is_staff,
            is_active_user=data.is_active_user,
            last_login=data.last_login,
            date_joined=data.date_joined,
        )

        return response
