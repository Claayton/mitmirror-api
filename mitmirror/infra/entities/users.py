"""Instancia da tabela User e seus metodos"""
from typing import Type
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from mitmirror.infra.config import Base


class User(Base):
    """Tabela de usuarios"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(256), nullable=False)

    secundary_id = Column(Integer, nullable=False)
    is_staff = Column(Boolean, nullable=False)
    is_active_user = Column(Boolean, nullable=False)
    last_login = Column(DateTime, nullable=False)
    date_joined = Column(DateTime, nullable=False)

    tokens = relationship("Token")

    def __init__(
        self,
        name: str,
        email: str,
        username: str,
        password_hash: str,
        secondary_id: int = 0,  # Configurar futuramente
        is_staff: bool = False,  # Configurar futuramente
        is_active: bool = False,  # Configurar futuramente
        date_joined: Type[datetime] = None,
    ):

        self.name = name
        self.email = email
        self.username = username
        self.password_hash = password_hash

        self.secondary_id = secondary_id
        self.is_istaff = is_staff
        self.is_active = is_active
        self.last_login = datetime.today()
        self.date_joined = date_joined

    def __repr__(self):
        return f"<User {self.name}>"
