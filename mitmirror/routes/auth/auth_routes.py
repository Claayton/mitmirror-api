from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from flask_cors import cross_origin
from mitmirror.models.users import Token


bp = Blueprint("auth_routes_bp", __name__)

@bp.route('/root/', methods=['GET'])
@login_required
def root():
    return jsonify ({'message': f'Hello {current_user.name}'})

@bp.route('/api/auth/', methods=['POST'])
@cross_origin()
def authenticate():
    return Token.auth()
