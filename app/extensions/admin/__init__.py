from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import ModelView
from wtforms import fields, Form
from app.extensions.database import db
from app.models.users import User, Token

# from flask_admin.base import AdminIndexView
# from flask_login import login_required

# AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
# sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)


class UserForm(Form):
    id = fields.IntegerField()
    name = fields.StringField()
    email = fields.StringField()
    username = fields.StringField()
    password_hash = fields.StringField()
    secondary_id = fields.IntegerField()
    is_staff = fields.BooleanField()
    is_active_user =  fields.BooleanField()
    last_login = fields.DateField()
    date_joined = fields.DateField()


class UserView(ModelView):
    form = UserForm
    column_list = ['id', 'name', 'is_active_user']


class TokenForm(Form):
    id = fields.IntegerField()
    token = fields.TextAreaField()
    expiration = fields.DateField()
    user_id = fields.IntegerField()
    user = fields.StringField()


class TokenView(ModelView):
    form = TokenForm
    column_list = ['id', 'user_id', 'user']


def init_app(app):
    admin = Admin(app, name='MitMirror Admin', template_mode='bootstrap4')
    admin.add_view(UserView(User, db.session))
    admin.add_view(TokenView(Token, db.session))
