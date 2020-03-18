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
    q1 = db.Column(db.Boolean, nullable=False)
    q2 = db.Column(db.Boolean, nullable=False)
    q3 = db.Column(db.Boolean, nullable=False)
    q4 = db.Column(db.Boolean, nullable=False)
    q5 = db.Column(db.Boolean, nullable=False)
    q6 = db.Column(db.Boolean, nullable=False)
    q7 = db.Column(db.Boolean, nullable=False)
    q8 = db.Column(db.Boolean, nullable=False)
    q9 = db.Column(db.Boolean, nullable=False)
    q10 = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, surname, email, password, login, teacherId, teacher, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.login = login
        self.teacherId = teacherId
        self.teacher = teacher
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10

    

        

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