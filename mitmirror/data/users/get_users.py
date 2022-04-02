"""Caso de uso Getusers"""
from typing import Type, Dict, List
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.domain.models import User
from mitmirror.domain.usecases import GetUsersInterface
from mitmirror.errors import DefaultError


class GetUsers(GetUsersInterface):
    """Classe responsavel pela busca de todos os usuarios cadastrados no sistema"""

    def __init__(self, user_repository: Type[UserRepositoryInterface]) -> None:

        self.__user_repository = user_repository

    def all_users(self) -> Dict[bool, List[User]]:
        """
        Realiza a busca de todos os usuarios no banco de dados.
        :return: Uma mensagem de sucesso e uma lista de usuarios.
        """

        data = None

        data = self.__user_repository.get_users()

        if data == []:

            raise DefaultError(message="Nenhum usuario encontrado!", type_error=404)

        return {"success": True, "data": self.__format_response(data)}

    @classmethod
    def __format_response(cls, data_list: List[User]) -> User:
        """Realiza a formatacao da resposta"""

        response = []

        if not data_list:

            return None

        for data in data_list:

            response.append(
                User(
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
            )

        return response
