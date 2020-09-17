import os
from consistente import app

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
SECRET_KEY = '4NBn148Y4VkzFnN6o8Gk'
#SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # Para docker (heroku)
#SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = True
#app.config['SECRET_KEY'] = SECRET_KEY