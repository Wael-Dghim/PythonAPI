from __init__ import db, ma
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, username, email, password, name):
        self.username = username
        self.email = email
        self.password = password
        self.name = name


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "email", "password", "name")


user_schema = UserSchema()
users_schema = UserSchema(many=True)
