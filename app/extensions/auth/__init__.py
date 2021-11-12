from flask import g
from flask.sessions import SecureCookieSessionInterface
from flask_login import LoginManager
from app.models.users import Token
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
            pass
        else:
            return decoded
        
    # next, try to login using JWT
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Bearer ', '', 1)
        decoded = Token.decode_jwt(api_key)
        if not decoded:
            return None
        else:
            return decoded
    
def init_app(app):
    from flask_login import user_loaded_from_header
    
    
    class CustomSessionInterface(SecureCookieSessionInterface):
        """Prevent creating session from API requests."""
        def save_session(self, *args, **kwargs):
            if g.get('login_via_header'):
                return
            return super(CustomSessionInterface, self).save_session(*args,
                                                                    **kwargs)


    app.session_interface = CustomSessionInterface()

    @user_loaded_from_header.connect
    def user_loaded_from_header(self, user=None):
        g.login_via_header = True

    lm.init_app(app)
