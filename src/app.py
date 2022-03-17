#src/app.py

import requests, os
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_caching import Cache

from src.models.UserModel import UserModel
from .config import app_config
from .models import db, bcrypt
from flask_login import LoginManager

# import user_api blueprint
from .views.UserView import user_api as user_blueprint

migrate = Migrate()
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))
app = Flask(__name__)
def create_app(env_name):
    """
    Create app
    """

    app.config.from_object(app_config[env_name])

    cache = Cache(app)
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    app.register_blueprint(user_blueprint)
    app.secret_key = os.getenv('SECRET_KEY')

    return app