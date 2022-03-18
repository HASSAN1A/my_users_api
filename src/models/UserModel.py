# src/models/UserModel.py
from . import db, bcrypt
from marshmallow import fields, Schema
import datetime
from flask_login import login_manager, UserMixin


class UserModel(UserMixin, db.Model):
  """
  User Model
  """

  # table name
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  # id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  password = db.Column(db.String(128), nullable=False)
  
  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    self.name = data.get('name')
    self.email = data.get('email')
    self.password = self.__generate_hash(data.get('password'))

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      if key == 'password':
        self.password = self.__generate_hash(item)
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()


  def is_active():
    return True

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all_users():
    return UserModel.query.all()

  def get_id(self):
    return str(self.id)
  @staticmethod
  def get_one_user(id):
    return UserModel.query.get(id)
  
  @staticmethod
  def get_user_by_email(value):
    return UserModel.query.filter_by(email=value).first()


  @staticmethod
  def filter_users_by_name(name):
    qs = UserModel.query.filter_by(name=name).all()
    return [item.serialize for item in qs]

  @staticmethod
  def filter_by_range(start, end):
    qs = UserModel.query.offset(start).limit(end).all()
    return [item.serialize for item in qs]
    
  def __generate_hash(self, password):
    return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")
  
  def check_hash(self, password):
    return bcrypt.check_password_hash(self.password, password)
  
  @property
  def serialize(self):
    '''Return a serialized response of the Model'''
    context ={
      "user_id": self.id,
      "name": self.name,
      "email": self.email,
    }
    return context
  def __str__(self):
    return self.name


class UserSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  email = fields.Email(required=True)
  password = fields.Str(required=True, load_only=True)

  def __str__(self) -> str:
      return self.name


