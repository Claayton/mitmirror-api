"""Criação dos bancos de dados"""
from sqlmodel import SQLModel
from mitmirror.infra.entities import *
from .database_config import engine


def create_db():
    """Criando bancos de dados"""

    base = SQLModel.metadata.create_all(engine)

    return base
