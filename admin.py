from flask import Blueprint, render_template, redirect, url_for, request, session
from flask_login import UserMixin, LoginManager, login_user, current_user, login_required, logout_user
from datetime import datetime, date



admin = Blueprint('admin',__name__,template_folder='adminTemplates')

from models import User, Posts
from app import db

@admin.route('/')
@login_required
def index():
    if current_user.admin == True:
        return redirect(url_for('admin.profiles'))
    else:
        return '''You don't have permisions'''

@admin.route('/profiles')
@login_required
def profiles():
    if current_user.admin == True:
        users=User.query.all()
        return render_template('adminIndex.html',users=users)
    else:
        return '''You don't have permisions'''

@admin.route('/posts')
@login_required
def posts():
    if current_user.admin == True:
        posts=Posts.query.all()
        return render_template('posts.html',posts=posts)
    else:
        return '''You don't have permisions'''


@admin.route('/contact-us-posts')
@login_required
def contactUs():
    if current_user.admin == True:
        messages = Posts.query.filter_by(title='Contact')
        return render_template('contactUsPosts.html',messages=messages)
    else:
        return '''You don't have permisions'''
