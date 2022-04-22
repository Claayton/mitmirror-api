"""Caso de uso: Authorization"""
from typing import Type
from fastapi import Request as RequestFastApi
import jwt
from mitmirror.config import SECRET_KEY
from mitmirror.errors import HttpUnauthorized
from mitmirror.domain.usecases import AuthorizationInterface, GetUserInterface


class Authorization(AuthorizationInterface):
    """
    Classe responsavel pela autorizaçao dos usuarios no sistema.
    """

    def __init__(self, get_user: Type[GetUserInterface]) -> None:
        self.__get_user = get_user

    def token_required(self, request: RequestFastApi):
        """
        Serve como dependencia para rotas que necessitam de authorizaçao.
        :param request: Requisicao que deve receber o header Authorization, com o token de acesso.
        :return informacoes do usuario.
        """

        try:

            token = request.headers["Authorization"]

        except (KeyError, TypeError) as error:

            raise HttpUnauthorized(
                message="Essa requisicao necessita de um token de acesso!, error"
            ) from error

        try:

            data = jwt.decode(jwt=token, key=SECRET_KEY, algorithms="HS256")
            current_user = self.__get_user.by_email(data["email"])

        except Exception as error:  # pylint: disable=W0703

            raise HttpUnauthorized(
                message="Token invalido ou expirado!, error"
            ) from error

        return current_user["data"]
