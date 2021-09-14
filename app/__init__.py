from flask import Flask
from flask_script import Manager
from flask_migrate import MigrateCommand
from app.extensions import database
from app.extensions import migrations
from app.extensions import authentication
from app.extensions import encryptation


app = Flask(__name__)
app.config.from_object('config')

manager = Manager(app)
manager.add_command('db', MigrateCommand)

database.init_app(app)
migrations.init_app(app)
authentication.init_app(app)
encryptation.init_app(app)

from app.models import users
from app.controllers.routes import *
