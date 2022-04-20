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
    password_hash = PasswordHashSpy()
    authentication = Authentication(get_user, password_hash)

    email = fake.email()
    password = "voumudaressasenhaumdia"

    response = authentication.authentication(email, password)

    # Testando a entrada:
    assert password_hash.verify_params["password"] == password

    # Testando a saida:
    assert isinstance(response, dict)
    assert "exp" in response["data"]
    assert "Authorization" in response["data"]
    assert "user" in response["data"]
