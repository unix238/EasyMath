from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, current_user, login_required, logout_user
from itsdangerous import URLSafeTimedSerializer



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

from test import test


app.register_blueprint(test, url_prefix='/test')

@login_manager.user_loader
def load_user(user_id):

	return User.query.get(int(user_id))


if __name__ == '__main__':
	app.run(debug=False)