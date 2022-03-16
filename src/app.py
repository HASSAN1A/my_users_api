#src/app.py

import requests
from flask import Flask, jsonify, request
from flask_caching import Cache
from .config import app_config
from .models import db, bcrypt

# import user_api blueprint
from .views.UserView import user_api as user_blueprint



def create_app(env_name):
  """
  Create app
  """

  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config['development'])

  cache = Cache(app)
  # initializing bcrypt and db
  bcrypt.init_app(app)
  db.init_app(app)

  app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')

  # @app.route('/', methods=['GET'])
  # @cache.cached(timeout=30, query_string=True)
  # def index():
  #   """
  #   Flask app
  #   """
  #   return 'Hello world my users'

  return app

