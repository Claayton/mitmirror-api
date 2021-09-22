from config.database import database_infos

DEBUG = True

SECRET_KEY = database_infos['secret_key']
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}/{}".format(
                                                                database_infos['username'],
                                                                database_infos['password'],
                                                                database_infos['server'],
                                                                database_infos['name_db'])