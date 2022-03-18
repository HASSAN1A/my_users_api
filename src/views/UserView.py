#/src/views/UserView

from cgi import test
from email import message
import json
from multiprocessing import context
from sre_constants import SUCCESS
from flask import (
    request, 
    json, Response, Blueprint, 
    jsonify, render_template, 
    redirect, url_for, flash
  )
from itsdangerous import Serializer
from flask_login import login_required, logout_user, login_user
from src.models.forms import RegistrationForm, LoginForm
from src.models import db
from ..models.UserModel import UserModel, UserSchema
from ..auth.Authentication import Auth

user_api = Blueprint('user_api', __name__)
user_schema = UserSchema()

@user_api.route('/register', methods = ['GET', 'POST'])
def user_registration():
  '''User Registration View'''
  form = RegistrationForm(request.form)
  if request.method == 'POST' and form.validate():
      data = request.form
      user = UserModel(data)

      user.save()
      return redirect(url_for('user_api.login'))
  return render_template('register.html',form = form)

@user_api.route('/login', methods=['POST', 'GET'])
def login():
    """
    User Login View
    """
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
      # req_data = request.get_json()
      req_data = json.dumps(request.form)
      data = user_schema.load(json.loads(req_data), partial=True)
      
      if not data.get('email') or not data.get('password'):
        return custom_response({'error': 'you need email and password to sign in'}, 400)
      user = UserModel.get_user_by_email(data.get('email'))

      if not user:
        return custom_response({'error': 'invalid credentials'}, 400)

      if not user.check_hash(data.get('password')):
        return custom_response({'error': 'invalid credentials'}, 400)

      login_user(user)
      flash({"Login Success": "Kabisa", 'code': 200})
      return redirect(url_for('user_api.index'))
      
    return render_template('login.html', form =form)

@user_api.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("user_api.index"))
@user_api.route('/users/', defaults = {'n':None})
@user_api.route('/users/<int:n>/')
@login_required
def get_users(n):
  '''This function returns a paginated number of results, the default is 100'''
  global ROWS_PER_PAGE
  if n is not None:
    ROWS_PER_PAGE = int(n)
  else:
    ROWS_PER_PAGE = 100
  page = request.args.get('page', 1, type=int)
  qs = UserModel.query.paginate(page = page, per_page = ROWS_PER_PAGE)
  qs = qs.items
  serializer =  [user.serialize for user in qs]
  context ={
    'count': len(qs),
    "message": "SUCCESS",
    'status_code': 200,
    'users': serializer
    }
  response = jsonify(context)
  return response

@user_api.route('/users/range/', defaults = {"start":0, "end": 100} )
@user_api.route('/users/range/<int:start>/<int:end>/')
@login_required
def filter_by_range(start, end):
  '''This function queries users by the id range provided.
    Params: start+1 => integer
            end => integer, the limit of results
            Example:
            /users/range/<5/2/ => Will return a query from id 6 to 7

  '''
  serializer = UserModel.filter_by_range(start=start, end=end)
  context = {
    'count': len(serializer),
    "message": "SUCCESS",
    'status_code': 200,
    'users': serializer
  }
  return jsonify(context)



@user_api.route('/user/<int:val>/')
@login_required
def get_user(val):
  '''This function returns a filter of a single user by their id or email'''
  if val.isdigit():
    context = {
      "status code": 200,
      "message": 'SUCCESS',
      "response":UserModel.get_one_user(val).serialize
    }
    return jsonify(context)
  if "@" in val:
    context = {
      "status code": 200,
      "message": 'SUCCESS',
      "response":UserModel.get_user_by_email(val).serialize
    }
    return jsonify(context)

@user_api.route('/users/<name>/')
@login_required
def filter_by_name(name):
  '''This function returns a filter of users by name'''
  serializer = UserModel.filter_users_by_name(name)
  context = {
    'count': len(serializer),
    "message": "SUCCESS",
    'status_code': 200,
    'users': serializer
  }
  return jsonify(context)
@user_api.route('/', methods=['POST'])
def create():
  """
  Create User Function
  """
  req_data = request.get_json()
  data, error = user_schema.load(req_data)

  if error:
    return custom_response(error, 400)
  
  # check if user already exist in the db
  user_in_db = UserModel.get_user_by_email(data.get('email'))
  if user_in_db:
    message = {'error': 'User already exist, please supply another email address'}
    return custom_response(message, 400)
  
  user = UserModel(data)
  user.save()
  ser_data = user_schema.dump(user).data
  token = Auth.generate_token(ser_data.get('id'))
  return custom_response({'jwt_token': token}, 201)

@user_api.route('/', methods=['GET'])
def index():
  """
  returns a landing page
  """
  return render_template('index.html')

@user_api.route('/me', methods=['PUT'])
@Auth.auth_required
def update():
  """
  Update myself
  """
  req_data = request.get_json()
  data, error = user_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)

  user = UserModel.get_one_user(g.user.get('id'))
  user.update(data)
  ser_user = user_schema.dump(user).data
  return custom_response(ser_user, 200)

@user_api.route('/me', methods=['DELETE'])
@Auth.auth_required
def delete():
  """
  Delete a user
  """
  user = UserModel.get_one_user(g.user.get('id'))
  user.delete()
  return custom_response({'message': 'deleted'}, 204)

@user_api.route('/me', methods=['GET'])
@Auth.auth_required
def get_me():
  """
  Get me
  """
  user = UserModel.get_one_user(g.user.get('id'))
  ser_user = user_schema.dump(user).data
  return custom_response(ser_user, 200)
 
def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=jsonify(res),
    status=status_code
  )
