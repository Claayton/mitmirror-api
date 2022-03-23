from flask_login import LoginManager
from mitmirror.models.users import User, Token

lm = LoginManager()

@lm.request_loader
def load_user_from_request(request):
    from flask import request
    from datetime import datetime

    # first, try to login using the api_key url arg
    api_key = request.args.get('token')
    if api_key:
        try:
            user_token = Token.query.filter_by(token=api_key).first()
            current_user = User.query.filter_by(id=user_token.user_id).first()
            if datetime.now() > user_token.expiration:
                raise TimeoutError
            return current_user
        except:
            return None
        
    # next, try to login using JWT
    api_key = request.headers.get('Authorization')
    if api_key:
        try:
            user_token = Token.query.filter_by(token=api_key).first()
            current_user = User.query.filter_by(id=user_token.user_id).first()
            if datetime.now() > user_token.expiration:
                TimeoutError
        except:
            return None
        return current_user
    

def init_app(app):
    lm.init_app(app)
