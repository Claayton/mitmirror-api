"""Configuraçoes de conexao de banco de dados"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


class DataBaseConnectionHandler:
    """Conexao de banco de dados com SQLAlchemy"""

    def __init__(self, connection_string: str) -> None:
        self.__connection_string = connection_string
        self.session = None

    def get_engine(self):
        """Retorna uma conexao com o banco de dados"""

        if not database_exists(self.__connection_string):

            create_database(self.__connection_string)

        engine = create_engine(self.__connection_string)

        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
