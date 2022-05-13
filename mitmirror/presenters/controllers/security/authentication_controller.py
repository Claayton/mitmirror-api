"""Controllers para Authentication"""
from typing import Type, Dict, Optional
from mitmirror.presenters.helpers import HttpRequest, HttpResponse
from mitmirror.errors import HttpBadRequestError, HttpUnprocessableEntity
from mitmirror.domain.usecases import AuthenticationInterface
from mitmirror.presenters.interfaces import ControllerInterface


class AuthenticationController(ControllerInterface):
    """Controller para o caso de uso Authentication"""

    def __init__(self, usecase: Type[AuthenticationInterface]) -> None:
        self.__usecase = usecase

    def handler(
        self, param: Optional[any] = None, http_request: Type[HttpRequest] = None
    ) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = None

        if http_request.body:

            body_params = http_request.body.keys()

            if "email" in body_params and "password" in body_params:

                email = http_request.body["email"]
                password = str(http_request.body["password"])

                response = self.__usecase.authentication(email, password)

                return self.__format_response(response["data"])

            raise HttpUnprocessableEntity(
                message="""
                Esta rota necessita dos seguintes parametros: 'email: str', 'password: str', error
                """
            )

        raise HttpBadRequestError(
            message="""
            Esta rota necessita dos seguintes body-params: 'email: str', 'password: str', error
            """
        )

    @classmethod
    def __format_response(cls, response_method: Dict) -> HttpResponse:
        """Formatando a resposta"""

        response = {
            "message": "Login efetuado com successo!",
            "data": {
                "Authorization": response_method["Authorization"],
                "exp": str(response_method["exp"]),
                "id": response_method["id"],
                "user": {
                    "id": response_method["user"]["id"],
                    "name": response_method["user"]["name"],
                    "email": response_method["user"]["email"],
                    "username": response_method["user"]["username"],
                    "password_hash": "Nao mostramos isso aqui!",
                    "secundary_id": response_method["user"]["secundary_id"],
                    "is_staff": response_method["user"]["is_staff"],
                    "is_active_user": response_method["user"]["is_active_user"],
                    "last_login": response_method["user"]["last_login"],
                    "date_joined": response_method["user"]["date_joined"],
                },
            },
        }

        return HttpResponse(status_code=200, body=response)
