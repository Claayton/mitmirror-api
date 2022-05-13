"""Arquivo de interface para UserRepository"""
from abc import ABC, abstractmethod
from typing import Type, List
from datetime import datetime
from mitmirror.domain.models import User


class UserRepositoryInterface(ABC):
    """Interface para a classe UserRepository"""

    @abstractmethod
    def insert_user(
        self,
        name: str,
        email: str,
        username: str,
        password_hash: str,
        secundary_id: int = 0,  # Configurar futuramente
        is_staff: bool = False,  # Configurar futuramente
        is_active_user: bool = False,  # Configurar futuramente
        date_joined: Type[datetime] = datetime.today(),  # Configurar futuramente
        last_login: Type[datetime] = datetime.today(),
    ) -> User:
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo insert_user")

    @abstractmethod
    def get_user(
        self, user_id: int = None, username: str = None, email: str = None
    ) -> User:
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo get_user")

    @abstractmethod
    def get_users(self) -> List[User]:
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo get_users")

    @abstractmethod
    def update_user(
        self,
        user_id: int,
        name: str = None,
        email: str = None,
        username: str = None,
        password_hash: str = None,
        secundary_id: int = None,
        is_staff: bool = None,
        is_active_user: bool = None,
        date_joined: Type[datetime] = None,
        last_login: Type[datetime] = None,
    ) -> User:
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo update_user")

    @abstractmethod
    def delete_user(self, user_id: int) -> User:
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo delete_user")
