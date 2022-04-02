"""Arquivo de inicializacao para o modulo erros"""
from .default_error import DefaultError
from .http_request_error import HttpRequestError
from .http_error400 import HttpBadRequestError
from .http_error401 import HttpUnauthorized
from .http_error404 import HttpNotFound
from .http_error422 import HttpUnprocessableEntity
