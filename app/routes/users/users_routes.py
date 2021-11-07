from app.routes.users import users_ctrl
from flask import Blueprint
from flask_cors import cross_origin
from flask_login import login_required

bp = Blueprint("users_routes_bp", __name__)

@bp.route('/api/users/', methods=['GET'])
def get_users():
    return users_ctrl.get_users()

@cross_origin()
@login_required
@bp.route('/api/users/<id>/', methods=['GET'])
def get_user(id):
    return users_ctrl.get_user(id)

@cross_origin()
@bp.route('/api/users/', methods=['POST'])
def post_user():
    return users_ctrl.post_user()

@cross_origin()
@login_required
@bp.route('/api/users/<id>', methods=['PUT'])
def put_user(id):
    return users_ctrl.update_user(id)

@cross_origin()
@login_required
@bp.route('/api/users/<id>', methods=['DELETE'])
def delete_user(id):
    return users_ctrl.delete_user(id)
