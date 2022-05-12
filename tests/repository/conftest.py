"""Arquivo para fixtures"""  # pylint: disable=E0401
from pytest import fixture
from mitmirror.infra.repository import UserRepository
from mitmirror.infra.entities import User as UserModel
from mitmirror.infra.config.database_config import get_session


@fixture
def user_repository():  # pylint: disable=W0621
    """Fixture para montar o objeto UserRepository"""

    return UserRepository()


@fixture
def user_repository_with_one_user(user_repository, fake_user):  # pylint: disable=W0621
    """
    Fixture para montar o objeto UserRepository com usuario registrado,
    E deleta o usuario no final do teste.
    """

    with get_session() as session:
        new_user = UserModel(
            id=fake_user.id,
            name=fake_user.name,
            email=fake_user.email,
            username=fake_user.username,
            password_hash=fake_user.password_hash,
            secundary_id=fake_user.secundary_id,
            is_staff=fake_user.is_staff,
            is_active_user=fake_user.is_active_user,
            date_joined=fake_user.date_joined,
            last_login=fake_user.last_login,
        )
        session.add(new_user)
        session.commit()

    yield user_repository
