"""Controllers para GetUsers"""
from typing import Type, List
from mitmirror.domain.models import User
from mitmirror.errors import HttpNotFound, DefaultError
from mitmirror.presenters.helpers import HttpRequest, HttpResponse
from mitmirror.domain.usecases import GetUsersInterface
from mitmirror.presenters.interfaces import ControllerInterface


class GetUsersController(ControllerInterface):
    """Controller para o caso de uso GetUsers"""

    def __init__(self, usecase: Type[GetUsersInterface]) -> None:

        self.__usecase = usecase

    def handler(
        self, param: any = None, http_request: Type[HttpRequest] = None
    ) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        try:

            response = self.__usecase.all_users()

            formated_response = self.__format_response(response["data"])

            return formated_response

        except DefaultError as error:

            if error.type_error == 404:

                raise HttpNotFound(
                    message="Nenhum usuario encontrado, error!"
                ) from error

            raise error

        except Exception as error:

            raise error

    @classmethod
    def __format_response(cls, response_method: List[User]) -> HttpResponse:
        """Formatando a resposta"""

        full_response = []

        for user in response_method:

            full_response.append(
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "username": user.username,
                    "password_hash": "Nao mostramos isso aqui!",
                    "secundary_id": user.secundary_id,
                    "is_staff": user.is_staff,
                    "is_active_user": user.is_active_user,
                    "last_login": user.last_login,
                    "date_joined": user.date_joined,
                }
            )

        response = {"message": "Usuarios encontrados!", "data": full_response}

        return HttpResponse(status_code=200, body=response)
