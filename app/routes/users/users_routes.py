from app.routes.users import users_ctrl
from flask import Blueprint

users_routes_bp = Blueprint("users_routes_bp", __name__)


@users_routes_bp.route('/api/users/', methods=['GET'])
def get_users():
    return users_ctrl.get_users()

@users_routes_bp.route('/api/users/<id>/', methods=['GET'])
def get_user(id):
    return users_ctrl.get_user(id)

@users_routes_bp.route('/api/users/', methods=['POST'])
def post_user():
    return users_ctrl.post_user()

@users_routes_bp.route('/api/users/<id>', methods=['PUT'])
def put_user(id):
    return users_ctrl.update_user(id)

@users_routes_bp.route('/api/users/<id>/', methods=['DELETE'])
def delete_user(id):
    return users_ctrl.delete_user(id)
