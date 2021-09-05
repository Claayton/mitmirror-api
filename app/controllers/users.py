from flask_restful import Resource
from app import server
from app.models.users import books_db

app, api = server.app, server.api


class Users(Resource):
    def get(self):
        return books_db

server.api.add_resource(Users, '/margarina')
