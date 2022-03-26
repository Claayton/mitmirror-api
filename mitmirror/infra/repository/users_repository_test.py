"""Testes para a classe UserRepository"""
from pytest import raises
from mitmirror.domain.models import User
from mitmirror.infra.repository.conftest import fake_user
from mitmirror.config import database_infos
from mitmirror.errors import DefaultError
from ..config import DataBaseConnectionHandler


database = DataBaseConnectionHandler(database_infos["connection_string"])


def test_insert_user(user_repository):
    """
    Testando o metodo insert_user.
    Deve retornar um objeto do tipo User com os mesmos parametros enviados.
    """

    response = user_repository.insert_user(
        name=fake_user["name"],
        email=fake_user["email"],
        username=fake_user["username"],
        password_hash=fake_user["password_hash"],
        secundary_id=fake_user["secundary_id"],
    )

    engine = database.get_engine()
    query_user = engine.execute(
        f"""SELECT * FROM users WHERE username='{fake_user["username"]}';"""
    ).fetchone()

    # Testando se as informacoes enviadas pelo metodo estao no db.
    assert isinstance(response, User)
    assert response.name == query_user.name
    assert response.email == query_user.email
    assert response.username == query_user.username
    assert response.password_hash == query_user.password_hash
    assert response.secundary_id == query_user.secundary_id


def test_insert_user_without_name_param(user_repository):
    """
    Testando o erro no metodo insert_user.
    Deixando de utilizar o parametro name.
    Deve retornar um erro do tipo DefaultError.
    """

    with raises(DefaultError) as error:

        user_repository.insert_user(
            name=None,
            email=fake_user["email"],
            username=fake_user["username"],
            password_hash=fake_user["password_hash"],
            secundary_id=fake_user["secundary_id"],
        )

    assert "error" in str(error.value)


def test_insert_user_without_email_param(user_repository):
    """
    Testando o erro no metodo insert_user.
    Deixando de utilizar o parametro email.
    Deve retornar um erro do tipo DefaultError.
    """

    with raises(DefaultError) as error:

        user_repository.insert_user(
            name=fake_user["name"],
            email=None,
            username=fake_user["username"],
            password_hash=fake_user["password_hash"],
            secundary_id=fake_user["secundary_id"],
        )

    assert "error" in str(error.value)


def test_insert_user_without_username_param(user_repository):
    """
    Testando o erro no metodo insert_user.
    Deixando de utilizar o parametro username.
    Deve retornar um erro do tipo DefaultError.
    """

    with raises(DefaultError) as error:

        user_repository.insert_user(
            name=fake_user["name"],
            email=fake_user["email"],
            username=None,
            password_hash=fake_user["password_hash"],
            secundary_id=fake_user["secundary_id"],
        )

    assert "error" in str(error.value)


def test_insert_user_without_password_hash_param(user_repository):
    """
    Testando o erro no metodo insert_user.
    Deixando de utilizar o parametro password_hash.
    Deve retornar um erro do tipo DefaultError.
    """

    with raises(DefaultError) as error:

        user_repository.insert_user(
            name=fake_user["name"],
            email=fake_user["email"],
            username=fake_user["username"],
            password_hash=None,
            secundary_id=fake_user["secundary_id"],
        )

    assert "error" in str(error.value)


def test_insert_user_without_secundary_id_param(user_repository):
    """
    Testando o erro no metodo insert_user.
    Deixando de utilizar o parametro secundary_id.
    Deve retornar um erro do tipo DefaultError.
    """

    with raises(DefaultError) as error:

        user_repository.insert_user(
            name=fake_user["name"],
            email=fake_user["email"],
            username=fake_user["username"],
            password_hash=fake_user["password_hash"],
            secundary_id=None,
        )

    assert "error" in str(error.value)
