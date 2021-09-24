from flask import Flask

from app.extensions import database
from app.extensions import authentication
from app.extensions import encryptation
from app.extensions import route_crossing
from app.extensions import migrations

from app.blueprints.controllers import routes

def minimal_app():
    app = Flask(__name__)
    app.config.from_object('config')
    return app

def create_app():
    app = minimal_app()

    database.init_app(app)
    authentication.init_app(app)
    encryptation.init_app(app)
    route_crossing.init_app(app)
    migrations.init_app(app)
    routes.init_app(app)
    return app
