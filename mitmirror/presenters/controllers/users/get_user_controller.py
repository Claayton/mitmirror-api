"""Controllers para GetUser"""
from typing import Type, Optional
from datetime import datetime
from mitmirror.domain.models import User
from mitmirror.domain.usecases import GetUserInterface
from mitmirror.presenters.interfaces import ControllerInterface
from mitmirror.presenters.helpers import HttpRequest, HttpResponse
from mitmirror.errors import (
    HttpBadRequestError,
    DefaultError,
    HttpNotFound,
    HttpUnprocessableEntity,
)


class GetUserController(ControllerInterface):
    """Controller para o caso de uso GetUser"""

    def __init__(self, usecase: Type[GetUserInterface]) -> None:

        self.__usecase = usecase

    def handler(
        self, param: Optional[any] = None, http_request: Type[HttpRequest] = None
    ) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = None

        if not param:

            raise HttpBadRequestError(
                message="Essa requisiçao exige o seguinte parametro: <int:user_id>, error!"
            )

        try:

            user_id = int(param)
            response = self.__usecase.by_id(user_id=user_id)

            return self.__format_response(response["data"])

        except ValueError as error:

            raise HttpUnprocessableEntity(
                message="O parametro <user_id> deve ser do tipo inteiro, error!"
            ) from error

        except DefaultError as error:

            if error.type_error == 404:

                raise HttpNotFound(
                    message="Nenhum usuario com os requisitos dos parametros encontrado!, error!"
                ) from error

            raise error

        except Exception as error:

            raise error

    @classmethod
    def __format_response(cls, response_method: Type[User]) -> HttpResponse:
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
                "last_login": datetime.isoformat(response_method.last_login),
                "date_joined": datetime.isoformat(response_method.date_joined),
            },
        }

        return HttpResponse(status_code=200, body=response)
