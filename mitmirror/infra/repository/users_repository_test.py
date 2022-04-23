"""Testes para a classe UserRepository"""
from pytest import raises, mark
from faker import Faker
from mitmirror.domain.models import User
from mitmirror.infra.entities import User as UserModel
from mitmirror.config import CONNECTION_STRING
from mitmirror.errors import DefaultError
from .conftest import user
from ..config import DataBaseConnectionHandler


fake = Faker()
database = DataBaseConnectionHandler(CONNECTION_STRING)


def test_insert_user(user_repository_with_delete_user, fake_user):
    """
    Testando o metodo insert_user.
    Deve retornar um objeto do tipo User com os mesmos parametros enviados.
    """

    response = user_repository_with_delete_user.insert_user(
        name=fake_user.name,
        email=fake_user.email,
        username=fake_user.username,
        password_hash=fake_user.password_hash,
        secundary_id=fake_user.secundary_id,
    )

    engine = database.get_engine()
    query_user = engine.execute(
        f"""SELECT * FROM users WHERE username='{fake_user.username}';"""
    ).fetchone()

    # Testando se as informacoes enviadas pelo metodo estao no db.
    assert isinstance(response, User)
    assert response.name == query_user.name
    assert response.email == query_user.email
    assert response.username == query_user.username
    assert response.password_hash == query_user.password_hash
    assert response.secundary_id == query_user.secundary_id


@mark.parametrize(
    "name,email,username,password_hash,secundary_id",
    [
        (None, user.email, user.username, user.password_hash, user.secundary_id),
        (user.name, None, user.username, user.password_hash, user.secundary_id),
        (user.name, user.email, None, user.password_hash, user.secundary_id),
        (user.name, user.email, user.username, None, user.secundary_id),
        (user.name, user.email, user.username, user.password_hash, None),
    ],
)
def test_insert_user_missing_one_of_the_params(
    user_repository, name, email, username, password_hash, secundary_id
):
    """
    Testando o erro no metodo insert_user.
    Deixando de utilizar um dos parametros.
    Deve retornar um erro do tipo DefaultError.
    """

    with raises(DefaultError) as error:

        user_repository.insert_user(
            name=name,
            email=email,
            username=username,
            password_hash=password_hash,
            secundary_id=secundary_id,
        )

    assert "error" in str(error.value)


@mark.parametrize(
    "user_id,username,email",
    [(user.id, None, None), (None, user.username, None), (None, None, user.email)],
)
def test_get_user(
    user_repository_with_one_user_registered_and_delete_user,
    fake_user,
    user_id,
    username,
    email,
):
    """
    Testando o metodo get_user, buscando pelo id, username e email.
    Deve retornar um objeto do tipo User com todas as infomacoes do usuario.
    """

    response = user_repository_with_one_user_registered_and_delete_user.get_user(
        user_id=user_id, username=username, email=email
    )

    engine = database.get_engine()
    query_user = engine.execute(
        f"""SELECT * FROM users WHERE username='{fake_user.username}';"""
    ).fetchone()

    # Testando se as informacoes enviadas pelo metodo estao no db.
    assert isinstance(response, UserModel)
    assert response.name == query_user.name
    assert response.email == query_user.email
    assert response.username == query_user.username
    assert response.password_hash == query_user.password_hash
    assert response.secundary_id == query_user.secundary_id


def test_get_user_with_no_results_found(user_repository, fake_user):
    """
    Testando o metodo get_user, sem encontrar resultados.
    Deve retornar uma lista vazia.
    """

    response = user_repository.get_user(
        user_id=fake_user.id, username=fake_user.username, email=fake_user.email
    )
    engine = database.get_engine()
    engine.execute(
        f"""SELECT * FROM users WHERE username='{fake_user.username}';"""
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


def test_get_users(user_repository_with_two_users_registered_and_delete_user):
    """
    Testando o metodo get_usesr.
    Deve uma lista com todos os usuarios cadastrados.
    """

    response = user_repository_with_two_users_registered_and_delete_user.get_users()
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


def test_update_user(
    user_repository_with_one_user_registered_and_delete_user, fake_user
):
    """
    Testando o metodo update_user.
    Deve retornar um objeto do tipo User com os mesmos parametros enviados.
    """

    engine = database.get_engine()
    query_user = engine.execute(
        f"""SELECT * FROM users WHERE id='{fake_user.id}';"""
    ).fetchone()

    response = user_repository_with_one_user_registered_and_delete_user.update_user(
        user_id=fake_user.id,
        name=f"{fake_user.name}2",
        email=f"{fake_user.email}2",
        username=f"{fake_user.username}2",
        is_staff=True,
        is_active_user=True,
    )

    # Testando se as informacoes enviadas pelo metodo estao no db.
    assert isinstance(response, User)
    assert response.id == query_user.id
    assert response.name != query_user.name
    assert response.email != query_user.email
    assert response.username != query_user.username


def test_update_user_with_no_results_found(user_repository, fake_user):
    """
    Testando o metodo update_user onde o id do usuario nao e encontrado no db.
    Deve retornar um DefaultError.
    """
    with raises(DefaultError) as error:

        user_repository.update_user(
            user_id=fake_user.id,
            name=f"{fake_user.name}2",
            email=f"{fake_user.email}2",
            username=f"{fake_user.username}2",
            is_staff=True,
            is_active_user=True,
        )
    assert "Usuario nao encontrado!" in str(error.value)


@mark.parametrize(
    "user_id,username,email",
    [
        (user.id, f"{user.username}1", user.email),
        (user.id, user.username, f"{user.email}1"),
    ],
)
def test_update_user_with_username_or_email_unavailable(
    user_repository_with_two_users_registered_and_delete_user,
    fake_user,
    user_id,
    username,
    email,
):
    """
    Testando o metodo update_user onde novo nome de usuario ou email esta indisponivel.
    Deve retornar um DefaultError.
    """
    with raises(DefaultError) as error:

        user_repository_with_two_users_registered_and_delete_user.update_user(
            user_id=user_id,
            name=f"{fake_user.name}2",
            email=email,
            username=username,
            is_staff=True,
            is_active_user=True,
        )

    assert "indisponivel" in str(error.value)


def test_delete_user(
    user_repository_with_one_user_registered_and_delete_user, fake_user
):
    """
    Testando o metodo delete_user.
    Deve retornar um objeto do tipo User com as informacoes do usuario deletado.
    """

    response = user_repository_with_one_user_registered_and_delete_user.delete_user(
        fake_user.id
    )

    engine = database.get_engine()
    query_user = engine.execute(
        f"""SELECT * FROM users WHERE id='{fake_user.id}';"""
    ).fetchone()

    assert isinstance(response, User)
    assert response.id == fake_user.id
    assert query_user is None


def test_delete_user_with_no_results_found(user_repository, fake_user):
    """
    Testando o metodo update_user onde o id do usuario nao e encontrado no db.
    Deve retornar um DefaultError.
    """
    with raises(DefaultError) as error:

        user_repository.delete_user(user_id=fake_user.id)

    assert "Usuario nao encontrado!" in str(error.value)
