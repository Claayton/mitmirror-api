"""Testes para a classe UserRepository"""
from mitmirror.domain.models import User
from mitmirror.infra.repository.conftest import fake_user


def test_insert_user(user_repository):
    """
    Testando o metodo insert_user.
    """

    response = user_repository.insert_user(
        name=fake_user["name"],
        email=fake_user["email"],
        username=fake_user["username"],
        password_hash=fake_user["password_hash"],
        secundary_id=fake_user["secundary_id"],
    )

    assert isinstance(response, User)
    assert response.name == fake_user["name"]
    assert response.email == fake_user["email"]
    assert response.username == fake_user["username"]
    assert response.password_hash == fake_user["password_hash"]
    assert response.secundary_id == fake_user["secundary_id"]
