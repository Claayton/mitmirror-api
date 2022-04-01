"""Testes para a classe RegisterUser"""
from mitmirror.domain.models import User


def test_register(fake_user, user_repository_spy, register_user):
    """
    Testando o metodo register.
    Deve retornar um dicionario success: True, e data: Dados do usuario.
    """

    response = register_user.register(
        name=fake_user.name,
        email=fake_user.email,
        username=fake_user.username,
        password=fake_user.password_hash,
    )

    # Testando a entrada:
    assert user_repository_spy.insert_user_params["name"] == fake_user.name
    assert user_repository_spy.insert_user_params["email"] == fake_user.email
    assert user_repository_spy.insert_user_params["password_hash"] is not None

    # Testando a saida:
    assert response["success"] is True
    assert isinstance(response["data"], User)
