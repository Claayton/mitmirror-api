"""Testes para a classe Authentication"""
from faker import Faker
from mitmirror.infra.tests import UserRepositorySpy
from mitmirror.data.tests import PasswordHashSpy
from mitmirror.data.users import GetUser
from .authentication import Authentication

fake = Faker()


def test_authentication():
    """Testando o metodo authentication"""

    infra = UserRepositorySpy()
    get_user = GetUser(infra)
    hash_password = PasswordHashSpy()
    authentication = Authentication(get_user, hash_password)

    email = fake.email()
    password = "voumudaressasenhaumdia"

    response = authentication.authentication(email, password)

    # Testando a entrada:
    # Implementar spy para hash_password

    # Testando a saida:
    assert isinstance(response, dict)
    assert "exp" in response["data"]
    assert "Authorization" in response["data"]
    assert "user" in response["data"]
