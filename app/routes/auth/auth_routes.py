from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from flask_cors import cross_origin
from app.models.users import Token
from .import auth_ctrl


bp = Blueprint("auth_routes_bp", __name__)

@bp.route('/root/', methods=['GET'])
@login_required
def root():
    return jsonify ({'message': f'Hello {current_user.name}'})

@bp.route('/api/auth/', methods=['POST'])
@cross_origin()
def authenticate():
    return auth_ctrl.pre_encode()
