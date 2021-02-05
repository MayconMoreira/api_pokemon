from functools import wraps

import jwt
from flask import current_app, jsonify, request
from models.user import User


def jwt_requerid(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        token = None

        if 'authorization' in request.headers:
            token = request.headers.get('Authorization')

        if not token:
            return jsonify({'error': 'you are not allowed to acess this route.'}), 403

        try:
            decoded = jwt.decode(
                token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.get(decoded['id'])
        except:
            return jsonify({'error': 'invalid token.'}), 401

        return function(current_user=current_user, *args, **kwargs)

    return wrapper
