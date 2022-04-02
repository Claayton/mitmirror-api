"""Caso de uso GetUser"""
from typing import Type, Dict
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.domain.models import User
from mitmirror.domain.usecases import GetUserInterface
from mitmirror.errors import DefaultError


class GetUser(GetUserInterface):
    """Classe responsavel pela busca de um unico usuario cadastrado no sistema"""

    def __init__(self, user_repository: Type[UserRepositoryInterface]) -> None:

        self.__user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, User]:
        """
        Realiza a busca de um usuario no banco de dados pelo id.
        :param user_id: ID do usuario cadastrado.
        :return: Uma mensagem de sucesso e um usuario.
        """

        data = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:

            data = self.__user_repository.get_user(user_id=user_id)

            if data == []:

                raise DefaultError(message="Usuario nao encontrado!", type_error=404)

        return {"success": validate_entry, "data": self.__format_response(data)}

    def by_email(self, email: str) -> Dict[bool, User]:
        """
        Realiza a busca de um usuario no banco de dados pelo email.
        :param email: email do usuario cadastrado.
        :return: Uma mensagem de sucesso e um usuario.
        """

        data = None
        validate_entry = isinstance(email, str)

        if validate_entry:

            data = self.__user_repository.get_user(email=email)

            if data == []:

                raise DefaultError(message="Usuario nao encontrado!", type_error=404)

        return {"success": validate_entry, "data": self.__format_response(data)}

    def by_username(self, username: str) -> Dict[bool, User]:
        """
        Realiza a busca de um usuario no banco de dados pelo username.
        :param username: username do usuario cadastrado.
        :return: Uma mensagem de sucesso e um usuario.
        """

        data = None
        validate_entry = isinstance(username, str)

        if validate_entry:

            data = self.__user_repository.get_user(username=username)

            if data == []:

                raise DefaultError(message="Usuario nao encontrado!", type_error=404)

        return {"success": validate_entry, "data": self.__format_response(data)}

    @classmethod
    def __format_response(cls, data) -> User:
        """Realiza a formatacao da resposta"""

        if not data:

            return None

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
