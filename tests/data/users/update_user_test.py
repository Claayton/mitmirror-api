"""Testes para a classe UpdateUser"""
from mitmirror.domain.models import User


def test_update(fake_user, user_repository_spy, update_user):
    """
    Testando o metodo update.
    Deve retornar um dicionario success: True, e data: Dados atualizados do usuario.
    """

    response = update_user.update(
        user_id=fake_user.id,
        name=f"{fake_user.name}2",
        email="mudeideemail@hotmail.com",
        username=f"{fake_user.username}vida_bandida",
        password="mudar123senhaforte",
        is_staff=True,
        is_active_user=True,
    )

    # Testando a entrada:
    assert user_repository_spy.update_user_params["user_id"] == fake_user.id
    assert user_repository_spy.update_user_params["name"] is not None

    # Testando a saida:
    assert response["success"] is True
    assert isinstance(response["data"], User)
