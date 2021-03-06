"""Testes para a classe UserRepository"""  # pylint: disable=E0401
from pytest import raises, mark
from sqlmodel import select
from mitmirror.domain.models import User
from mitmirror.infra.entities import User as UserModel
from mitmirror.infra.config.database_config import get_session
from mitmirror.errors import DefaultError
from tests.conftest import user


def test_insert_user(fake_user, user_repository):
    """
    Testando o metodo insert_user.
    Deve retornar um objeto do tipo User com os mesmos parametros enviados.
    """

    response = user_repository.insert_user(
        name=fake_user.name,
        email=fake_user.email,
        username=fake_user.username,
        password_hash=fake_user.password_hash,
        secundary_id=fake_user.secundary_id,
    )

    with get_session() as session:
        query_user = session.exec(
            select(UserModel).where(UserModel.username == fake_user.username)
        ).one()

    # Testando se as informacoes enviadas pelo metodo estao no db.
    assert isinstance(response, User)
    assert response.name == query_user.name
    assert response.email == query_user.email
    assert response.username == query_user.username
    assert response.password_hash == query_user.password_hash
    assert response.secundary_id == query_user.secundary_id


@mark.parametrize(
    "name,email,username,password_hash",
    [
        (None, user.email, user.username, user.password_hash),
        (user.name, None, user.username, user.password_hash),
        (user.name, user.email, None, user.password_hash),
        (user.name, user.email, user.username, None),
    ],
)
def test_insert_user_missing_one_of_the_params(
    user_repository, name, email, username, password_hash
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
        )

    assert "error" in str(error.value)


@mark.parametrize(
    "user_id,username,email",
    [(user.id, None, None), (None, user.username, None), (None, None, user.email)],
)
def test_get_user(
    user_repository_with_one_user,
    fake_user,
    user_id,
    username,
    email,
):
    """
    Testando o metodo get_user, buscando pelo id, username e email.
    Deve retornar um objeto do tipo User com todas as infomacoes do usuario.
    """

    response = user_repository_with_one_user.get_user(
        user_id=user_id, username=username, email=email
    )
    with get_session() as session:
        query_user = session.exec(
            select(UserModel).where(UserModel.username == fake_user.username)
        ).one()

    # Testando se as informacoes enviadas pelo metodo estao no db.
    assert isinstance(response, User)
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


def test_get_users(user_repository_with_one_user, fake_user):
    """
    Testando o metodo get_users.
    Deve uma lista com todos os usuarios cadastrados.
    """

    with get_session() as session:
        new_user = UserModel(
            id=fake_user.id + 1,
            name=fake_user.name,
            email=f"{fake_user.email}2",
            username=f"{fake_user.username}2",
            password_hash=fake_user.password_hash,
            secundary_id=fake_user.secundary_id,
            is_staff=fake_user.is_staff,
            is_active_user=fake_user.is_active_user,
            date_joined=fake_user.date_joined,
            last_login=fake_user.last_login,
        )
        session.add(new_user)
        session.commit()

    response = user_repository_with_one_user.get_users()

    with get_session() as session:
        query_users = list(session.exec(select(UserModel)))

    # Testando se as informacoes enviadas pelo metodo estao no db.
    assert isinstance(response, list)
    assert response[0].id == query_users[0].id
    assert response[0].username == query_users[0].username
    assert response[0].email == query_users[0].email
    assert response[1].id == query_users[1].id
    assert response[1].username == query_users[1].username
    assert response[1].email == query_users[1].email


def test_get_users_with_no_results_found(user_repository):
    """
    Testando o metodo get_users, sem encontrar resultados.
    Deve retornar uma lista vazia.
    """

    response = user_repository.get_users()

    # Testando se o retorno e uma lista vazia.
    assert response == []


def test_update_user(user_repository_with_one_user, fake_user):
    """
    Testando o metodo update_user.
    Deve retornar um objeto do tipo User com os mesmos parametros enviados.
    """

    with get_session() as session:
        query_user = session.exec(
            select(UserModel).where(UserModel.id == fake_user.id)
        ).one()

    response = user_repository_with_one_user.update_user(
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
        (user.id, f"{user.username}", user.email),
        (user.id, user.username, f"{user.email}"),
    ],
)
def test_update_user_with_username_or_email_unavailable(
    user_repository_with_one_user,
    fake_user,
    user_id,
    username,
    email,
):
    """
    Testando o metodo update_user onde novo nome de usuario ou email esta indisponivel.
    Deve retornar um DefaultError.
    """

    with get_session() as session:
        new_user = UserModel(
            id=fake_user.id + 1,
            name=fake_user.name,
            email=f"{fake_user.email}2",
            username=f"{fake_user.username}2",
            password_hash=fake_user.password_hash,
            secundary_id=fake_user.secundary_id,
            is_staff=fake_user.is_staff,
            is_active_user=fake_user.is_active_user,
            date_joined=fake_user.date_joined,
            last_login=fake_user.last_login,
        )
        session.add(new_user)
        session.commit()

    with raises(DefaultError) as error:

        user_repository_with_one_user.update_user(
            user_id=user_id,
            name=f"{fake_user.name}2",
            email=email,
            username=username,
            is_staff=True,
            is_active_user=True,
        )

    assert "indisponivel" in str(error.value)


def test_delete_user(user_repository_with_one_user, fake_user):
    """
    Testando o metodo delete_user.
    Deve retornar um objeto do tipo User com as informacoes do usuario deletado.
    """

    response = user_repository_with_one_user.delete_user(fake_user.id)

    with get_session() as session:
        query_user = session.exec(
            select(UserModel).where(UserModel.username == fake_user.username)
        ).all()

    assert isinstance(response, User)
    assert response.id == fake_user.id
    assert not query_user


def test_delete_user_with_no_results_found(user_repository, fake_user):
    """
    Testando o metodo update_user onde o id do usuario nao e encontrado no db.
    Deve retornar um DefaultError.
    """
    with raises(DefaultError) as error:

        user_repository.delete_user(user_id=fake_user.id)

    assert "Usuario nao encontrado!" in str(error.value)
