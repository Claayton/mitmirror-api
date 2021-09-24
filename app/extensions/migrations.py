from flask_migrate import Migrate, MigrateCommand
from app.extensions.database import db

migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)
    
