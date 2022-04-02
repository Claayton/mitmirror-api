"""Testes para a classe PasswordHash"""
from faker import Faker
from .password_hash import PasswordHash

fake = Faker()


def test_hash():
    """Testando o metodo hash"""

    password = "estaeumasenhadeteste@123"

    hashed_password = PasswordHash.hash(password)

    assert hashed_password != password
    assert isinstance(hashed_password, bytes)


def test_verify():
    """Testando o metodo verify"""

    password = "estaeumasenhadeteste@123"
    password_hashed = b"$2b$12$gS5XWVaQqbmIkWHeNTsIWO/qmQHMUeObOU8bT6nYjbi47NbCH2QG."

    is_hashed = PasswordHash.verify(password, password_hashed)

    assert is_hashed is True
