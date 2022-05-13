"""Arquivo de interface para Authentication"""
from abc import ABC, abstractmethod
from typing import Dict


class AuthenticationInterface(ABC):
    """Interface para a classe Authentication"""

    @abstractmethod
    def authentication(self, email: str, password: str) -> Dict[bool, Dict]:
        """Deve ser implementado"""

        raise Exception("Must implement authentication")
