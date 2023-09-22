from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User, user_schema
from sqlalchemy import or_

from __init__ import db


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():
    email = request.json["email"]
    username = request.json["username"]
    password = request.json["password"]
    name = request.json["name"]

    user = User.query.filter(
        or_(User.email == email, User.username == username)
    ).first()
    if user:
        return jsonify({"message": "User already exists"}), 409

    new_user = User(
        username=username,
        email=email,
        password=generate_password_hash(password, method="sha256"),
        name=name,
    )

    db.session.add(new_user)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "User created successfully",
                "user": {"username": username, "email": email, "name": name},
            }
        ),
        201,
    )


@auth_bp.route("/login", methods=["POST"])
def login():
    email = request.json.get("email") or None
    username = request.json.get("username") or None
    password = request.json["password"]
    remember = request.json["remember"]

    user = User.query.filter(
        or_(User.email == email, User.username == username)
    ).first()
    print(user)
    if not user or not check_password_hash(user.password, password):
        return (
            jsonify({"message": "Please check your login details and try again"}),
            403,
        )

    login_user(user, remember=remember)
    return (
        jsonify(
            {
                "message": "User logged in successfully",
                "user": {
                    "username": username if username else None,
                    "email": email if email else None,
                    "name": user.name,
                },
            }
        ),
        200,
    )


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return jsonify({"message": "User logged out successfully"})
