from flask import Blueprint, jsonify
from app.routes.index import index_ctrl

bp = Blueprint('index_routes_bp', __name__)

@bp.route('/')
def index():
    return jsonify({'message': 'Successfully fetched', 'routes': index_ctrl.index()}), 200
