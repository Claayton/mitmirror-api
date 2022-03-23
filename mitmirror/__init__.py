from flask import Flask

from mitmirror.extensions import database
from mitmirror.extensions import authentication
from mitmirror.extensions import security
from mitmirror.extensions import crossing
from mitmirror.extensions import migrations
from mitmirror.extensions import admin

from mitmirror.routes.users import users_routes
from mitmirror.routes.auth import auth_routes
from mitmirror.routes.index import index_routes

def minimal_app(config_file):
    app = Flask(__name__)
    app.config.from_object(config_file)
    return app

def create_app():
    app = minimal_app(config_file='config')

    database.init_app(app)
    authentication.init_app(app)
    security.init_app(app)
    crossing.init_app(app)
    migrations.init_app(app)
    admin.init_app(app)
    
    app.register_blueprint(users_routes.bp)
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(index_routes.bp)
    return app

def tests_app():
    app = minimal_app(config_file='config.config_tests')

    database.init_app(app)
    authentication.init_app(app)
    security.init_app(app)
    crossing.init_app(app)
    migrations.init_app(app)
    admin.init_app(app)
    
    app.register_blueprint(users_routes.bp)
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(index_routes.bp)
    return app
