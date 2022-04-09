"""Arquivo de inicializacao do modulo config"""
from .database import database_infos

JSONIFY_PRETTYPRINT_REGULAR = True

SECRET_KEY = database_infos["secret_key"]
SQLALCHEMY_TRACK_MODIFICATIONS = True

CONNECTION_STRING_TEST = database_infos["connection_string_test"]
CONNECTION_STRING = "mysql+pymysql://{}:{}@{}/{}".format(
    database_infos["username"],
    database_infos["password"],
    database_infos["server"],
    database_infos["name_db"],
)
