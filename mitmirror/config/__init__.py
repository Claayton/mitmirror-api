"""Arquivo de inicializacao do modulo config"""
import os
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="MITMIRROR",
    load_dotenv=True,
    root_path=os.path.dirname(__file__),
    settings_files=["settings.toml", ".secrets.toml"],
)
