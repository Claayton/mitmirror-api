"""Caso de uso: Authentication"""
from typing import Type, Dict
from datetime import datetime, timedelta
import jwt
from mitmirror.config import SECRET_KEY
from mitmirror.domain.usecases import GetUserInterface, PasswordHashInterface
from mitmirror.errors.http_error401 import HttpUnauthorized
from mitmirror.domain.usecases import AuthenticationInterface


class Authentication(AuthenticationInterface):
    """
    Classe responsavel pela autenticaçao dos usuarios no sistema.
    """

    def __init__(
        self,
        get_user: Type[GetUserInterface],
        hash_password: Type[PasswordHashInterface],
    ) -> None:
        self.__get_user = get_user
        self.__hash_password = hash_password

    def authentication(self, email: str, password: str) -> Dict[bool, Dict]:
        """
        Realiza autenticaçao de usuarios.
        :return: Uma mensagem de sucesso e um dicionario com informaçoes e um token.
        """

        user = self.__get_user.by_email(email=email)["data"]
        verify_password = self.__hash_password.verify(
            password, user.password_hash.encode("utf8")
        )

        if user and verify_password:

            payloads = {
                "exp": datetime.utcnow() + timedelta(hours=12),
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

        raise HttpUnauthorized(message="Erro de authenticaçao!")
