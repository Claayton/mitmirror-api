"""Configuracoes de testes"""
from .database import database_infos

JSONIFY_PRETTYPRINT_REGULAR = True

SECRET_KEY = database_infos["secret_key"]
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "sqlite:///tests.sqlite3"
