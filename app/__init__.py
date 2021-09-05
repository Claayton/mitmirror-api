from flask import Flask
from flask_restful import Resource, Api


class Server():
    def __init__(self):
        self.app = Flask(__name__)
        # self.app.config.from_object('config')
        self.api = Api(self.app)  

    def run(self):
        self.app.run()


server = Server()
api = server.api

from app.controllers.users import Users