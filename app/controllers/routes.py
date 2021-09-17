from app.views import users, helper
from flask import jsonify

from app import app

@app.route('/', methods=['GET'])
@helper.token_required
def root(current_user):
    return jsonify ({'message': f'Hello {current_user.name}'})

@app.route('/api/auth', methods=['POST'])
def authenticate():
    return helper.auth()

@app.route('/api/users/', methods=['POST'])
def post_user():
    return users.post_user()

@app.route('/api/users/<id>', methods=['PUT'])
def put_user(id):
    return users.update_user(id)

@app.route('/api/users/', methods=['GET'])
def get_users():
    return users.get_users()

@app.route('/api/users/<id>/', methods=['GET'])
def get_user(id):
    return users.get_user(id)

@app.route('/api/users/<id>/', methods=['DELETE'])
def delete_user(id):
    return users.delete_user(id)
