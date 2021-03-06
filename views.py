from app import app, db
import models
from flask import render_template, redirect, url_for, request, session, flash
from flask_login import UserMixin, LoginManager, login_user, current_user, login_required, logout_user
import base64


@app.route('/', methods=['GET', 'POST'])
# Index page
def index():
    return render_template('index.html')


@app.route('/sign-up', methods=['POST'])
# Registration process
def signup():
    # requesting data
    name = request.form['name']
    surname = request.form['lastname']
    login = request.form['login']
    password = request.form['password']
    email = request.form['email']
    teacher = request.form.get('position')
    teacherId = None

    if teacher is None:
        teacher = False
        teacherId = request.form['teacherId']
    else:
        teacher = True

    loginInDatabase = models.User.query.filter_by(login=login).first()
    emailInDatabase = models.User.query.filter_by(email=email).first()

    if not loginInDatabase and not emailInDatabase:
        newUser = models.User(name=name, surname=surname, email=email, password=password, login=login,
                              teacherId=teacherId, teacher=teacher)

        db.session.add(newUser)
        db.session.commit()

        return redirect(url_for('login'))

    return '''email or login already exist'''


@app.route('/sign-in', methods=['GET', 'POST'])
# login page
def login():
    # checking requested method (login process or entry page)

    if request.method == 'POST':
        # Login process

        # requesting data
        login = request.form['login']
        password = request.form['password']

        # search login in database (User)

        userLoginInDatabase = models.User.query.filter_by(login=login).first()
        if userLoginInDatabase:
            if userLoginInDatabase.password == password:

                login_user(userLoginInDatabase)

                return redirect(url_for('profile', id=current_user.id))
            else:
                flash('Incorrect Password')
                return redirect(url_for('login'))
        else:
            flash('Incorrect login')
            return render_template('login.html')

    else:
        # Showing login pag
        return render_template('login.html')


@app.route('/logout')
# LogOut Function
@login_required
def logout():
    # killing cookie with logged user
    logout_user()

    # redirecting to main page
    return redirect(url_for('index'))


@app.route('/id<id>')
@login_required
# creating profile page route
def profile(id):
    profiles = models.User.query.filter_by(id=id).first()
    allData = models.User.query.all()
    # if requested profile id = curent user id, user can edit own page
    posts = models.Posts.query.filter_by(author=id)
    students = models.User.query.all()

    friends = models.Friends.query.all()

    frinedRequests = models.addingFriend.query.filter_by(requestTo=current_user.id)

    file_data = models.Image.query.filter_by(userID=id).first()

    return render_template('profile.html', profile=profiles, allData=allData,
                           posts=posts, students=students,
                           frinedRequests=frinedRequests, friends=friends,
                           data=list, file_data=file_data)


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
    email = request.form['email']
    text = request.form['message']
    author = '{0}-{1}'.format(name, email)

    message = models.Posts(title='Contact', body=text, author=author)
    db.session.add(message)
    db.session.commit()

    return redirect(url_for('profile', id=current_user.id))


@app.route('/add-message-to-wall-of-thoughts', methods=['GET', 'POST'])
@login_required
def wallOfThoughts():
    body = request.form['body']
    title = request.form['title']

    return redirect(url_for('addingPost', title=title, body=body, author=current_user.id))


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

    return redirect(url_for('profile', id=current_user.id))


@app.route('/edit-teacher-id', methods=['GET', 'POST'])
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
    return render_template('contact.html', messages=messages)


@app.route('/edit-posts-<postID>-post', methods=['POST'])
def editPosts(postID):
    text = request.form['body']

    post = models.Posts.query.get(postID)
    post.body = text

    db.session.commit()

    return redirect(url_for('profile', id=current_user.id))


@app.route('/sending-request-to-add-friend-<id>', methods=['POST'])
def sendingRequest(id):
    fromUser = models.addingFriend.query.filter_by(requestFrom=current_user.id)
    toUser = models.addingFriend.query.filter_by(requestTo=id)

    for fuser in fromUser:

        for tuser in toUser:

            if fuser and tuser:

                if fuser.id == tuser.id:
                    return redirect(url_for('profile', id=current_user.id))

    newRequest = models.addingFriend(requestFrom=current_user.id, requestTo=id)
    db.session.add(newRequest)
    db.session.commit()

    return redirect(url_for('profile', id=id))


@app.route('/adding-to-friend-<id>', methods=['POST', 'GET'])
def addingFriend(id):
    requestTo = models.addingFriend.query.filter_by(requestTo=current_user.id)
    requestFrom = models.addingFriend.query.filter_by(requestFrom=id)

    for i in requestFrom:
        for j in requestTo:
            if j.id == i.id:
                newFrriend = models.Friends(firstUserID=i.requestFrom, secondUserID=i.requestTo)
                db.session.add(newFrriend)
                db.session.commit()

                db.session.delete(i)
                db.session.commit()
                break

    return redirect(url_for('profile', id=current_user.id))


@app.route('/searching', methods=['GET', 'POST'])
def finder():
    search = request.form['search']

    

    users = models.User.query.filter_by(name=search)
    posts = models.Posts.query.filter_by(body=search)

    return render_template('searchResults.html', users=users, posts=posts)


@app.route('/editing-email-address-user', methods=['POST'])
def editEmail():
    email = request.form['email']
    x = models.User.query.get(current_user.id)
    x.email = email

    db.session.commit()
    return redirect(url_for('profile', id=current_user.id))


@app.route('/editting-profile-photo', methods=['POST'])
def editingPhoto():
    file = request.files['inputFile']
    a = models.Image.query.filter_by(userID=current_user.id).first()
    if a:
        a.data = file.read()
        db.session.commit()
    else:
        new = models.Image(userID=current_user.id, data=file.read())
        db.session.add(new)
        db.session.commit()
    return redirect(url_for('profile', id=current_user.id))