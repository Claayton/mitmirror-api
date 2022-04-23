"""Criação dos bancos de dados"""
from mitmirror.config import CONNECTION_STRING
from mitmirror.infra.entities import *  # pylint: disable=W0401, W0614
from mitmirror.infra.config import DataBaseConnectionHandler, Base


def create_db():
    """Criando bancos de dados"""

    db_connection = DataBaseConnectionHandler(CONNECTION_STRING)
    engine = db_connection.get_engine()
    base = Base.metadata.create_all(engine)

    return base
