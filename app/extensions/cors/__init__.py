from typing import NoReturn
from flask_cors import CORS

from flask import Flask
from typing import NoReturn

cors = CORS()

def init_app(app: Flask) -> NoReturn:
    recursos = {
        r"/api/users/": {"origins": "*"},
    }
    cors.init_app(app, resources=recursos)
