from app.models.users import User
from app.views import users

import jwt
from flask import request, jsonify
from functools import wraps
from datetime import datetime, timedelta

from app import app



def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify ({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

    user = User.query.filter_by(username=auth.username).first()
    if not user:
        return jsonify ({'message': 'user not found', 'data': {}}), 401

    if user and user.verify_password(auth.password):
        token = jwt.encode({'username': user.username, 'exp': datetime.now() + timedelta(hours=4)}, app.config['SECRET_KEY'])

        return jsonify ({'message': 'Validated sucessfully', 'token': token, 'exp': datetime.now() + timedelta(hours=12)})
    return jsonify ({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

def token_required(f):
    wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify ({'message': 'Token is missing', 'data': {}}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(username=data['username']).first()
        except:
            return jsonify ({'message': 'Token is invalid or expired', 'data': {}}), 401
        return f (current_user, *args, **kwargs)
    return decorated
