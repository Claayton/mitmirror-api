"""Caso de uso UpdateUser"""
from typing import Type, Dict
from datetime import datetime
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.domain.usecases import UpdateUserInterface, PasswordHashInterface
from mitmirror.domain.models import User
from mitmirror.errors import DefaultError


class UpdateUser(UpdateUserInterface):
    """Classe responsavel pela atualizacao de dados de usuarios"""

    def __init__(
        self,
        user_repository: Type[UserRepositoryInterface],
        password_hash: Type[PasswordHashInterface]
    ) -> None:

        self.__user_repository = user_repository
        self.__password_hash = password_hash

    def update(
        self,
        user_id: int,
        name: str = None,
        email: str = None,
        username: str = None,
        password: any = None,
        secundary_id: int = None,
        is_staff: bool = None,
        is_active_user: bool = None,
        date_joined: Type[datetime] = None,
        last_login: Type[datetime] = None,
    ) -> Dict[bool, User]:
        """
        Realiza o registro de novos usuarios no sistema.
        :param user_id: ID do usuario.
        :param name: Nome do usuario.
        :param email: Email do usuario.
        :param username: Nome de usuario unico para cada um.
        :param password: Senha do usuario.
        :param secundary_id: Numero secundario de identificacao do usuario.
        :param is_staff: Se o usuario e ou nao o admin sistema.
        :param is_active_user: Se o usuario e esta ativo no sistema.
        :param date_joined: Data de cadastro do usuario no sistema.
        :param last_login: Data do ultimo login do usuario no sistema.
        :return: Uma mensagem de sucesso e o usuario com seus dados atualizados.
        """

        password_hash = self.__password_hash.hash(password)

        try:

            user_update = self.__user_repository.update_user(
                user_id=user_id,
                name=name,
                email=email,
                username=username,
                password_hash=password_hash.decode(),
                secundary_id=secundary_id,
                is_staff=is_staff,
                is_active_user=is_active_user,
                date_joined=date_joined,
                last_login=last_login,
            )

            return {
                "success": True,
                "data": self.__format_response(user_update),
            }

        except Exception as error:

            raise DefaultError() from error

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
