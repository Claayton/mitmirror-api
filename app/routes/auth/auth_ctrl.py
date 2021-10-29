from flask import jsonify, request
from app.models.users import Token

def pre_encode():
    auth = request.json
    if not auth or not auth["email"] or not auth["password"]:
        return jsonify ({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    encode_email = auth["email"]
    encode_password = auth["password"]
    token = Token.encode_jwt(encode_email, encode_password)
    if token == 403:
        return jsonify ({'message': 'user not found', 'data': {}}), 403
    elif token == 401:
        return jsonify ({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    else:
        return jsonify ({
            'message': 'Validated sucessfully',
            'Authorization': token["Authorization"],
            'exp': token["exp"],
            'id': token["id"]}), 200, {
                'Authorization': token["Authorization"],
                'exp': token["exp"],
                'id': token["id"]
                }
