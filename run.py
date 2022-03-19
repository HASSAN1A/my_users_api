# /run.py
import os
from dotenv import load_dotenv, find_dotenv

from src.app import create_app
from src.config import Production

load_dotenv(find_dotenv())

env_name = os.getenv('FLASK_ENV')
app = create_app(Production)

if __name__ == '__main__':
  port = os.getenv('PORT')
  app.secret_key ='SECRET_KEY'
  app.debug = True
  # run app
  app.run(host='0.0.0.0', port=port)
