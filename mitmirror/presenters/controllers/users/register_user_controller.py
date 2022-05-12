"""Controller para RegisterUser"""
from typing import Type, Optional
from datetime import datetime
from mitmirror.errors import HttpBadRequestError, DefaultError
from mitmirror.presenters.interfaces import ControllerInterface
from mitmirror.domain.usecases import RegisterUserInterface
from mitmirror.domain.models import User
from mitmirror.presenters.helpers import HttpRequest, HttpResponse


class RegisterUserController(ControllerInterface):
    """Controller para o caso de uso RegisterUser"""

    def __init__(self, usecase: Type[RegisterUserInterface]) -> None:

        self.__usecase = usecase

    def handler(
        self, param: Optional[any] = None, http_request: Type[HttpRequest] = None
    ) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        try:

            response = None

            if not http_request.body:

                raise DefaultError(type_error=400)

            body_params = http_request.body.keys()

            if (
                "name" not in body_params
                or "email" not in body_params
                or "username" not in body_params
                or "password" not in body_params
            ):

                raise DefaultError(type_error=400)

            name = http_request.body["name"]
            email = http_request.body["email"]
            username = http_request.body["username"]
            password = http_request.body["password"]

            response = self.__usecase.register(
                name=name, email=email, username=username, password=password
            )

            return self.__format_response(response["data"])

        except DefaultError as error:

            if error.type_error == 400:

                raise HttpBadRequestError(
                    message="Esta requisicao precisa dos seguintes parametros:\
        <str:name>, <str:email>, <str:username>, <any:password>, error!"
                ) from error

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
                "last_login": datetime.isoformat(response_method.last_login),
                "date_joined": datetime.isoformat(response_method.date_joined),
            },
        }

        return HttpResponse(status_code=201, body=response)
