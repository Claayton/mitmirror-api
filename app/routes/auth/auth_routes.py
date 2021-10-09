from flask import Blueprint, jsonify
from flask_cors import cross_origin
from app.routes.auth import auth_ctrl


bp = Blueprint("auth_routes_bp", __name__)

@bp.route('/root/', methods=['GET'])
@auth_ctrl.token_required
def root(current_user):
    return jsonify ({'message': f'Hello {current_user.name}'})

@bp.route('/api/auth/', methods=['POST'])
@cross_origin()
def authenticate():
    return auth_ctrl.auth()
