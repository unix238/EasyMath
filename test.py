#import modules
from flask import Blueprint, render_template, redirect, url_for, request, session
from flask_login import UserMixin, LoginManager, login_user, current_user, login_required, logout_user
from datetime import datetime, date



#creating Blueprint object
test = Blueprint('test',__name__,template_folder='testTemplates')

from app import db

import models


@test.route('/')
def index():
	questions = models.Question.query.all()
	return render_template('test_index.html', questions=questions)


@test.route('<id>')
def detail(id):
	question = models.Question.query.get(id)
	answers = models.Answer.query.filter_by(questionID = id)
	return render_template('detail.html', answers=answers, question=question)