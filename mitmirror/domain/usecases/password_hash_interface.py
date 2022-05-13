"""Arquivo de interface para Password"""
from abc import ABC, abstractmethod


class PasswordHashInterface(ABC):
    """Interface para Password"""

    @staticmethod
    @abstractmethod
    def hash(password: str) -> str:
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo: hash")

    @staticmethod
    @abstractmethod
    def verify(password: str, password_hashed: str) -> bool:
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo: verify")
