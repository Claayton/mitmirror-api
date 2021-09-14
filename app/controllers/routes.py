from flask import jsonify, g, request
from flask_login import login_required, logout_user, login_user, current_user
from app import app
from app.views import users, helper

@app.route('/api/users/', methods=['POST'])
def post_user():
    return users.post_user()

@app.route('/api/users/<id>', methods=['PUT'])
def put_user(id):
    return users.update_user(id)

@app.route('/api/users/', methods=['GET'])
def get_users():
    return users.get_users()

@app.route('/api/users/<id>/', methods=['GET'])
def get_user(id):
    return users.get_user(id)

@app.route('/api/users/<id>/', methods=['DELETE'])
def delete_user(id):
    return users.delete_user(id)

@app.route('/api/auth', methods=['POST'])
def authenticate():
    return helper.auth()

@app.route('/', methods=['GET'])
@helper.token_required
def root(current_user):
    return jsonify ({'message': f'Hello {current_user.name}'})


"""
@lm.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@lm.request_loader
def load_user_from_request(request):

    # first, try to login using the api_key url arg
    api_key = request.args.get('api_key')
    if api_key:
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # next, try to login using Basic Auth
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        try:
            api_key = base64.b64decode(api_key)
        except TypeError:
            pass
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # finally, return None if both methods did not login the user
    return None


class CustomSessionInterface(SecureCookieSessionInterface):
    Prevent creating session from API requests.
    def save_session(self, *args, **kwargs):
        if g.get('login_via_header'):
            return
        return super(CustomSessionInterface, self).save_session(*args,
                                                                **kwargs)

app.session_interface = CustomSessionInterface()

@user_loaded_from_header.connect
def user_loaded_from_header(self, user=None):
    g.login_via_header = True"""