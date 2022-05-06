"""Diretorio de manipulaçao de dados para a tabela User"""
from typing import Type, List
from datetime import datetime
from sqlmodel import select
from sqlalchemy.exc import NoResultFound
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.errors import DefaultError
from mitmirror.infra.config import get_session
from mitmirror.infra.entities import User as UserModel
from mitmirror.domain.models import User


class UserRepository(UserRepositoryInterface):
    """Manipulacao de dados da tabela User"""

    def __init__(self) -> None:

        self.__session = get_session()

    def insert_user(
        self,
        name: str,
        email: str,
        username: str,
        password_hash: str,
        secundary_id: int = 0,  # Configurar futuramente
        is_staff: bool = False,  # Configurar futuramente
        is_active_user: bool = False,  # Configurar futuramente
        date_joined: Type[datetime] = datetime.today(),  # Configurar futuramente
        last_login: Type[datetime] = datetime.today(),
    ) -> User:
        """
        Realiza a inserçao de um novo usuario na tabela User
        :param name: Nome do usuario.
        :param email: Email do usuario.
        :param username: Nome de usuario que deve ser unico para cada um.
        :param password_hash: Hash da senha do usuario.
        :param secundary_id: Numero secundario de identificacao do usuario.
        :param is_staff: Se o usuario e ou nao o admin sistema.
        :param is_active_user: Se o usuario e esta ativo no sistema.
        :param date_joined: Data de cadastro do usuario no sistema.
        :param last_login: Data do ultimo login do usuario no sistema.
        :return: O usuario cadastrado e seus dados.
        """

        with self.__session as session:

            try:

                new_user = UserModel(**locals())

                session.add(new_user)
                session.commit()
                session.refresh(new_user)

                return User(**new_user.dict())

            except Exception as error:

                session.rollback()
                raise DefaultError(
                    type_error=422, message="Parametros invalidos!, error"
                ) from error

    def get_user(
        self, user_id: int = None, username: str = None, email: str = None
    ) -> User:
        """
        Realiza a busca de um usuario cadastrado no banco de dados.
        Os dados seram buscados por ID do usuario, username ou email.
        :param user_id: ID do usuario.
        :param username: Nome de usuario, que deve ser unico no sistema.
        :param emil: Email do usuario.
        :return: Um usuario e seus dados.
        """

        try:

            query_user = None

            if user_id:

                with self.__session as session:

                    query_user = session.exec(
                        select(UserModel).where(UserModel.id == user_id)
                    ).one()

            elif username:

                with self.__session as session:

                    query_user = session.exec(
                        select(UserModel).where(UserModel.username == username)
                    ).one()

            elif email:

                with self.__session as session:

                    query_user = session.exec(
                        select(UserModel).where(UserModel.email == email)
                    ).one()

            else:

                raise DefaultError(
                    message="""
                    E necessario o user_id, username ou email, para encontrar o usuario!, error""",
                    type_error=400,
                )

            return User(**query_user.dict())

        except NoResultFound:

            return []

        except Exception as error:  # pylint: disable=W0703

            raise DefaultError(message=str(error)) from error

    def get_users(self) -> List[User]:
        """
        Realiza uma busca por todos os usuarios cadastrados no sistema.
        :return: Uma Lista com todos os usuarios e seus dados.
        """

        try:

            with self.__session as session:

                query_data = session.exec(select(UserModel)).all()

            response = [User(**data.dict()) for data in query_data]

            return response

        except NoResultFound:

            return []

        except Exception as error:  # pylint: disable=W0703

            raise DefaultError(message=str(error)) from error

    def update_user(
        self,
        user_id: int,
        name: str = None,
        email: str = None,
        username: str = None,
        password_hash: str = None,
        secundary_id: int = None,
        is_staff: bool = None,
        is_active_user: bool = None,
        date_joined: Type[datetime] = None,
        last_login: Type[datetime] = None,
    ) -> User:
        """
        Realiza a atualização de dados de um usuario cadastrado na tabela User.
        :param user_id: ID do usuario, necessario para encontrar-lo no sistema.
        :param name: Nome do usuario.
        :param email: Email do usuario.
        :param username: Nome de usuario que deve ser unico para cada um.
        :param password_hash: Hash da senha do usuario.
        :param secundary_id: Numero secundario de identificacao do usuario.
        :param is_staff: Se o usuario e ou nao o admin sistema.
        :param is_active_user: Se o usuario e esta ativo no sistema.
        :param date_joined: Data de cadastro do usuario no sistema.
        :param last_login: Data do ultimo login do usuario no sistema.
        :return: O usuario com seus dados atualizados.
        """

        with self.__session as session:

            try:

                user = session.exec(
                    select(UserModel).where(UserModel.id == user_id)
                ).one()

                if not user:

                    raise NoResultFound

            except NoResultFound as error:

                raise DefaultError(
                    message="Usuario nao encontrado!", type_error=404
                ) from error

            try:

                username_exist = session.exec(
                    select(UserModel).where(UserModel.username == username)
                ).one()

                if username_exist and user.name != name:

                    raise DefaultError(
                        message="Nome de usuario indisponivel", type_error=400
                    )

            except NoResultFound:

                pass

            except Exception as error:

                session.rollback()
                raise DefaultError(message=str(error)) from error

            try:

                email_exist = session.exec(
                    select(UserModel).where(UserModel.email == email)
                ).one()

                if email_exist and user.email != email:

                    raise DefaultError(message="Email indisponivel", type_error=400)

            except NoResultFound:

                pass

            except Exception as error:

                session.rollback()
                raise DefaultError(message=str(error)) from error

            try:

                if name is not None:
                    user.name = name
                if email is not None:
                    user.email = email
                if username is not None:
                    user.username = username
                if password_hash is not None:
                    user.password_hash = password_hash
                if secundary_id is not None:
                    user.secundary_id = secundary_id
                if is_staff is not None:
                    user.is_staff = is_staff
                if is_active_user is not None:
                    user.is_active_user = is_active_user
                if date_joined is not None:
                    user.date_joined = date_joined
                if last_login is not None:
                    user.last_login = last_login

                session.commit()
                session.refresh(user)

                return User(**user.dict())

            except Exception as error:  # pylint: disable=W0703

                session.rollback()
                raise DefaultError(message=str(error)) from error

    def delete_user(self, user_id: int) -> User:
        """
        Realiza a exclusao um usuario cadastrado no sistema.
        :param uesr_id: ID do usuario cadastrado.
        :return: O usuario deletado e seus dados.
        """

        with self.__session as session:

            try:

                user = session.exec(
                    select(UserModel).where(UserModel.id == user_id)
                ).one()

                if not user:

                    raise NoResultFound

            except NoResultFound as error:

                raise DefaultError(
                    message="Usuario nao encontrado!", type_error=404
                ) from error

            try:

                session.delete(user)
                session.commit()

                return User(**user.dict())

            except Exception as error:

                session.rollback()
                raise DefaultError(message=str(error)) from error
