"""Arquivo para HttpForbidden - 403"""


class HttpForbidden(Exception):
    """HttpError 403 - Forbidden!"""

    def __init__(self, message: str = "Forbidden!") -> None:
        super().__init__(message)
        self.message = message
        self.name = "ForbiddenError"
        self.status_code = 403
