from app.routes.users import users_ctrl
from flask import Blueprint
from flask_cors import cross_origin
from flask_login import login_required

bp = Blueprint("users_routes_bp", __name__, url_prefix='/api')

@bp.route('/users/', methods=['GET'])
def get_users():
    return users_ctrl.get_users()

@bp.route('/users/<id>/', methods=['GET'])
@login_required
@cross_origin()
def get_user(id):
    return users_ctrl.get_user(id)

@bp.route('/users/', methods=['POST'])
@cross_origin()
def post_user():
    return users_ctrl.post_user()

@bp.route('/users/<id>/', methods=['PUT'])
@login_required
@cross_origin()
def put_user(id):
    return users_ctrl.update_user(id)

@bp.route('/users/<id>/', methods=['DELETE'])
@login_required
@cross_origin()
def delete_user(id):
    return users_ctrl.delete_user(id)
