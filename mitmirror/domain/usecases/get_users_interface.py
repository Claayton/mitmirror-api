"""Arquivo de interface para GetUsers"""
from abc import ABC, abstractmethod
from typing import Dict
from mitmirror.domain.models import User


class GetUsersInterface(ABC):
    """Interface para GetrUsers"""

    @abstractmethod
    def all_users(self) -> Dict[bool, User]:
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo: all_users")
