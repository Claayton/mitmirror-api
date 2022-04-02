"""Arquivo de interface para GetUser"""
from abc import ABC, abstractmethod
from typing import Dict
from mitmirror.domain.models import User


class GetUserInterface(ABC):
    """Interface para GetrUser"""

    @abstractmethod
    def by_id(self, user_id: int) -> Dict[bool, User]:
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo: by_id")

    @abstractmethod
    def by_email(self, email: str) -> Dict[bool, User]:
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo: email")

    @abstractmethod
    def by_username(self, username: str) -> Dict[bool, User]:
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo: username")
