#import modules
from flask import Blueprint, render_template, redirect, url_for, request, session
from flask_login import UserMixin, LoginManager, login_user, current_user, login_required, logout_user
from datetime import datetime, date



#creating Blueprint object
test = Blueprint('test',__name__)

from models import User, Question, Answers

from app import db

#localhost:5000/profile/<profile> 
@test.route('/')
def index():
	return redirect(url_for('test.start'))


@test.route('/start')
def start():
	allQuestions = Question.query.all()
	return render_template('start.html', allQuestions=allQuestions)


@test.route('/<questionId>')
def questionDetail(questionId):
	question = Question.query.filter_by(id=questionId).first()
	return render_template('questionDetail.html', question=question)


@test.route('/collecting-answers', methods=['POST'])
def collectingAnswers():
	answer = request.form['answer']
	questionNumber = request.form['questionID']
	print(questionNumber)
	newAnswer = Answers(answer=answer, studentId = current_user.id, questionId=questionNumber)
	db.session.add(newAnswer)
	db.session.commit()
	if questionNumber == '1':
		current_user.q1 = True
		db.session.commit()
		print(questionNumber)
	
	if questionNumber == '2':
		current_user.q2 = True
		db.session.commit()
		print(questionNumber)

	if questionNumber == '3':
		current_user.q3 = True
		db.session.commit()
		print(questionNumber)

	if questionNumber == '4':
		current_user.q4 = True
		db.session.commit()

	if questionNumber == '5':
		current_user.q5 = True
		db.session.commit()

	if questionNumber == '6':
		current_user.q6 = True
		db.session.commit()

	if questionNumber == '7':
		current_user.q7 = True
		db.session.commit()

	if questionNumber == '8':
		current_user.q8 = True
		db.session.commit()

	if questionNumber == '9':
		current_user.q9 = True
		db.session.commit()

	if questionNumber == '10':
		current_user.q10 = True
		db.session.commit()


	if current_user.q1 == True and current_user.q2 == True and current_user.q3 == True and current_user.q4 == True and current_user.q5 == True and current_user.q6 == True and current_user.q7 == True and current_user.q8 == True and current_user.q9 == True and current_user.q10 == True:
		
		return redirect(url_for('addingPost', title='finished work !', body="Waiting for teacher result's", author=current_user.id)) 
	else:
		return redirect(url_for('test.start'))
	
@test.route('/adding-questions', methods=['POST','GET'])
def admin():
	
	if request.method == 'GET':
		return '''
		<form method='POST' action="adding-questions">
			<input type='text' name='question'>
			<input type='submit'> 
		</form>
		'''
	if request.method == 'POST':
		question = request.form['question']
		newQuestion = Question(question, 'admin')
		db.session.add(newQuestion)
		db.session.commit()
		return redirect(url_for('test.admin'))