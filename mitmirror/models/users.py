from mitmirror.extensions.database import db
from mitmirror.extensions.security import bcpt

from flask_login import UserMixin
from mitmirror.config.email import email_infos
from datetime import datetime, timedelta


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

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

        self.secondary_id = 0  # Configurar furturamente
        self.is_staff = False
        self.is_active_user = False  # Configurar futuramente
        self.last_login = self.login_time()  # Configurar futuramente
        self.date_joined = date_joined

    def __repr__(self):
        return f"<User {self.name}>"

    def find(self, find_username):
        return self.query.filter_by(username=find_username).first()

    def hash_password(self, password):
        self.password_hash = bcpt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        return bcpt.check_password_hash(self.password_hash, password)

    def create_secundary_id(self):  # Configurar futuramente
        return self.id * self.id

    def login_time(self):  # Configurar futuramente
        return datetime.today()

    def set_unable_password(self):  # Configurar futuramente
        self.password_hash = "None"

    def has_usable_password(self):
        if not self.password_hash == "None":
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

        password = email_infos["password"]
        msg["From"] = email_infos["email"]
        msg["To"] = self.email
        msg["Subject"] = msg_subject

        msg.attach(MIMEText(message, "plain"))
        server = smtplib.SMTP("smtp.gmail.com", port=587)
        server.starttls()
        server.login(msg["From"], password)
        server.sendmail(msg["From"], msg["To"], msg.as_string())
        server.quit()


class Token(db.Model):
    __tablename__ = "tokens"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    token = db.Column(db.String(256))
    expiration = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", foreign_keys=user_id)

    def __init__(self, token, user_id, expiration):
        self.token = token
        self.expiration = expiration
        self.user_id = user_id

    def __repr__(self):
        return f"<Token {self.id}>"

    def auth():
        """
        -> Receive username and password in json format,
        check if the user is registered and the password is correct,
        generate a new token and register it in the db, if there is already
        one registered, the system will generate a different one and replace
        the current one, along with an expiration time for the new token.
        :return: The new token generated and its expiration time in json format.
        """
        from mitmirror.extensions.database import db
        import config
        import jwt
        from flask import request, jsonify

        auth = request.json
        if not auth or not auth["username"] or not auth["password"]:
            return (
                jsonify(
                    {
                        "message": "Could not verify",
                        "WWW-Authenticate": 'Basic auth="Login required"',
                    }
                ),
                401,
            )

        user = User.query.filter_by(username=auth["username"]).first()
        if not user:
            return jsonify({"message": "user not found", "data": {}}), 403

        if user and user.verify_password(auth["password"]):
            payloads = {
                "exp": datetime.utcnow() + timedelta(hours=4),
                "iat": datetime.utcnow(),
                "sub": user.username,
            }
            try:
                user_token = Token.query.filter_by(user_id=user.id).first()
                while True:
                    token = jwt.encode(payloads, config.SECRET_KEY, algorithm="HS256")
                    if token != user_token.token:
                        break
                user_token.token = token
                user_token.expiration = datetime.now() + timedelta(hours=4)
                db.session.commit()
            except:
                token = jwt.encode(payloads, config.SECRET_KEY, algorithm="HS256")
                user_token = Token(
                    token, user.id, datetime.utcnow() + timedelta(hours=4)
                )
                db.session.add(user_token)
                db.session.commit()

            return (
                jsonify(
                    {
                        "message": "Validated sucessfully",
                        "token": user_token.token,
                        "exp": user_token.expiration,
                    }
                ),
                200,
            )

        return (
            jsonify(
                {
                    "message": "Could not verify",
                    "WWW-Authenticate": 'Basic auth="Login required"',
                }
            ),
            401,
        )
