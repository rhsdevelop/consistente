from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember')

class UserEditForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    name = StringField('Nome completo', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Telefone')
    password = PasswordField('password', validators=[DataRequired()])
    active = BooleanField('remember')
