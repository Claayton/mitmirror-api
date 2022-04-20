"""Caso de uso: Authorization"""
from typing import Type
from fastapi import Request, HTTPException
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

    async def token_required(self, request: Request):
        """
        Serve como dependencia para rotas que necessitam de authorizaçao.
        :param request: Requisicao que deve receber o header Authorization, com o token de acesso.
        :return informacoes do usuario.
        """

        try:

            token = request.headers["Authorization"]

        except KeyError as error:

            http_error = HttpUnauthorized(message="Token invalido ou expirado!")

            raise HTTPException(
                status_code=http_error.status_code, detail=http_error.message
            ) from error

        try:

            data = jwt.decode(jwt=token, key=SECRET_KEY, algorithms="HS256")
            current_user = self.__get_user.by_email(data["email"])

        except Exception:  # pylint: disable=W0703

            http_error = HttpUnauthorized(message="Token invalido ou expirado!")

            return {"success": False, "data": {"error": http_error.message}}

        return current_user
