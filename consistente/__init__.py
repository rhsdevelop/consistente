import os
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
port = int(os.environ.get("PORT", 5000))
manager.add_command('runserver', Server(host='0.0.0.0', port=port))

lm = LoginManager(app)
lm.login_view = 'auth.login'

from consistente.controllers import default
from consistente.models import tables