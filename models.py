from app import db
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    login = db.Column(db.String(20), unique=True, nullable=False)
    teacherId = db.Column(db.Integer, nullable=True)
    teacher = db.Column(db.Boolean, nullable=False)
    admin = db.Column(db.Boolean, nullable=True)

    def __init__(self, name, surname, email, password, login, teacherId, teacher):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.login = login
        self.teacherId = teacherId
        self.teacher = teacher
    

        

    def __repr__(self):
        return '<User %r>' % self.name



class Posts (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(200))
    author = db.Column(db.String)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    

    def __init__(self, title, body, author):
        self.title = title
        self.body = body
        self.author = author

    

    def __repr__(self):
        return '<postTitle %r> ' % self.title



class addingFriend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requestFrom = db.Column(db.Integer, nullable=False)
    requestTo = db.Column(db.Integer, nullable = True)
    friend = db.Column(db.Boolean, default=False, nullable=True)

    def __init__(self, requestFrom,requestTo):
        self.requestFrom = requestFrom
        self.requestTo = requestTo
    

    def __repr__(self):
        return '<requestFrom %r> ' % self.requestFrom



class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstUserID = db.Column(db.Integer)
    secondUserID = db.Column(db.Integer)
    

    def __init__(self, firstUserID,secondUserID):
        self.firstUserID = firstUserID
        self.secondUserID = secondUserID
    

    def __repr__(self):
        return '<firstUserID %r> ' % self.firstUserID



class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer)
    data = db.Column(db.BLOB)



class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    cheked = db.Column(db.Boolean)

    def __init__(self, body,cheked):
        self.body = body
        self.cheked = cheked

    def __repr__(self):
        return f"Question: {self.body}"



class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(70))
    correct = db.Column(db.Boolean)
    questionID = db.Column(db.Integer)

    def __init__(self, answer, correct, questionID):
        self.answer = answer
        self.correct = correct
        self.questionID = questionID

    def __repr__(self):
        return f"Answer: {self.answer} [{self.correct}] [ID: {self.questionID}]"