from flask import Blueprint
from models.user import User, user_schema, users_schema
from .auth import auth_bp


users_bp = Blueprint("users", __name__)

users_bp.register_blueprint(auth_bp, url_prefix="/auth")


@users_bp.route("/")
def contact_hello():
    return "Hello from contact route", 200
