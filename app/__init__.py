from flask import Flask

from app.extensions import database
from app.extensions import authentication
from app.extensions import encryptation
from app.extensions import route_crossing
from app.extensions import migrations

from app.routes.users.users_routes import users_routes_bp
from app.routes.auth.auth_routes import auth_routes_bp


class NewApp:

    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object('config')

    def minimal_app(self):
        return self.app

    def create_app(self):
        database.init_app(self.app)
        authentication.init_app(self.app)
        encryptation.init_app(self.app)
        route_crossing.init_app(self.app)
        migrations.init_app(self.app)
        
        self.app.register_blueprint(users_routes_bp)
        self.app.register_blueprint(auth_routes_bp)
        return self.app

    def run(self):
        self.app = self.create_app()
        self.app.run()
