from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users, Players
from flask_login import current_user, LoginManager

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
			])
	last_name = StringField('Last Name',
		validators=[
			DataRequired(),
			Length(min=4, max=30)
			])
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired()
		])
	confirm_password = PasswordField('Confirm Password',
		validators=[
			DataRequired(),
			EqualTo('password')
		])
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = Users.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already in use!')

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired()
		])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
			])
	last_name = StringField('Last Name',
		validators=[
			DataRequired(),
			Length(min=4, max=30)
			])
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	submit = SubmitField('Update')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = Users.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email already in use!')	

class SelectionForm(FlaskForm):
	def players(name):
		choice, into = [], []
		names = Players.query.filter_by(posistion=name).all()

		for i in range(int(len(names))):
			name = names[i].first_name + ' ' + names[i].last_name + ': ' + str(names[i].worth)
			into = [name, name]
			choice.append(into)

		return choice

	positions = ['Loosehead Prop: ', 'Hooker: ', 'Tighthead Prop: ',
				'Left Lock: ', 'Right Lock: ', 'Blindside Flanker: ',
				'Openside Flanker: ', 'Number 8: ', 'Scrumhalf: ',
				'Flyhalf: ', 'Left Wing: ', 'Inside Centre: ',
				'Outside Centre: ', 'Right Wing: ', 'Fullback: ']

	choice = players('Prop')
	Loosehead_Prop = SelectField(positions[0], 
		choices=choice)

	choice = players('Hooker')
	Hooker = SelectField(positions[1], 
	 	choices=choice)

	choice = players('Prop')
	Tighthead_Prop = SelectField(positions[2], 
	 	choices=choice)

	choice = players('Locks')
	Left_Lock = SelectField(positions[3], 
		choices=choice)
	
	choice = players('Locks')
	Right_Lock = SelectField(positions[4], 
		choices=choice)
	
	choice = players('Flanker')
	Blindside_Flanker = SelectField(positions[5], 
		choices=choice)
	
	choice = players('Flanker')
	Openside_Flanker = SelectField(positions[6], 
		choices=choice)
	
	choice = players('Number 8')
	Number = SelectField(positions[7], 
		choices=choice)
	
	choice = players('Scrumhalf')
	Scrum_Half = SelectField(positions[8], 
		choices=choice)
	
	choice = players('Flyhalf')
	Fly_Half = SelectField(positions[9], 
		choices=choice)
	
	choice = players('Wings')
	Left_Wing = SelectField(positions[10], 
		choices=choice)
	
	choice = players('Centre')
	Inside_Centre = SelectField(positions[11], 
		choices=choice)
	
	choice = players('Centre')
	Outside_Centre = SelectField(positions[12], 
		choices=choice)
	
	choice = players('Wings')
	Right_Wing = SelectField(positions[13], 
		choices=choice)
	
	choice = players('Fullback')
	Fullback = SelectField(positions[14], 
		choices=choice)
	submit = SubmitField('Save!')