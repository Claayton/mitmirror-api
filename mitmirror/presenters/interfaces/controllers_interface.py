"""Arquivo de interface para controlers"""
from typing import Type
from abc import ABC, abstractmethod
from mitmirror.presenters.helpers import HttpRequest, HttpResponse


class ControllerInterface(ABC):
    """Interface Padrão para controllers"""

    @abstractmethod
    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Methodo para facilitar o request"""

        raise Exception("Should implement handler method")
