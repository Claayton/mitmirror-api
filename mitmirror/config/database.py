""""Configuracoes de banco de dados"""
import os
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    "name_db": os.getenv("DATABASE"),
    "username": os.getenv("USERNAME_DB"),
    "password": os.getenv("PASSWORD_DB"),
    "server": os.getenv("SERVER_DB"),
    "secret_key": os.getenv("SECRET_KEY"),
}
