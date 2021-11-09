from typing import NoReturn
from flask_cors import CORS

from flask import Flask
from typing import NoReturn


def init_app(app: Flask) -> NoReturn:
    recursos = {
        r"/api/users/*": {"origins": "*"},
    }
    cors= CORS(app, resources=recursos)
