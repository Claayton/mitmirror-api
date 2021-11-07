from app.extensions.database import db
from flask import request, jsonify
from app.models.users import User
from datetime import datetime

def get_users():
    """
    -> It has the sole function of returning the data of all users registered in the database or an error message if there is none
    :return: The data in json format of all registered users, sorting by id.
    """

    users = User.query.all()
    json_users = {}
    if users:
        for user in users:
            json_user = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "username": user.username,
            }
            json_users[json_user["id"]]=json_user
        
        return jsonify({'message': 'Successfully fetched', 'data': json_users}), 200
    return jsonify({'message': 'nothing found', 'data': {}}), 404

def get_user(id):
    """
    -> It function is to return the data a user registered in the database or an error message if it does not exist.
    :param id: Receives the user id in order to identify the user.
    :return: The data in json format of a registered user.
    """

    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify({'message': "User don't exist", 'data': {}}), 404
    json_user = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "username": user.username,
        "date_joined": user.date_joined
    }
    return jsonify({'message': 'Successfully fetched', 'data': json_user}), 200

def post_user():
    """
    -> Receives data in json format from the client to register a new user with the following information:
        * name,
        * email,
        * username,
        * password.
    -> Treat the information so as not to register two users with the same email or username.
    -> Encrypt the received password with a hash.
    -> Saves the information to the database.
    :return: The data again in json format, now with the encrypted password, a unique id for each user and the registration date.
    """

    email_exists = User.query.filter_by(email=request.json['email']).first()
    username_exists = User.query.filter_by(username=request.json['username']).first()
    if email_exists:
        return jsonify({'message': 'Email unavailable', 'data': {}}), 403
    elif username_exists:
        return jsonify({'message': 'Username unavailable', 'data': {}}), 403

    name = request.json['name']
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']
    date_joined = datetime.today()
    user = User(name, email, username, password, date_joined)
    user.hash_password(password)

    try:
        db.session.add(user)
        db.session.commit() 
        json_user = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "username": user.username,
            "date_joined": user.date_joined
        }
        return jsonify({'message': 'Successfully registered', 'data': json_user}), 201
    except:
        return jsonify({'message': 'Unable to create', 'data': {}}), 500

def update_user(id):
    """
    -> Receives from the client data in json format to update the data of an already registered user, the information to be received is:
        * name,
        * email,
        * username,
        * password.
    -> Treat the information so as not to updated the user with an existing email or username.
    -> Encrypt the new password received with a hash.
    -> Saves the information to the database.
    :param id: Receives the user id in order to identify the user.
    :return: The data again in json format, now with the encrypted password, a unique id for each user and the registration date.
    """
    
    user = User.query.filter_by(id=id).first()

    email_exists = User.query.filter_by(email=request.json['email']).first()
    username_exists = User.query.filter_by(username=request.json['username']).first()
    if user.email != request.json['email'] and email_exists:
        return jsonify({'message': 'Email unavailable', 'data': {}}), 500
    elif user.username != request.json['username'] and username_exists:
        return jsonify({'message': 'Username unavailable', 'data': {}}), 500

    name = request.json['name']
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']
    user.hash_password(password)

    if not user:
        return jsonify({'message': "User don't exist", 'data': {}}), 404

    try:
        user.name = name
        user.email = email
        user.username = username
        user.hash_password(password)
        db.session.commit() 
        json_user = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "username": user.username,
            "date_joined": user.date_joined
        }
        return jsonify({'message': 'Successfully updated', 'data': json_user}), 201
    except:
        return jsonify({'message': 'Unable to update', 'data': {}}), 500
    
def delete_user(id):
    """
    -> It has the function of deleting all the data data of a registered user in the database.
    :param id: Receives the user id in order to identify the user.
    :return: A success message and deleted user data.
    """

    user = User.query.filter_by(id=id).first()

    if not user:
        return jsonify({'message': "User don't exist", 'data': {}}), 403

    if user:
        json_user = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "username": user.username,
        "date_joined": user.date_joined
    }
        try:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'Successfully deleted', 'data': json_user}), 200
        except:
            return jsonify({'message': 'Unable to delete', 'data': json_user}), 500
