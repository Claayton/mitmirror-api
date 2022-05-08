"""Testes para a classe RegisterUser"""  # pylint: disable=E0401
from pytest import raises, mark
from mitmirror.domain.models import User
from mitmirror.errors import DefaultError
from tests.conftest import user


def test_register(fake_user, user_repository_spy, register_user):
    """
    Testando o metodo register.
    Deve retornar um dicionario success: True, e data: Dados do usuario.
    """

    response = register_user.register(
        name=fake_user.name,
        email=fake_user.email,
        username=fake_user.username,
        password=fake_user.password,
    )

    # Testando a entrada:
    assert user_repository_spy.insert_user_params["name"] == fake_user.name
    assert user_repository_spy.insert_user_params["email"] == fake_user.email
    assert user_repository_spy.insert_user_params["password_hash"] is not None

    # Testando a saida:
    assert response["success"] is True
    assert isinstance(response["data"], User)


@mark.parametrize(
    "name,email,username,password",
    [
        (user.id, user.email, user.username, user.password),
        (user.name, user.id, user.username, user.password),
        (user.name, user.email, user.id, user.password),
        (user.name, user.email, user.username, user.id),
    ],
)
def test_register_with_invalid_params(register_user, name, email, username, password):
    """
    Testando o erro no metodo register.
    Utilizando parametros invalidos.
    Deve retornar um DefaultError.
    """

    with raises(DefaultError) as error:

        register_user.register(
            name=name,
            email=email,
            username=username,
            password=password,
        )

    assert "Esta requisicao necessita dos parametros:" in str(error.value)
