"""Arquivo de interface para Authorization"""
from abc import ABC, abstractmethod
from fastapi import Request


class AuthorizationInterface(ABC):
    """Interface para a classe Authorization"""

    @abstractmethod
    def token_required(self, request: Request):
        """Deve ser implementado"""

        raise Exception("Must implement token_required")
