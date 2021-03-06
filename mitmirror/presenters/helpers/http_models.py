"""Arquivo para Http Models"""
from typing import Dict


class HttpRequest:
    """Representaçao de requisicoes"""

    def __init__(
        self, headers: Dict = None, body: Dict = None, query: Dict = None
    ) -> None:
        self.headers = headers
        self.body = body
        self.query = query

    def __repr__(self):
        return f"HttpRequest (headers={self.headers}, body={self.body}, query={self.query})"


class HttpResponse:
    """Representaçao de respostas"""

    def __init__(self, status_code: int, body: Dict) -> None:
        self.status_code = status_code
        self.body = body

    def __repr__(self):
        return f"HttpResponse (status_code={self.status_code}, body={self.body})"
