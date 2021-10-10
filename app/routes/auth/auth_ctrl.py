from flask import jsonify, request
from app.models.users import Token

def pre_encode():
    auth = request.json
    if not auth or not auth["email"] or not auth["password"]:
        return jsonify ({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    encode_email = auth["email"]
    encode_password = auth["password"]
    return Token.encode_jwt(encode_email, encode_password)
