"""Caso de uso DeleteUser"""
from typing import Type, Dict
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.domain.models import User
from mitmirror.domain.usecases import DeleteUserInterface
from mitmirror.errors import DefaultError


class DeleteUser(DeleteUserInterface):
    """Classe responsavel por excluir um usuario do sistema"""

    def __init__(self, user_repository: Type[UserRepositoryInterface]) -> None:

        self.__user_repository = user_repository

    def delete(self, user_id: int) -> Dict[bool, User]:
        """
        Realiza a exclusao de um usuario no banco de dados pelo id.
        :param user_id: ID do usuario cadastrado.
        :return: Uma mensagem de sucesso e o usuario excluido.
        """

        data = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:

            data = self.__user_repository.delete_user(user_id=user_id)

            if not data:

                raise DefaultError(message="Usuario nao encontrado!", type_error=404)

        return {"success": validate_entry, "data": self.__format_response(data)}

    @classmethod
    def __format_response(cls, data) -> User:
        """Realiza a formatacao da resposta"""

        if not data:

            return None

        return User(
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
