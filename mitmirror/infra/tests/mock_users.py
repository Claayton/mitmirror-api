"""Arquivo de mock de usuarios"""
from faker import Faker
from mitmirror.domain.models import User


fake = Faker()


def mock_user():
    """Mock para users"""

    return User(
        id=fake.random_number(),
        name=fake.name(),
        email=f"{fake.name()}@test.com",
        username=f"{fake.name()}_vidaloka",
        password_hash=fake.pystr(),
        secundary_id=fake.random_number(),
        is_staff=False,
        is_active_user=False,
        last_login=fake.date_time(),
        date_joined=fake.date_time(),
    )
