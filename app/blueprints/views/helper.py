from app.extensions.database import db
from app.blueprints.models.users import User, Token

import jwt
from flask import request, jsonify
from functools import wraps
from datetime import datetime, timedelta

def auth():
    """
    -> Receive username and password in json format, check if the user is registered and the password is correct, generate a new token and register it in the db, if there is already one registered, the system will generate a different one and replace the current one, along with an expiration time for the new token.
    :return: The new token generated and its expiration time in json format.
    """
    
    auth = request.json
    if not auth or not auth["username"] or not auth["password"]:
        return jsonify ({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

    user = User.query.filter_by(username=auth["username"]).first()
    if not user:
        return jsonify ({'message': 'user not found', 'data': {}}), 401

    if user and user.verify_password(auth["password"]):
        try:
            user_token = Token.query.filter_by(user_id=user.id).first()
            while True:
                token = jwt.encode({'username': user.username, 'exp': datetime.now() + timedelta(hours=4)}, app.config['SECRET_KEY'])
                if token != user_token.token:
                    break
            user_token.token = token
            user_token.expiration = datetime.now() + timedelta(hours=4)
            db.session.commit()
        except:
            token = jwt.encode({'username': user.username, 'exp': datetime.now() + timedelta(hours=4)}, app.config['SECRET_KEY'])

            user_token = Token(token, user.id, datetime.now() + timedelta(hours=4))
            db.session.add(user_token)
            db.session.commit() 
        
        return jsonify ({'message': 'Validated sucessfully', 'token': token, 'exp': datetime.now() + timedelta(hours=12)})

    return jsonify ({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

def token_required(f):
    wraps(f)
    """
    A decorator for routes that requires a token to give access to user information, the system receives this token, checks if it is registered in the db and checks if it has not expired.
    
    :param f: Receive the decorated function.
    :return: The current user if the token data is valid, along with their data.
    """
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify ({'message': 'Token is missing', 'data': {}}), 401
        try:
            user_token = Token.query.filter_by(token=token).first()
            current_user = User.query.filter_by(id=user_token.user_id).first()
            if datetime.now() > user_token.expiration:
                TimeoutError
        except:
            return jsonify ({'message': 'Token is invalid or expired', 'data': {}}), 401
        return f (current_user, *args, **kwargs)
    return decorated
