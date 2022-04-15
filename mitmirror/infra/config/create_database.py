"""Criação dos bancos de dados"""
from mitmirror.config import CONNECTION_STRING_TEST, CONNECTION_STRING
from mitmirror.infra.entities import *  # pylint: disable=W0401, W0614
from mitmirror.infra.config import DataBaseConnectionHandler, Base


def create_databases():
    """Criando bancos de dados"""

    db_connection = DataBaseConnectionHandler(CONNECTION_STRING)
    db_connection_tests = DataBaseConnectionHandler(CONNECTION_STRING_TEST)

    engine = db_connection.get_engine()
    engine_tests = db_connection_tests.get_engine()

    base = Base.metadata.create_all(engine)
    base = Base.metadata.create_all(engine_tests)

    return base
