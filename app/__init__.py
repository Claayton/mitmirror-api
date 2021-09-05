from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.app.config.from_object('config')
        self.db = SQLAlchemy(self.app)
        self.migrate = Migrate(self.app, self.db)
        self.manager = Manager(self.app)
        self.manager.add_command('db', MigrateCommand)
        self.lm = LoginManager()
        self.lm.init_app(self.app)
        self.lm.login_view = 'login'
        self.bcpt = Bcrypt(self.app)


    def run(self):
        self.app.run()


server = Server()
app = server.app
api = server.api
db = server.db
migrate = server.migrate
manager = server.manager
lm = server.lm
bcpt = server.bcpt

from app.models import tables
from app.controllers.routes import CallUsers
