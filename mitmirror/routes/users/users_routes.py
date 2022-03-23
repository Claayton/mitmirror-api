from mitmirror.routes.users import users_ctrl
from flask import Blueprint

bp = Blueprint("users_routes_bp", __name__)


@bp.route('/api/users/', methods=['GET'])
def get_users():
    return users_ctrl.get_users()

@bp.route('/api/users/<id>/', methods=['GET'])
def get_user(id):
    return users_ctrl.get_user(id)

@bp.route('/api/users/', methods=['POST'])
def post_user():
    return users_ctrl.post_user()

@bp.route('/api/users/<id>', methods=['PUT'])
def put_user(id):
    return users_ctrl.update_user(id)

@bp.route('/api/users/<id>', methods=['DELETE'])
def delete_user(id):
    return users_ctrl.delete_user(id)
