"""Arquivo de interface para RegisterUser"""
from abc import ABC, abstractmethod
from typing import Dict
from mitmirror.domain.models import User


class RegisterUserInterface(ABC):
    """Interface para RegisterUser"""

    @abstractmethod
    def register(
        self, name: str, email: str, username: str, password: any
    ) -> Dict[bool, User]:
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo: register")
