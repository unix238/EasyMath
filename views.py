from app import app,db
import models
from flask import render_template, redirect, url_for, request, session
from flask_login import UserMixin, LoginManager, login_user, current_user, login_required, logout_user



@app.route('/', methods=['GET', 'POST'])
#Index page
def index():
	return render_template('index.html')


@app.route('/sign-up', methods = ['POST'])
#Registration procces
def signup():
	#requsting data
	name = request.form['name']
	surname = request.form['lastname']
	login = request.form['login']
	password = request.form['password']
	email = request.form['email']
	teacher = request.form.get('position')
	teacherId = None
	
	if teacher == None:
		teacher = False
		teacherId = request.form['teacherId']
	else:
		teacher = True
	
	loginInDatabase = models.User.query.filter_by(login=login).first()
	emailInDatabase = models.User.query.filter_by(email=email).first()

	if not loginInDatabase and not emailInDatabase:

		newUser = models.User(name=name, surname=surname, email=email, password=password, login=login, teacherId=teacherId, teacher=teacher, q1=False, q2=False, q3=False, q4=False, q5=False, q6=False, q7=False, q8=False, q9=False, q10=False)

		db.session.add(newUser)
		db.session.commit()

		return redirect(url_for('login'))

	return '''email or login alredy exist'''




@app.route('/sign-in', methods=['GET','POST'])
#login page 
def login():
	#cheking requsted method (login procces or entry page)

	if request.method == 'POST':
		#Login procces 

		#requsting data
		login = request.form['login']
		password = request.form['password']

		#search login in database (User) 

		userLoginInDatabase = models.User.query.filter_by(login=login).first()

		if userLoginInDatabase.password == password:

			login_user(userLoginInDatabase)

			return redirect(url_for('profile', id=current_user.id))
		else:

			return '''encorrect password'''
	else:
		#Showing login page

		return render_template('login.html')


@app.route('/logout')
#LogOut Function
@login_required
def logout():
	#killing cookie with logged user
    logout_user()
	
	#redirecting to main page
    return redirect(url_for('index'))


@app.route('/id<id>')
@login_required
#creating profile page route
def profile(id):
	
	profiles = models.User.query.filter_by(id=id).first()
	allData = models.User.query.all()
	#if requested profile id = curent user id, user can edit own page
	posts = models.Posts.query.filter_by(author=id)
	students = models.User.query.all()
	answers = models.Answers.query.all()
	

	return render_template('profile.html', profile=profiles, allData=allData, posts=posts, students=students, answers=answers)



@app.route('/adding-post-<title>-<body>-<author>', methods=['POST', 'GET'])
@login_required
def addingPost(title, body, author):
	
	newPost = models.Posts(title=title, body=body, author=author)
	db.session.add(newPost)
	db.session.commit()
	return redirect(url_for('profile', id=current_user.id))

@app.route('/deletePost-<postID>')
@login_required
def deletePost(postID):
	post = models.Posts.query.filter_by(id=postID).first()

	db.session.delete(post)
	db.session.commit()

	return redirect(url_for('profile', id=current_user.id))


@app.route('/contact-form', methods=['POST'])
@login_required
def contactForm():
	name = request.form['name']
	email =request.form['email']
	text = request.form['message']
	author = '{0}-{1}'.format(name,email)

	message = models.Posts(title='Contact', body=text, author=author)
	db.session.add(message)
	db.session.commit()

	return redirect(url_for('profile', id=current_user.id))


@app.route('/add-message-to-wall-of-thoughts', methods=['GET','POST'])
@login_required
def wallOfThoughts():
	body = request.form['body']

	return redirect(url_for('addingPost', title='New Post', body=body, author=current_user.id))


@app.route('/edit-password', methods=['POST'])
@login_required
def editPassword():
	oldPassword = request.form['oldPassword']
	password = request.form['password1']
	passwordVerification = request.form['password2']

	if oldPassword == current_user.password and passwordVerification == password:
		profile = models.User.query.filter_by(id=current_user.id).first()
		profile.password = password
		db.session.commit()

	return redirect(url_for('profile',id=current_user.id))	


@app.route('/edit-teacher-id', methods=['GET','POST'])
@login_required
def editTeacherId():

	teacherId = request.form['teacherId']
	current_user.teacherId = teacherId
	db.session.commit()

	return redirect(url_for('profile', id=current_user.id))


@app.route('/edit-password')
@login_required
def editPasswordView():
	
	return render_template('password.html')

@app.route('/contact-us-views')
def contactUsView():
	messages = models.Posts.query.filter_by(title='Contact')
	return render_template('contact.html', messages = messages)


@app.route('/edit-posts-<postID>-post', methods=['POST'])
def editPosts(postID):
	text = request.form['body']

	post = models.Posts.query.get(postID)
	post.body = text

	db.session.commit()

	return redirect(url_for('profile',id=current_user.id))


