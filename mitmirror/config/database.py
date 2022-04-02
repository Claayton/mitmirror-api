""""Configuracoes de banco de dados"""
import os
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    "connection_string_test": os.getenv("CONNECTION_STRING_TEST"),
    "name_db": os.getenv("DATABASE_HEROKU"),
    "username": os.getenv("MYSQL_USERNAME_HEROKU"),
    "password": os.getenv("MYSQL_PASSWORD_HEROKU"),
    "server": os.getenv("MYSQL_SERVER_HEROKU"),
    "secret_key": os.getenv("SECRET_KEY"),
}
