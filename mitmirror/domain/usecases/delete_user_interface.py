"""Arquivo de interface para DeleteUser"""
from abc import ABC, abstractmethod
from typing import Dict
from mitmirror.domain.models import User


class DeleteUserInterface(ABC):
    """Interface para DeleteUser"""

    @abstractmethod
    def delete(self, user_id: int) -> Dict[bool, User]:
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo: delete")
