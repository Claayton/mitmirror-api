from flask import request
from flask_login import login_user, logout_user, login_required
from flask_restful import Resource
from app import api, db
from app.models.tables import User

def generate_response(status,
                    message,
                    content_name=False,
                    content=False):

    response = {}
    response["message"] = message
    response["status"] = status

    if content_name and content:
        response[f"{content_name}"] = content
    return response


class CallUsers(Resource):
    def post(self):

        body = request.get_json()

        user = User.query.filter_by(username=body["username"]).first()
        if not user:
            return generate_response(400, 'user not found')
        elif not user.verify_password(body["password"]):
            return generate_response(401, 'Incorrect username or password')
        else:
            if body["remember_me"]:
                login_user(user, remember=True)
            else:
                login_user(user)
            user = {
                    "id": f"{user.id}",
                    "name": f"{user.name}",
                    "username": f"{user.username}",
                    "password": f"{user.password_hash}"
                    }
            return generate_response(200, 'User found', 'user', user)

api.add_resource(CallUsers, '/user/')
