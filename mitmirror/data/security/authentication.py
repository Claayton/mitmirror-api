"""Caso de uso: Authentication"""
from typing import Type, Dict
from datetime import datetime, timedelta
import jwt
from mitmirror.config import SECRET_KEY
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.domain.usecases import PasswordHashInterface
from mitmirror.errors import HttpUnauthorized, HttpForbidden
from mitmirror.domain.usecases import AuthenticationInterface


class Authentication(AuthenticationInterface):
    """
    Classe responsavel pela autenticaçao dos usuarios no sistema.
    """

    def __init__(
        self,
        user_repository: Type[UserRepositoryInterface],
        password_hash: Type[PasswordHashInterface],
    ) -> None:
        self.__user_repository = user_repository
        self.__password_hash = password_hash

    def authentication(self, email: str, password: str) -> Dict[bool, Dict]:
        """
        Realiza autenticaçao de usuarios.
        :return: Uma mensagem de sucesso e um dicionario com informaçoes e um token.
        """

        user = self.__user_repository.get_user(email=email)

        if not user:

            raise HttpUnauthorized(message="Credenciais nao autorizadas!")

        verify_password = self.__password_hash.verify(
            password, user.password_hash.encode("utf8")
        )

        if not verify_password:

            raise HttpForbidden(message="Erro de autenticacao!")

        payloads = {
            "exp": datetime.utcnow() + timedelta(hours=24),
            "iat": datetime.utcnow(),
            "name": user.name,
            "email": user.email,
            "username": user.username,
        }

        token = jwt.encode(payload=payloads, key=SECRET_KEY)

        return {
            "success": True,
            "data": {
                "Authorization": token,
                "exp": payloads["exp"],
                "id": user.id,
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "username": user.username,
                    "password_hash": "Nao mostramos isso aqui!",
                    "secundary_id": user.secundary_id,
                    "is_staff": user.is_staff,
                    "is_active_user": user.is_active_user,
                    "last_login": datetime.isoformat(user.last_login),
                    "date_joined": datetime.isoformat(user.date_joined),
                },
            },
        }
