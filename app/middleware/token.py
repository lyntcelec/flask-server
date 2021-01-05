from flask_jwt_extended import JWTManager
from flask import jsonify

jwt = JWTManager()
jwt_blacklist = set()


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({"msg": "Token has expired!"}, 401)


@jwt.invalid_token_loader
def invalid_token_callback(*args):
    return jsonify({"msg": args[0]}, 401)


@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({"msg": "Revoked token"}, 401)
