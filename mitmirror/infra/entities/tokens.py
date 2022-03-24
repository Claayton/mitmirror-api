"""Instancia da tabela Token e seus metodos"""
from typing import Type
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from mitmirror.infra.config import Base


class Token(Base):
    """Tabela de tokens"""

    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, nullable=False)
    token = Column(String(256))
    expiration = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User")

    def __init__(self, token: str, user_id: int, expiration: Type[datetime]):

        self.token = token
        self.user_id = user_id
        self.expiration = expiration

    def __repr__(self):
        return f"<Token {self.id}: {self.user.name}>"
