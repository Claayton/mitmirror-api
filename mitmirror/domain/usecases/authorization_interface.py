"""Arquivo de interface para Authorization"""
from abc import ABC, abstractmethod
from fastapi import Request as RequestFastApi


class AuthorizationInterface(ABC):
    """Interface para a classe Authorization"""

    @abstractmethod
    def token_required(self, request: RequestFastApi):
        """Deve ser implementado"""

        raise Exception("Must implement token_required")
