"""Arquivo para fixtures"""
from unittest.mock import patch
from pytest import fixture
from sqlmodel import create_engine, SQLModel
from mitmirror.infra.tests import mock_user
from mitmirror.infra.entities import *  # pylint: disable=W0614, W0401


user = mock_user()


@fixture(scope="module")
def fake_user():
    """Mock de usuario"""

    return user


@fixture(autouse=True, scope="function")
def separate_database(request):
    """
    Cria um mock do banco de dados para que cada teste use um banco separado.
    """

    tmpdir = request.getfixturevalue("tmpdir")
    test_db = tmpdir.join("mitmirror.test.db")
    engine = create_engine(f"sqlite:///{test_db}")
    SQLModel.metadata.create_all(engine)
    with patch("mitmirror.infra.config.database_config.engine", engine):
        yield
