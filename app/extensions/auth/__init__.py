from flask_login import LoginManager
from app.models.users import User, Token
from app.models.users import Token

lm = LoginManager()

@lm.request_loader
def load_user_from_request(request):
    from flask import request

    # first, try to login using the api_key url arg
    api_key = request.args.get('token')
    if api_key:
        decoded = Token.decode_jwt(api_key)
        if not decoded:
            return None
        else:
            return decoded
        
    # next, try to login using JWT
    api_key = request.headers.get('Authorization')
    if api_key:
        decoded = Token.decode_jwt(api_key)
        if not decoded:
            return None
        else:
            return decoded
    
def init_app(app):
    lm.init_app(app)
