"""Rotas de usuarios"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from mitmirror.main.adapters import request_adapter
from mitmirror.main.serializers.users import (
    UserOut,
    UsersOut,
    RegisterUserIn,
    UpdateUserIn,
)
from mitmirror.presenters.errors import handler_errors
from mitmirror.main.composers.users import (
    get_users_composer,
    get_user_composer,
    register_user_composer,
    update_user_composer,
    delete_user_composer,
)

users = APIRouter(prefix="/api/users", tags=["user"])


@users.get("/", response_model=UsersOut, status_code=200)
async def get_users(request: RequestFastApi):
    """
    Rota para buscar todos os usuarios registrados no sistema.
    """

    response = None

    try:

        controller = get_users_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703

        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@users.get("/{user_id:int}/", response_model=UserOut, status_code=200)
async def get_user(request: RequestFastApi, user_id: int):
    """
    Rota para buscar um usuario registrado no sistema, identificado pelo user_id.
    """

    response = None

    try:

        controller = get_user_composer()
        response = await request_adapter(request, controller.handler, user_id)

    except Exception as error:  # pylint: disable=W0703

        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@users.post("/", response_model=UserOut, status_code=201)
async def register_user(new_user: RegisterUserIn):
    """Rota para registrar um novo usuario no sistema."""

    response = None

    try:
        register = register_user_composer()
        response = register.handler(params=new_user.dict())

    except Exception as error:  # pylint: disable=W0703

        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@users.put("/{user_id:int}/", response_model=UserOut, status_code=200)
async def update_user(update_user_data: UpdateUserIn, user_id: int):
    """
    Rota para atualizar dados de um usuario ja registrado no sistema, identificado pelo user_id.
    """

    response = None

    try:

        update = update_user_composer()
        response = update.handler(params=update_user_data.dict(), user_id=user_id)

    except Exception as error:  # pylint: disable=W0703

        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@users.delete("/{user_id:int}/", response_model=UserOut, status_code=200)
async def delete_user(request: RequestFastApi, user_id: int):
    """
    Deleta um usuario que esteja cadastrado no banco de dados, identificado pelo user_id.
    """

    response = None

    try:

        controller = delete_user_composer()
        response = await request_adapter(request, controller.handler, user_id)

    except Exception as error:  # pylint: disable=W0703

        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)
