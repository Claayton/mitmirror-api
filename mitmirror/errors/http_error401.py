"""Arquivo para HttpUnauthorized - 401"""


class HttpUnauthorized(Exception):
    """HttpError 401 - Unauthorized!"""

    def __init__(self, message: str = "Unauthorized!") -> None:
        super().__init__(message)
        self.message = message
        self.name = "UnauthorizedError"
        self.status_code = 401
