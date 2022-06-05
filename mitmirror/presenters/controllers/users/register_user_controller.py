"""Controller para RegisterUser"""
from typing import Type, Dict
from datetime import datetime
from mitmirror.errors import HttpBadRequestError, DefaultError
from mitmirror.domain.usecases import RegisterUserInterface
from mitmirror.domain.models import User
from mitmirror.presenters.helpers import HttpResponse


class RegisterUserController:
    """Controller para o caso de uso RegisterUser"""

    def __init__(self, usecase: Type[RegisterUserInterface]) -> None:

        self.__usecase = usecase

    def handler(self, params: Dict) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        try:

            if params is None or (
                "name" not in params
                or "email" not in params
                or "username" not in params
                or "password" not in params
            ):

                raise DefaultError(type_error=400)

            response = self.__usecase.register(**params)

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
