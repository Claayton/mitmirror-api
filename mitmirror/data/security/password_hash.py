"""Caso de uso: PasswordHash"""
import bcrypt
from mitmirror.domain.usecases import PasswordHashInterface


class PasswordHash(PasswordHashInterface):
    """Classe responsavel por realizar o hash de senhas de usuarios"""

    @staticmethod
    def hash(password: str) -> str:
        """Realiza o procesos de hash da senha"""

        hashed = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())

        return hashed

    @staticmethod
    def verify(password: str, password_hashed: str) -> bool:
        """Realiza a verificaçao se a senha passada é a mesma da senha cadastrada"""

        is_hashed = (
            bcrypt.hashpw(password.encode("utf8"), password_hashed) == password_hashed
        )

        return is_hashed
