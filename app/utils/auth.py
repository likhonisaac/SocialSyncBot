from functools import wraps
from flask import request, jsonify
from config import Config

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key and api_key == Config.SECRET_KEY:
            return f(*args, **kwargs)
        return jsonify({"error": "Invalid API key"}), 401
    return decorated_function
