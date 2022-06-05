"""Caso de uso: Authorization"""
from typing import Type
from fastapi import Request as RequestFastApi
import jwt
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.domain.usecases import AuthorizationInterface
from mitmirror.errors import HttpUnauthorized, HttpForbidden
from mitmirror.config import settings


class Authorization(AuthorizationInterface):
    """
    Classe responsavel pela autorizaçao dos usuarios no sistema.
    """

    def __init__(self, user_repository: Type[UserRepositoryInterface]) -> None:
        self.__user_repository = user_repository

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

            data = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms="HS256")
            current_user = self.__user_repository.get_user(email=data["email"])

        except Exception as error:  # pylint: disable=W0703

            raise HttpForbidden(message="Token invalido ou expirado!, error") from error

        return current_user
