from functools import wraps
from flask import request, jsonify
from src.security.Security import Security

def require_token(f):
    """
    Decorator to protect routes that require a valid JWT token.
    Uses Security.verify_token() for validation.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        headers = request.headers

        # Validate the token using your existing method
        token_valid = Security.verify_token(headers)

        if not token_valid:
            return jsonify({
                "error": "Unauthorized: Invalid or missing token",
                "code": 401
            }), 401

        # Token valid -> proceed to the route
        return f(*args, **kwargs)

    return decorated
