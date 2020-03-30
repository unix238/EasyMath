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


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(150))
    author = db.Column(db.String(100), nullable=True)

    def __init__(self, question, author):
        self.question = question
        self.author = author
        
    
    def __repr__(self):
        return '<questions %r>' % self.question


class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(150))
    studentId = db.Column(db.String(100), nullable=False)
    questionId = db.Column(db.Integer)

    def __init__(self, answer, studentId, questionId):
        self.answer = answer
        self.studentId = studentId
        self.questionId = questionId
    
    def __repr__(self):
        return '<answer %r>' % self.answer



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

