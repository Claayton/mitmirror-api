"""Serializer para User"""
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class UserData(BaseModel):
    """Dados do usuario"""

    id: int
    name: str
    email: str
    username: str
    password_hash: str
    secundary_id: int
    is_staff: bool
    is_active_user: bool
    last_login: datetime
    date_joined: datetime


class RegisterUserIn(BaseModel):
    """Cadastrar novo usuario"""

    name: str
    email: str
    username: str
    password: str


class UpdateUserIn(BaseModel):
    """Atualizar dados de usuario ja registrado"""

    name: Optional[str]
    email: Optional[str]
    username: Optional[str]
    password: Optional[str]


class UserOut(BaseModel):
    """Saida para as rotas User"""

    message: str
    data: UserData


class UsersOut(BaseModel):
    """Saida para a rota Users"""

    message: str
    data: List[UserData]
