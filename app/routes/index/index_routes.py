from flask import Blueprint, jsonify
from app.routes.index import index_ctrl

index_routes_bp = Blueprint('index_routes_bp', __name__)

@index_routes_bp.route('/')
def index():
    return jsonify({'message': 'Successfully fetched', 'routes': index_ctrl.index()}), 200
