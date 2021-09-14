from app import db
from flask import request, jsonify
from app.models.users import User
from datetime import datetime

def post_user():
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
            "password_hash": user.password_hash,
            "date_joined": user.date_joined
        }
        return jsonify({'message': 'Successfully registered', 'data': json_user}), 201
    except:
        return jsonify({'message': 'Unable to create', 'data': {}}), 500
        
def update_user(id):
    name = request.json['name']
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']
    user = User.query.filter_by(id=id).first()
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
            "password_hash": user.password_hash,
            "date_joined": user.date_joined
        }
        return jsonify({'message': 'Successfully updated', 'data': json_user}), 201
    except:
        return jsonify({'message': 'Unable to update', 'data': {}}), 500
    
def get_users():
    json_list = []
    users = User.query.all()
    if users:
        for c in users:
            json_user = {
            "id": c.id,
            "name": c.name,
            "email": c.email,
            "username": c.username,
            "password_hash": c.password_hash,
            "date_joined": c.date_joined
            }
            json_list.append(json_user)
           
        
        return jsonify({'message': 'Successfully fetched', 'data': json_list}), 200
    return jsonify({'message': 'nothing found', 'data': {}}), 404

def get_user(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify({'message': "User don't exist", 'data': {}}), 404
    json_user = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "username": user.username,
        "password_hash": user.password_hash,
        "date_joined": user.date_joined
    }
    return jsonify({'message': 'Successfully fetched', 'data': json_user}), 201

def delete_user(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify({'message': "User don't exist", 'data': {}}), 404

    if user:
        json_user = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "username": user.username,
        "password_hash": user.password_hash,
        "date_joined": user.date_joined
    }
        try:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'Successfully deleted', 'data': json_user}), 200
        except:
            return jsonify({'message': 'Unable to delete', 'data': json_user}), 500

def user_by_userame(username):
    try: 
        return User.query.filter_by(username=username).first()
    except:
        return None
