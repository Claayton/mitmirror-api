from env import *

DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}/mitmirror".format(mysql_username, mysql_password, mysql_server)

SECRET_KEY = secret_key
