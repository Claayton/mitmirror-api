"""Instancia da tabela User e seus metodos"""
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

    token = relationship("Token", back_populates="user")

    def __repr__(self):
        return f"<User {self.name}>"
