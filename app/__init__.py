from flask import Flask
from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
# A principio isso só é requirido para rodar a aplicação em server local

from app.extensions import database
from app.extensions import authentication
from app.extensions import encryptation

from app.extensions.database import db

app = Flask(__name__)
app.config.from_object('config')
CORS(app)
# A principio isso só é requirido para rodar a aplicação em server local

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

database.init_app(app)
authentication.init_app(app)
encryptation.init_app(app)

from app.models import users
from app.controllers.routes import *
