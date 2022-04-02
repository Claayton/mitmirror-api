"""Testes para a classe GetUser"""
from pytest import raises
from mitmirror.domain.models import User
from mitmirror.errors import DefaultError


def test_by_id(get_user_with_spy, user_repository_spy, fake_user):
    """
    Testando o metodo by_id.
    Deve retornar uma mensagem de sucesso, e um usuario.
    """

    response = get_user_with_spy.by_id(user_id=fake_user.id)

    # Testando a entrada:
    assert user_repository_spy.get_user_params["user_id"] == fake_user.id

    # Testando a saida:
    assert response["success"] is True
    assert isinstance(response["data"], User)


def test_by_id_error(get_user_with_spy, user_repository_spy, fake_user):
    """
    Testando o erro metodo by_id.
    Utilizando um malor invalido para o parametro user_id.
    Deve retornar uma mensagem negativa de sucesso e None.
    """

    response = get_user_with_spy.by_id(user_id=fake_user.name)

    # Testando a entrada:
    assert not user_repository_spy.get_user_params

    # Testando a saida:
    assert response["success"] is False
    assert response["data"] is None


def test_by_id_with_no_result_found(get_user, fake_user):
    """
    Testando o erro no metodo by_id.
    Onde nao e encontrado nenhum usuario com o ID recebido
    Deve retornar um DefaultError.
    """

    with raises(DefaultError) as error:

        get_user.by_id(user_id=fake_user.id)

    assert "Usuario nao encontrado!" in str(error.value)


def test_by_email(get_user_with_spy, user_repository_spy, fake_user):
    """
    Testando o metodo by_email.
    Deve retornar uma mensagem de sucesso, e um usuario.
    """

    response = get_user_with_spy.by_email(email=fake_user.email)

    # Testando a entrada:
    assert user_repository_spy.get_user_params["email"] == fake_user.email

    # Testando a saida:
    assert response["success"] is True
    assert isinstance(response["data"], User)


def test_by_email_error(get_user_with_spy, user_repository_spy, fake_user):
    """
    Testando o erro metodo by_email.
    Utilizando um valor invalido para o parametro email.
    Deve retornar uma mensagem negativa de sucesso e None.
    """

    response = get_user_with_spy.by_email(email=fake_user.id)

    # Testando a entrada:
    assert not user_repository_spy.get_user_params

    # Testando a saida:
    assert response["success"] is False
    assert response["data"] is None


def test_by_email_with_no_result_found(get_user, fake_user):
    """
    Testando o erro no metodo by_email.
    Onde nao e encontrado nenhum usuario com o email recebido
    Deve retornar um DefaultError.
    """

    with raises(DefaultError) as error:

        get_user.by_email(email=fake_user.email)

    assert "Usuario nao encontrado!" in str(error.value)


def test_by_username(get_user_with_spy, user_repository_spy, fake_user):
    """
    Testando o metodo by_username.
    Deve retornar uma mensagem de sucesso, e um usuario.
    """

    response = get_user_with_spy.by_username(username=fake_user.username)

    # Testando a entrada:
    assert user_repository_spy.get_user_params["username"] == fake_user.username

    # Testando a saida:
    assert response["success"] is True
    assert isinstance(response["data"], User)


def test_by_username_error(get_user_with_spy, user_repository_spy, fake_user):
    """
    Testando o erro metodo by_username.
    Utilizando um valor invalido para o parametro username.
    Deve retornar uma mensagem negativa de sucesso e None.
    """

    response = get_user_with_spy.by_username(username=fake_user.id)

    # Testando a entrada:
    assert not user_repository_spy.get_user_params

    # Testando a saida:
    assert response["success"] is False
    assert response["data"] is None


def test_by_username_with_no_result_found(get_user, fake_user):
    """
    Testando o erro no metodo by_username.
    Onde nao e encontrado nenhum usuario com o username recebido
    Deve retornar um DefaultError.
    """

    with raises(DefaultError) as error:

        get_user.by_username(username=fake_user.username)

    assert "Usuario nao encontrado!" in str(error.value)
