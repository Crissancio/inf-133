from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
import json


def jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 401

    return wrapper


def roles_required(roles=[]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                verify_jwt_in_request()
                current_user = get_jwt_identity()
                user_roles = json.loads(current_user.get("role", []))
                if not set(roles).intersection(user_roles):
                    return jsonify({"error": "Acceso no autorizado para este rol"}), 403
                return func(*args, **kwargs)
            except Exception as e:
                return jsonify({"error": str(e)}), 401

        return wrapper

    return decorator