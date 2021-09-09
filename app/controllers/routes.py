from flask import request, g
from flask_login import login_user, logout_user, login_required
from app import app, db, auth
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


@app.route('/api/login/', methods=['POST', 'GET'])
def login():

    body = request.get_json()
    print(f'\033[31m{body}\033[m')
    if "remember_me" not in body:
        body["remember_me"] = False

    user = User.query.filter_by(username=body["username"]).first()
    if not user:
        return generate_response(404, 'user not found')
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

@app.route('/api/<token>/user/', methods=['POST'])
def register(token=''):
    from datetime import datetime

    body = request.get_json()

    if "name" not in body:
        return generate_response(401, 'Field name required')
    elif "lastname" not in body:
        body["lastname"] = ''
    elif "email" not in body:
        return generate_response(401, 'Field email required')
    elif "password" not in body:
        return generate_response(401, 'Field password required')
    elif "confirm_password" not in body:
        return generate_response(401, 'Field confirm_password required')
    if "remember_me" not in body:
        body["remember_me"] = False

    user_name = User.query.filter_by(username=body["username"]).first()
    if user_name:
        return generate_response(401, 'This username already registered')
    user_email = User.query.filter_by(email=body["email"]).first()
    if user_email:
        return generate_response(401, 'This email already registered')
    elif body["password"] != body["confirm_password"]:
        return generate_response(401, 'The passwords are different')
    else:
        i = User(f'{body["name"]} {body["lastname"]}'.strip(), body["email"], body["username"], body["password"], datetime.today())
        i.hash_password(body["password"])
        db.session.add(i)
        db.session.commit()

        user = {
            "id": i.id,
            "name": i.name,
            "username": i.username,
            "email": i.email,
            "username": i.username,
            "remember_me": body["remember_me"]
        }
        return generate_response(200, 'Registered user', 'user', user)

@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return ({'token': token.decode('ascii'), 'duration': 600})

@app.route('/api/<token>/user/<get_user>', methods=['GET'])
def get_user(token, get_user):
    i = User.query.filter_by(username=get_user).first()
    if not i:
        i = User.query.filter_by(id=get_user).first()
        if not i:
            return generate_response(404, 'user not found')
    user = {
            "id": i.id,
            "name": i.name,
            "username": i.username,
            "email": i.email,
            "username": i.username
        }
    return generate_response(200, 'User found', 'user', user)


@auth.login_required
@app.route('/api/token/user/<get_user>', methods=['DELETE'])
def delete(get_user, token=''):

    i = User.query.filter_by(username=get_user).first()
    if not i:
        i = User.query.filter_by(id=get_user).first()
        if not i:
            return generate_response(404, 'user not found')

    db.session.delete(i)
    db.session.commit()
    user = {
            "id": i.id,
            "name": i.name,
        }
    return generate_response(200, 'User deleted', 'user', user)
