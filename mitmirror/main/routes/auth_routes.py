"""Arquivo de rotas"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from mitmirror.config import CONNECTION_STRING_TEST
from mitmirror.main.adapters import request_adapter
from mitmirror.presenters.errors import handler_errors
from mitmirror.main.composers.auth import authentication_composer
from mitmirror.main.routes.middleware import middleware_testing

auth = APIRouter(prefix="/api/auth", tags=["authentication"])


@auth.post("/")
async def authentication(request: RequestFastApi):
    """Rota para autenticar usuarios registrados no sistema."""

    response = None

    try:

        if middleware_testing(request):

            controller = authentication_composer(
                connection_string=CONNECTION_STRING_TEST
            )
            response = await request_adapter(request, controller.handler)

        else:

            controller = authentication_composer()
            response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703

        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)
