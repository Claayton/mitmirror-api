from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth


class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object('config')
        self.db = SQLAlchemy(self.app)
        self.migrate = Migrate(self.app, self.db)
        self.manager = Manager(self.app)
        self.manager.add_command('db', MigrateCommand)
        self.lm = LoginManager()
        self.lm.init_app(self.app)
        self.lm.login_view = 'login'
        self.bcpt = Bcrypt(self.app)
        self.auth = HTTPBasicAuth()


    def run(self):
        self.app.run()


server = Server()
app = server.app
db = server.db
migrate = server.migrate
manager = server.manager
lm = server.lm
bcpt = server.bcpt
auth = server.auth

from app.models import tables
from app.controllers.routes import *
