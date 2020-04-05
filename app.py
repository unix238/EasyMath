from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, current_user, login_required, logout_user
from itsdangerous import URLSafeTimedSerializer
import base64


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
login_serializer = URLSafeTimedSerializer(app.secret_key)
login_manager.login_view = 'login'




from views import *
from models import User

from admin import admin
from test import test
import jinja2

def decoding(img):
	image = base64.b64encode(img.data).decode('ascii')
	return image


def date(pub_date):
	date = str(pub_date)
	temp = date[11::]
	g = temp[:5:]
	return g


jinja2.filters.FILTERS['b64decode'] = decoding
jinja2.filters.FILTERS['date'] = date


app.register_blueprint(test, url_prefix='/test')
app.register_blueprint(admin, url_prefix='/admin')

@login_manager.user_loader
def load_user(user_id):

	return User.query.get(int(user_id))


if __name__ == '__main__':
	app.run(debug=True)