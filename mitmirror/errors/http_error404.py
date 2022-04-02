"""Arquivo para HttpNotFound - 404"""


class HttpNotFound(Exception):
    """HttpError 404 - Not Found!"""

    def __init__(self, message: str = "Not Found!") -> None:
        super().__init__(message)
        self.message = message
        self.name = "NotFoundError"
        self.status_code = 404
