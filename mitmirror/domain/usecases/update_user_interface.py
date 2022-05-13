"""Arquivo de interface para UpdateUser"""
from abc import ABC, abstractmethod
from typing import Dict, Type
from datetime import datetime
from mitmirror.domain.models import User


class UpdateUserInterface(ABC):
    """Interface para UpdateUser"""

    @abstractmethod
    def update(
        self,
        user_id: int,
        name: str = None,
        email: str = None,
        username: str = None,
        password: any = None,
        secundary_id: int = None,
        is_staff: bool = None,
        is_active_user: bool = None,
        date_joined: Type[datetime] = None,
        last_login: Type[datetime] = None,
    ) -> Dict[bool, User]:
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo: update")
