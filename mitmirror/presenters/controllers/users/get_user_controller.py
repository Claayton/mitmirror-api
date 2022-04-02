"""Controllers para GetUser"""
from typing import Type
from mitmirror.domain.models import User
from mitmirror.errors import HttpBadRequestError, HttpNotFound
from mitmirror.presenters.helpers import HttpRequest, HttpResponse
from mitmirror.domain.usecases import GetUserInterface
from mitmirror.presenters.interfaces import ControllerInterface


class GetUserController(ControllerInterface):
    """Controller para o caso de uso GetUser"""

    def __init__(self, usecase: Type[GetUserInterface]) -> None:

        self.__usecase = usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = None

        if http_request.query:

            query_string_params = http_request.query.keys()

            if "user_id" in query_string_params:

                user_id = int(http_request.query["user_id"])
                response = self.__usecase.by_id(user_id=user_id)

            elif "email" in query_string_params:

                email = http_request.query["email"]
                response = self.__usecase.by_email(email=email)

            elif "username" in query_string_params:

                username = http_request.query["username"]
                response = self.__usecase.by_username(username=username)

            else:

                raise HttpNotFound(
                    message="Nenhum usuario com os requisitos dos parametros encontrado!"
                )

            formated_response = self.__format_response(response["data"])

            return formated_response

        raise HttpBadRequestError(
            message="Essa requisiçao exige um dos seguintes parametros: \
'user_id: int', 'email: str', 'username: str'"
        )

    def __format_response(self, response_method: Type[User]) -> HttpResponse:
        """Formatando a resposta"""

        response = {
            "message": "Usuario encontrado!",
            "data": {
                "id": response_method.id,
                "name": response_method.name,
                "email": response_method.email,
                "username": response_method.username,
                "password_hash": "Nao mostramos isso aqui!",
                "secundary_id": response_method.secundary_id,
                "is_staff": response_method.is_staff,
                "is_active_user": response_method.is_active_user,
                "last_login": response_method.last_login,
                "date_joined": response_method.date_joined,
            },
        }

        return HttpResponse(status_code=200, body=response)
