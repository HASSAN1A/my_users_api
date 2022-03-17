from click import confirm
from flask_wtf import FlaskForm
# from wtforms import StringField,PasswordField,SubmitField, ValidationError
# from wtforms.validators import Required,Email,EqualTo
from wtforms import Form, BooleanField, StringField, validators, PasswordField, ValidationError
from .UserModel import UserModel

class RegistrationForm(Form):
    name    = StringField('Username', [validators.Length(min=4, max=25)])
    email        = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password     = PasswordField('Password', [validators.Length(min=4, max=25), validators.InputRequired()])
    confirm_password     = PasswordField('Confirm Password', [validators.Length(min=4, max=25), validators.InputRequired()])

    def validate_email(self,data_field):
            if UserModel.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if UserModel.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

    def get_password(self, data_field):
        return data_field.data

    def validate_confirm_password(self, data_field):   
        print(self.get_password(self.password))
        if data_field.data != self.get_password(self.password):
            raise ValidationError('The passwords did\'t match.')

class LoginForm(Form):
    email        = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password     = PasswordField('Password', [validators.Length(min=4, max=25), validators.InputRequired()])