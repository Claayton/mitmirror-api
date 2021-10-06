from flask import Blueprint, jsonify
from flask_cors import cross_origin # Evita o cruzamento de rotas em serverver local
from app.routes.auth import auth_ctrl

auth_routes_bp = Blueprint("auth_routes_bp", __name__)

@auth_routes_bp.route('/root/', methods=['GET'])
@auth_ctrl.token_required
def root(current_user):
    return jsonify ({'message': f'Hello {current_user.name}'})

@auth_routes_bp.route('/api/auth/', methods=['POST'])
@cross_origin()
def authenticate():
    return auth_ctrl.auth()
