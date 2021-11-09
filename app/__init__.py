from flask import Flask

from app.extensions import database
from app.extensions import auth
from app.extensions import security
from app.extensions import cors
from app.extensions import migrations
from app.extensions import admin

from app.routes.users import users_routes
from app.routes.auth import auth_routes
from app.routes.index import index_routes

def minimal_app(config_file):
    app = Flask(__name__)
    app.config.from_object(config_file)
    return app

def create_app():
    app = minimal_app(config_file='config')

    database.init_app(app)
    auth.init_app(app)
    security.init_app(app)
    cors.init_app(app)
    migrations.init_app(app)
    admin.init_app(app)
    
    app.register_blueprint(users_routes.bp)
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(index_routes.bp)
    return app

def tests_app():
    app = minimal_app(config_file='config.config_tests')

    database.init_app(app)
    auth.init_app(app)
    security.init_app(app)
    cors.init_app(app)
    migrations.init_app(app)
    admin.init_app(app)
    
    app.register_blueprint(users_routes.bp)
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(index_routes.bp)
    return app
