import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

secret = os.environ.get("SECRET_KEY")
db_uri = os.environ.get("DATABASE_URI")

app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = secret

db = SQLAlchemy(app)
ma = Marshmallow(app)
