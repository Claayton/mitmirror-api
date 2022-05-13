"""Lógica para tratamento de erros"""
from typing import Type, Dict
from mitmirror.presenters.helpers import HttpResponse
from mitmirror.errors import (
    HttpRequestError,
    HttpBadRequestError,
    HttpUnauthorized,
    HttpNotFound,
    HttpUnprocessableEntity,
    HttpForbidden,
)


def handler_errors(error: Type[Exception]) -> Dict:
    """
    Handler para tratamentos de execoes.
    :param error: Tipo de error gerado.
    :return: Um dicionario com o status_code e uma mensagem para esse tipo de erro.
    """

    if isinstance(
        error,
        (
            HttpRequestError,
            HttpBadRequestError,
            HttpUnprocessableEntity,
            HttpUnauthorized,
            HttpNotFound,
            HttpForbidden,
        ),
    ):
        http_response = HttpResponse(
            status_code=error.status_code, body={"error": str(error)}
        )

    else:
        http_response = HttpResponse(status_code=500, body={"error": str(error)})

    return http_response
