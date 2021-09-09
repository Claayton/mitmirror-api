from flask import g
from flask.sessions import SecureCookieSessionInterface
from flask_login import UserMixin, login_required, user_loaded_from_header
from app import db, bcpt, app, auth
from datetime import datetime
import env # mudar futuramente
import jwt

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

    
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    secondary_id = db.Column(db.Integer, nullable=False)
    is_staff = db.Column(db.Boolean, nullable=False)
    is_active_user = db.Column(db.Boolean, nullable=False)
    last_login = db.Column(db.DateTime, nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False)


    def __init__(self, name, email, username, password_hash, date_joined):

        self.name = name
        self.email = email
        self.username = username
        self.password_hash = password_hash

        self.secondary_id = 0 # Configurar furturamente
        self.is_staff = False
        self.is_active_user = False # Configurar futuramente
        self.last_login = self.login_time() # Configurar futuramente
        self.date_joined = date_joined

        
    def __repr__(self):
        return f'<User {self.username}>'

    def find(self, find_username):
        return self.query.filter_by(username=find_username).first()

    def hash_password(self, password):
        self.password_hash = bcpt.generate_password_hash (password). decode ('utf-8')

    def verify_password(self, password):
        return bcpt.check_password_hash(self.password_hash, password)

    def gerenate_auth_token(self, expires_in=600):
        return jwt.encode(
            {'id': self.id, 'exp': datetime() + expires_in},
            app.config['SECRET_KEY'], algorithm='Hs256')

    @staticmethod
    def verify_auth_token(token):
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['Hs256'])
        except:
            return
        return User.query.get(data['id'])

    def create_secundary_id(self): # Configurar futuramente
        return self.id * self.id

    def login_time(self): # Configurar futuramente
        return datetime.today()
    
    def set_unable_password(self): # Configurar futuramente
        self.password_hash = 'None'

    def has_usable_password(self):
        if not self.password_hash == 'None':
            return True
        else:
            return False

    def set_password(self, new_password):
        self.hash_password = self.hash_password(new_password)

    def send_email(self, msg_subject, msg_message):
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        import smtplib

        msg = MIMEMultipart()
        message = msg_message

        password = env.password_mitmirrortests
        msg['From'] = env.email_mitmirrortests
        msg['To'] = self.email
        msg['Subject'] = msg_subject

        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', port=587)
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()

@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True
