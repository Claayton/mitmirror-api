from flask import Flask

from app.extensions import database
from app.extensions import authentication
from app.extensions import encryptation
from app.extensions import route_crossing
from app.extensions import migrations

from app.routes.users.users_routes import users_routes_bp
from app.routes.auth.auth_routes import auth_routes_bp

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
    
    app.register_blueprint(users_routes_bp)
    app.register_blueprint(auth_routes_bp)
    return app
