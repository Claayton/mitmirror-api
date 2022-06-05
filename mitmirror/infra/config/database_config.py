"""Configuraçoes de conexao de banco de dados"""
import warnings

from sqlalchemy.exc import SAWarning
from sqlmodel import create_engine, Session
from sqlmodel.sql.expression import Select, SelectOfScalar

from mitmirror.config import settings

warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True


engine = create_engine(settings.CONNECTION_STRING)


def get_session():
    """Entrega uma instancia da session, para manipular o db."""
    return Session(engine)
