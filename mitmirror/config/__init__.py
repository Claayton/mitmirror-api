"""Arquivo de inicializacao do modulo config"""
from .database import database_infos
import os

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="MITMIRROR",
    root_path=os.path.dirname(__file__),
    settings_files=["settings.toml"],
)

JSONIFY_PRETTYPRINT_REGULAR = True

SECRET_KEY = database_infos["secret_key"]
SQLALCHEMY_TRACK_MODIFICATIONS = True

CONNECTION_STRING = "mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4".format(
    database_infos["username"],
    database_infos["password"],
    database_infos["server"],
    database_infos["name_db"],
)
