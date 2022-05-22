"""Arquivo de inicializacao do modulo config"""
import os
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="MITMIRROR",
    load_dotenv=True,
    root_path=os.path.dirname(__file__),
    settings_files=["settings.toml", ".secrets.toml"],
)

# CONNECTION_STRING = "mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4".format(
#     settings.USERNAME_DB,
#     settings.PASSWORD_DB,
#     settings.SERVER_DB,
#     settings.DB_NAME
# )
