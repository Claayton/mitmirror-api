"""Controller para UpdateUser"""
from typing import Type, Dict
from datetime import datetime
from mitmirror.domain.usecases import UpdateUserInterface
from mitmirror.domain.models import User
from mitmirror.presenters.helpers import HttpResponse
from mitmirror.errors import (
    HttpBadRequestError,
    DefaultError,
    HttpNotFound,
    HttpUnprocessableEntity,
)


class UpdateUserController:
    """Controller para o caso de uso UpdateUser"""

    def __init__(self, usecase: Type[UpdateUserInterface]) -> None:

        self.__usecase = usecase

    def handler(self, user_id: int, params: Dict = None) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        if not user_id:

            raise HttpBadRequestError(
                message="Essa requisiçao exige o seguinte parametro: <int:user_id>, error!"
            )

        if not str(user_id).isnumeric():

            raise HttpUnprocessableEntity(
                message="O parametro <user_id> deve ser do tipo inteiro, error!"
            )

        try:

            if params is None:

                raise DefaultError(type_error=400)

            name = params.get("name", None)
            email = params.get("email", None)
            username = params.get("username", None)
            password = params.get("password", None)

            response = self.__usecase.update(
                user_id=user_id,
                name=name,
                email=email,
                username=username,
                password=password,
            )

            return self.__format_response(response["data"])

        except DefaultError as error:

            if error.type_error == 400:

                raise HttpBadRequestError(
                    message="Esta requisicao precisa dos seguintes parametros:\
        <str:name>, <str:email>, <str:username>, <any:password>, error!"
                ) from error

            if error.type_error == 404:

                raise HttpNotFound(message="Usuario nao encontrado, error!") from error

            raise error

        except Exception as error:

            raise error

    @classmethod
    def __format_response(cls, response_method: Type[User]) -> HttpResponse:
        """Formatando a resposta"""

        response = {
            "message": "Informacoes do usuario atualizadas com sucesso!",
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
