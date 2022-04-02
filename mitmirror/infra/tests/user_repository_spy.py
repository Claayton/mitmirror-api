"""Arquivo de spy para classe UserRepository"""
from typing import Type, List
from datetime import datetime
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.domain.models import User
from . import mock_user


class UserRepositorySpy(UserRepositoryInterface):
    """Spy para UserRepository"""

    def __init__(self) -> None:

        self.insert_user_params = {}
        self.get_user_params = {}

    def insert_user(
        self,
        name: str,
        email: str,
        username: str,
        password_hash: str,
        secundary_id: int = 0,
        is_staff: bool = False,
        is_active_user: bool = False,
        date_joined: Type[datetime] = datetime.today(),
        last_login: Type[datetime] = datetime.today(),
    ) -> User:
        """Spy para insert_user"""

        self.insert_user_params["name"] = name
        self.insert_user_params["email"] = email
        self.insert_user_params["username"] = username
        self.insert_user_params["password_hash"] = password_hash
        self.insert_user_params["secundary_id"] = secundary_id
        self.insert_user_params["is_staff"] = is_staff
        self.insert_user_params["is_active_user"] = is_active_user
        self.insert_user_params["date_joined"] = date_joined
        self.insert_user_params["last_login"] = last_login

        return mock_user()

    def get_user(
        self, user_id: int = None, username: str = None, email: str = None
    ) -> User:
        """Spy para get_user"""

        self.get_user_params["user_id"] = user_id
        self.get_user_params["email"] = email
        self.get_user_params["username"] = username

        return mock_user()

    def get_users(self) -> List[User]:
        """Spy para get_users"""

        return [mock_user(), mock_user()]

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

        pass

    def delete_user(self, user_id: int) -> User:
        """Deve ser implementado"""

        pass
