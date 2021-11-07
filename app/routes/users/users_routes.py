from app.routes.users import users_ctrl
from flask import Blueprint
from flask_cors import cross_origin
from flask_login import login_required

bp = Blueprint("users_routes_bp", __name__)

@bp.route('/api/users/', methods=['GET'])
def get_users():
    return users_ctrl.get_users()

@bp.route('/api/users/<id>/', methods=['GET'])
@cross_origin()
@login_required
def get_user(id):
    return users_ctrl.get_user(id)

@bp.route('/api/users/', methods=['POST'])
@cross_origin()
def post_user():
    return users_ctrl.post_user()

@bp.route('/api/users/<id>/', methods=['PUT'])
@cross_origin()
@login_required
def put_user(id):
    return users_ctrl.update_user(id)

@bp.route('/api/users/<id>/', methods=['DELETE'])
@cross_origin()
@login_required
def delete_user(id):
    return users_ctrl.delete_user(id)
