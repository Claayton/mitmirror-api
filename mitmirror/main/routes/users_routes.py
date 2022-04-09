"""Rotas de usuarios"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from mitmirror.main.adapters import request_adapter
from mitmirror.presenters.errors import handler_errors
from mitmirror.main.composers.users import (
    get_users_composer,
    get_user_composer,
    register_user_composer,
    update_user_composer,
    delete_user_composer,
)

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


@users.get("/{user_id:int}/")
async def get_user(request: RequestFastApi, user_id: int):
    """
    Rota para buscar um usuario registrado no sistema.
    :param user_id: ID do usuario para busca no db.
    :return: Um usuario e informacoes do mesmo.
    """

    try:

        response = None
        controller = get_user_composer()
        response = await request_adapter(request, controller.handler, user_id)

    except Exception as error:  # pylint: disable=W0703

        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@users.post("/")
async def register_user(request: RequestFastApi):
    """
    Rota para registrar um novo usuario no sistema.
    Deve receber os seguintes body-parameters:
    ('name: str', 'email: str', 'username: str', 'password: any').
    """

    try:

        response = None
        controller = register_user_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703

        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@users.put("/{user_id:int}/")
async def update_user(request: RequestFastApi, user_id: int):
    """
    Rota para dados de um usuario ja registrado no sistema.
    Deve receber os body-parameters 'user_id' + um dos seguintes:
    ('name: str', 'email: str', 'username: str', 'password: any').
    :param user_id: ID do usuario para busca no db.
    :return: Um usuario e informacoes do mesmo.
    """

    try:

        response = None
        controller = update_user_composer()
        response = await request_adapter(request, controller.handler, user_id)

    except Exception as error:  # pylint: disable=W0703

        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@users.delete("/{user_id:int}/")
async def delete_user(request: RequestFastApi, user_id: int):
    """
    Deleta um usuario que esteja cadastrado no banco de dados.
    :param user_id: ID do usuario para busca no db.
    :return: Um usuario e informacoes do mesmo.
    """

    try:

        response = None
        controller = delete_user_composer()
        response = await request_adapter(request, controller.handler, user_id)

    except Exception as error:  # pylint: disable=W0703

        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)
