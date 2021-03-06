"""Arquivo para DefaultError"""


class DefaultError(Exception):
    """Erro personalizado padrao"""

    def __init__(self, type_error: any = "default", message: str = None) -> None:

        super().__init__(message)
        self.type_error = type_error
        self.message = message
