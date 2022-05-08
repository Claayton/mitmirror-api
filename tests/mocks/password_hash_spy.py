"""Spy para PasswordHash"""


class PasswordHashSpy:
    """Spy para a classe PasswordHash"""

    def __init__(self) -> None:

        self.hash_params = {}
        self.verify_params = {}

    def hash(self, password: str) -> str:
        """Realiza o procesos de hash da senha"""

        self.hash_params["password"] = password

        return b"$2b$12$bw0tdfUAgnYLjJWtVqb00O/bEEzSPTl7hiQwcssijzRCqkuc9K9AS"

    def verify(self, password: str, password_hashed: str) -> bool:
        """Realiza a verificaçao se a senha passada é a mesma da senha cadastrada"""

        self.verify_params["password"] = password
        self.verify_params["password_hashed"] = password_hashed

        return True
