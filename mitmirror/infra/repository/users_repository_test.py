"""Testes para a classe UserRepository"""
from pytest import raises
from mitmirror.domain.models import User
from mitmirror.infra.entities import User as UserModel
from mitmirror.config import database_infos
from mitmirror.errors import DefaultError
from ..config import DataBaseConnectionHandler


database = DataBaseConnectionHandler(database_infos["connection_string"])


def test_insert_user(user_repository_with_delete_user, mock_user):
    """
    Testando o metodo insert_user.
    Deve retornar um objeto do tipo User com os mesmos parametros enviados.
    """

    response = user_repository_with_delete_user.insert_user(
        name=mock_user["name"],
        email=mock_user["email"],
        username=mock_user["username"],
        password_hash=mock_user["password_hash"],
        secundary_id=mock_user["secundary_id"],
    )

    engine = database.get_engine()
    query_user = engine.execute(
        f"""SELECT * FROM users WHERE username='{mock_user["username"]}';"""
    ).fetchone()

    # Testando se as informacoes enviadas pelo metodo estao no db.
    assert isinstance(response, User)
    assert response.name == query_user.name
    assert response.email == query_user.email
    assert response.username == query_user.username
    assert response.password_hash == query_user.password_hash
    assert response.secundary_id == query_user.secundary_id


def test_insert_user_without_name_param(user_repository, mock_user):
    """
    Testando o erro no metodo insert_user.
    Deixando de utilizar o parametro name.
    Deve retornar um erro do tipo DefaultError.
    """

    with raises(DefaultError) as error:

        user_repository.insert_user(
            name=None,
            email=mock_user["email"],
            username=mock_user["username"],
            password_hash=mock_user["password_hash"],
            secundary_id=mock_user["secundary_id"],
        )

    assert "error" in str(error.value)


def test_insert_user_without_email_param(user_repository, mock_user):
    """
    Testando o erro no metodo insert_user.
    Deixando de utilizar o parametro email.
    Deve retornar um erro do tipo DefaultError.
    """

    with raises(DefaultError) as error:

        user_repository.insert_user(
            name=mock_user["name"],
            email=None,
            username=mock_user["username"],
            password_hash=mock_user["password_hash"],
            secundary_id=mock_user["secundary_id"],
        )

    assert "error" in str(error.value)


def test_insert_user_without_username_param(user_repository, mock_user):
    """
    Testando o erro no metodo insert_user.
    Deixando de utilizar o parametro username.
    Deve retornar um erro do tipo DefaultError.
    """

    with raises(DefaultError) as error:

        user_repository.insert_user(
            name=mock_user["name"],
            email=mock_user["email"],
            username=None,
            password_hash=mock_user["password_hash"],
            secundary_id=mock_user["secundary_id"],
        )

    assert "error" in str(error.value)


def test_insert_user_without_password_hash_param(user_repository, mock_user):
    """
    Testando o erro no metodo insert_user.
    Deixando de utilizar o parametro password_hash.
    Deve retornar um erro do tipo DefaultError.
    """

    with raises(DefaultError) as error:

        user_repository.insert_user(
            name=mock_user["name"],
            email=mock_user["email"],
            username=mock_user["username"],
            password_hash=None,
            secundary_id=mock_user["secundary_id"],
        )

    assert "error" in str(error.value)


def test_insert_user_without_secundary_id_param(user_repository, mock_user):
    """
    Testando o erro no metodo insert_user.
    Deixando de utilizar o parametro secundary_id.
    Deve retornar um erro do tipo DefaultError.
    """

    with raises(DefaultError) as error:

        user_repository.insert_user(
            name=mock_user["name"],
            email=mock_user["email"],
            username=mock_user["username"],
            password_hash=mock_user["password_hash"],
            secundary_id=None,
        )

    assert "error" in str(error.value)


def test_get_user_by_id(user_repository_with_one_user_registered, mock_user):
    """
    Testando o metodo get_user, buscando pelo id do usuario.
    Deve retornar um objeto do tipo User com todas as infomacoes do usuario.
    """

    response = user_repository_with_one_user_registered.get_user(
        user_id=mock_user["user_id"]
    )
    engine = database.get_engine()
    query_user = engine.execute(
        f"""SELECT * FROM users WHERE username='{mock_user["username"]}';"""
    ).fetchone()

    # Testando se as informacoes enviadas pelo metodo estao no db.
    assert isinstance(response, UserModel)
    assert response.name == query_user.name
    assert response.email == query_user.email
    assert response.username == query_user.username
    assert response.password_hash == query_user.password_hash
    assert response.secundary_id == query_user.secundary_id


def test_get_user_username(user_repository_with_one_user_registered, mock_user):
    """
    Testando o metodo get_user, buscando pelo username do usuario.
    Deve retornar um objeto do tipo User com todas as infomacoes do usuario.
    """

    response = user_repository_with_one_user_registered.get_user(
        username=mock_user["username"]
    )
    engine = database.get_engine()
    query_user = engine.execute(
        f"""SELECT * FROM users WHERE username='{mock_user["username"]}';"""
    ).fetchone()

    # Testando se as informacoes enviadas pelo metodo estao no db.
    assert isinstance(response, UserModel)
    assert response.name == query_user.name
    assert response.email == query_user.email
    assert response.username == query_user.username
    assert response.password_hash == query_user.password_hash
    assert response.secundary_id == query_user.secundary_id


def test_get_user_email(user_repository_with_one_user_registered, mock_user):
    """
    Testando o metodo get_user, buscando pelo email do usuario.
    Deve retornar um objeto do tipo User com todas as infomacoes do usuario.
    """

    response = user_repository_with_one_user_registered.get_user(
        email=mock_user["email"]
    )
    engine = database.get_engine()
    query_user = engine.execute(
        f"""SELECT * FROM users WHERE username='{mock_user["username"]}';"""
    ).fetchone()

    # Testando se as informacoes enviadas pelo metodo estao no db.
    assert isinstance(response, UserModel)
    assert response.name == query_user.name
    assert response.email == query_user.email
    assert response.username == query_user.username
    assert response.password_hash == query_user.password_hash
    assert response.secundary_id == query_user.secundary_id


def test_get_user_with_no_results_found(user_repository, mock_user):
    """
    Testando o metodo get_user, sem encontrar resultados.
    Deve retornar uma lista vazia.
    """

    response = user_repository.get_user(
        user_id=mock_user["user_id"],
        username=mock_user["username"],
        email=mock_user["email"],
    )
    engine = database.get_engine()
    engine.execute(
        f"""SELECT * FROM users WHERE username='{mock_user["username"]}';"""
    ).fetchone()

    # Testando se o retorno e uma lista vazia.
    assert response == []


def test_get_user_without_params(user_repository):
    """
    Testando o metodo get_user, sem utilizar nenhum parametro.
    Deve retornar um erro do tipo DefaultError.
    """

    with raises(Exception) as error:

        user_repository.get_user(user_id=None, username=None, email=None)

    assert "error" in str(error.value)


def test_get_users(user_repository_with_two_users_registered, mock_user):
    """
    Testando o metodo get_usesr.
    Deve uma lista com todos os usuarios cadastrados.
    """

    response = user_repository_with_two_users_registered.get_users()
    engine = database.get_engine()
    query_user = engine.execute("SELECT * FROM users;").fetchall()

    # Testando se as informacoes enviadas pelo metodo estao no db.
    assert isinstance(response, list)
    assert response[0].id == query_user[0].id
    assert response[0].username == query_user[0].username
    assert response[0].email == query_user[0].email
    assert response[1].id == query_user[1].id
    assert response[1].username == query_user[1].username
    assert response[1].email == query_user[1].email


def test_get_users_with_no_results_found(user_repository):
    """
    Testando o metodo get_users, sem encontrar resultados.
    Deve retornar uma lista vazia.
    """

    response = user_repository.get_users()

    # Testando se o retorno e uma lista vazia.
    assert response == []
