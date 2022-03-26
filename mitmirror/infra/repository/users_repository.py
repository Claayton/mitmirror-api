"""Diretorio de manipulaçao de dados para a tabela User"""
from typing import Type, List
from datetime import datetime
from sqlalchemy.exc import NoResultFound
from mitmirror.data.interfaces import UserRepositoryInterface
from mitmirror.errors import DefaultError
from mitmirror.infra.config import DataBaseConnectionHandler
from mitmirror.infra.entities import User as UserModel
from mitmirror.domain.models import User


class UserRepository(UserRepositoryInterface):
    """Manipulacao de dados da tabela User"""

    def __init__(self, connection_string: str) -> None:

        self.__connection_string = connection_string

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

                with DataBaseConnectionHandler(self.__connection_string) as database:

                    query_user = (
                        database.session.query(UserModel).filter_by(id=user_id).one()
                    )

            elif username:

                with DataBaseConnectionHandler(self.__connection_string) as database:

                    query_user = (
                        database.session.query(UserModel)
                        .filter_by(username=username)
                        .one()
                    )

            elif email:

                with DataBaseConnectionHandler(self.__connection_string) as database:

                    query_user = (
                        database.session.query(UserModel).filter_by(email=email).one()
                    )

            else:

                raise DefaultError(
                    message="E necessario o user_id, username ou email, para encontrar o usuario!",
                    type_error=400,
                )

            return query_user

        except NoResultFound:

            return []

        except Exception as error:

            database.session.rollback()
            raise DefaultError(message=str(error)) from error

        finally:

            database.session.close()

    def get_users(self) -> List[User]:
        """
        Realiza uma busca por todos os usuarios cadastrados no sistema.
        :return: Uma Lista com todos os usuarios e seus dados.
        """

        try:

            with DataBaseConnectionHandler(self.__connection_string) as database:

                query_data = database.session.query(UserModel).all()

            return query_data

        except NoResultFound:

            return []

        except Exception as error:

            database.session.rollback()
            raise DefaultError(message=str(error)) from error

        finally:

            database.session.close()

    def insert_user(
        self,
        name: str,
        email: str,
        username: str,
        password_hash: str,
        secondary_id: int = 0,  # Configurar futuramente
        is_staff: bool = False,  # Configurar futuramente
        is_active: bool = False,  # Configurar futuramente
        date_joined: Type[datetime] = None,
        last_login: Type[datetime] = datetime.today(),
    ) -> User:
        """
        Realiza a inserçao de um novo usuario na tabela User
        :param name: Nome do usuario.
        :param email: Email do usuario.
        :param username: Nome de usuario que deve ser unico para cada um.
        :param password_hash: Hash da senha do usuario.
        :param secondary_id: Numero secundario de identificacao do usuario.
        :param is_staff: Se o usuario e ou nao o admin sistema.
        :param is_active: Se o usuario e esta ativo no sistema.
        :param date_joined: Data de cadastro do usuario no sistema.
        :param kast_login: Data do ultimo login do usuario no sistema.
        :return: O usuario cadastrado e seus dados.
        """

        with DataBaseConnectionHandler(self.__connection_string) as database:

            try:

                new_user = UserModel(
                    name=name,
                    email=email,
                    username=username,
                    password_hash=password_hash,
                    secondary_id=secondary_id,
                    is_staff=is_staff,
                    is_active=is_active,
                    date_joined=date_joined,
                    last_login=last_login,
                )
                database.session.add(new_user)
                database.session.commit()

                return User(
                    id=new_user.id,
                    name=new_user.name,
                    email=new_user.email,
                    username=new_user.username,
                    password_hash=new_user.password_hash,
                    secondary_id=new_user.secondary_id,
                    is_staff=new_user.is_staff,
                    is_active=new_user.is_active,
                    date_joined=new_user.date_joined,
                    last_login=new_user.last_login,
                )

            except Exception as error:

                database.session.rollback()
                raise DefaultError(message=str(error)) from error

            finally:

                database.session.close()

    def update_user(
        self,
        user_id: int,
        name: str = None,
        email: str = None,
        username: str = None,
        password_hash: str = None,
        secondary_id: int = None,
        is_staff: bool = None,
        is_active: bool = None,
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
        :param secondary_id: Numero secundario de identificacao do usuario.
        :param is_staff: Se o usuario e ou nao o admin sistema.
        :param is_active: Se o usuario e esta ativo no sistema.
        :param date_joined: Data de cadastro do usuario no sistema.
        :param kast_login: Data do ultimo login do usuario no sistema.
        :return: O usuario com seus dados atualizados.
        """

        with DataBaseConnectionHandler(self.__connection_string) as database:

            try:

                user = (
                    database.session.query(UserModel).filter_by(user_id=user_id).one()
                )
                username_exist = (
                    database.session.query(UserModel).filter_by(username=username).one()
                )
                email_exist = (
                    database.session.query(UserModel).filter_by(email=email).one()
                )

            except NoResultFound:

                pass

            except Exception as error:

                raise DefaultError(message=str(error)) from error

            try:

                if not user:

                    raise DefaultError(
                        message="Usuario nao encontrado!", type_error=404
                    )

                if username_exist and user.username != name:

                    raise DefaultError(message="Nome indisponivel", type_error=400)

                if email_exist and user.email != email:

                    raise DefaultError(message="Email indisponivel", type_error=400)

                user.name = name
                if email:
                    user.email = email
                if username:
                    user.username = username
                user.password_hash = password_hash
                user.secondary_id = secondary_id
                user.is_staff = is_staff
                user.is_active = is_active
                user.date_joined = date_joined
                user.last_login = last_login

                database.session.commit()

                return User(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    username=user.username,
                    password_hash=user.password_hash,
                    secondary_id=user.secondary_id,
                    is_staff=user.is_staff,
                    is_active=user.is_active,
                    date_joined=user.date_joined,
                    last_login=user.last_login,
                )

            except Exception as error:

                database.session.rollback()
                raise DefaultError(message=str(error)) from error

            finally:

                database.session.close()

    def delete_user(self, user_id: int) -> User:
        """
        Realiza a exclusao um usuario cadastrado no sistema.
        :param uesr_id: ID do usuario cadastrado.
        :return: O usuario deletado e seus dados.
        """

        with DataBaseConnectionHandler(self.__connection_string) as database:

            try:

                user = database.session.query(UserModel).filter_by(id=user_id).one()

            except NoResultFound as error:

                raise DefaultError(
                    message="Usuario nao encontrado!", type_error=404
                ) from error

            try:
                if not user:

                    raise DefaultError(
                        message="Usuario nao encontrado!", type_error=404
                    )

                database.session.delete(user)
                database.session.commit()

                return user

            except Exception as error:

                database.session.rollback()
                raise DefaultError(message=str(error)) from error

            finally:

                database.session.close()
