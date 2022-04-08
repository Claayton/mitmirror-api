"""Rotas de usuarios"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from mitmirror.main.adapters import request_adapter
from mitmirror.presenters.errors import handler_errors
from mitmirror.main.composers.users import get_users_composer

users = APIRouter(prefix="/api/users", tags=["user"])


@users.get("/")
async def get_users(request: RequestFastApi):
    """
    Rota para buscar todos os usuarios registrados no sistema.
    """

    try:

        response = None
        controller = get_users_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703

        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)
