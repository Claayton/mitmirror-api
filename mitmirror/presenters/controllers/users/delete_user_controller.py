"""Controller para DeleteUser"""
from typing import Type
from mitmirror.errors import HttpBadRequestError, DefaultError
from mitmirror.errors.http_error404 import HttpNotFound
from mitmirror.errors.http_error422 import HttpUnprocessableEntity
from mitmirror.presenters.interfaces import ControllerInterface
from mitmirror.domain.usecases import DeleteUserInterface
from mitmirror.domain.models import User
from mitmirror.presenters.helpers import HttpRequest, HttpResponse


class DeleteUserController(ControllerInterface):
    """Controller para o caso de uso DeleteUser"""

    def __init__(self, usecase: Type[DeleteUserInterface]) -> None:

        self.__usecase = usecase

    def handler(
        self, param: any = None, http_request: Type[HttpRequest] = None
    ) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = None

        if not param:

            raise HttpBadRequestError(
                message="Essa requisiçao exige o seguinte parametro: <int:user_id>, error!"
            )

        if not str(param).isnumeric():

            raise HttpUnprocessableEntity(
                message="O parametro <user_id> deve ser do tipo inteiro, error!"
            )

        try:

            response = self.__usecase.delete(user_id=param)

            formated_response = self.__format_response(response["data"])

            return formated_response

        except DefaultError as error:

            if error.type_error == 404:

                raise HttpNotFound(message="Usuario nao encontrado, error!") from error

            raise error

        except Exception as error:

            raise error

    @classmethod
    def __format_response(cls, response_method: Type[User]) -> HttpResponse:
        """Formatando a resposta"""

        response = {
            "message": "Usuario cadastrado com sucesso!",
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

        return HttpResponse(status_code=204, body=response)
