"""Arquivo para fixtures"""
from pytest import fixture
from faker import Faker
from mitmirror.config import database_infos
from . import UserRepository
from ..config import DataBaseConnectionHandler


fake = Faker()
database = DataBaseConnectionHandler(database_infos["connection_string"])

fake_user = {
    "user_id": fake.random_number(),
    "name": fake.name(),
    "email": f"{fake.name()}@test.com",
    "username": f"{fake.name()}_vidaloka",
    "password_hash": fake.pystr(),
    "secundary_id": fake.random_number(),
}


@fixture
def user_repository():
    """Fixture para montar o objeto UserRepository"""

    yield UserRepository(database_infos["connection_string"])

    name = fake_user["name"]

    engine = database.get_engine()
    engine.execute(f"DELETE FROM users WHERE name='{name}';")
