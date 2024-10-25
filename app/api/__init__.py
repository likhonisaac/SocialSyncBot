from flask import Blueprint, jsonify, request
from app.services.sync_service import SyncService
from app.utils.auth import require_api_key

api_bp = Blueprint('api', __name__)
sync_service = SyncService()

@api_bp.route('/sync', methods=['POST'])
@require_api_key
def sync_post():
    data = request.get_json()
    result = sync_service.sync_post(
        content=data.get('content'),
        platforms=data.get('platforms', ['twitter', 'telegram'])
    )
    return jsonify(result)

@api_bp.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "operational"})
