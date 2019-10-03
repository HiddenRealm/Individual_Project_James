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
	delete = SubmitField('Delete')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = Users.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email already in use!')

class DeletionForm(FlaskForm):
	deleteOne = SubmitField('Delete')
	deleteTwo = SubmitField('Delete')
	deleteThree = SubmitField('Delete')

class SelectionForm(FlaskForm):
	def players(name):
		choice, into = [], []
		names = Players.query.filter_by(posistion=name).all()

		for i in range(int(len(names))):
			name = names[i].first_name + ' ' + names[i].last_name + ': ' + str(names[i].worth)
			into = [names[i].id, name]
			choice.append(into)

		return choice

	positions = ['Loosehead Prop: ', 'Hooker: ', 'Tighthead Prop: ',
				'Left Lock: ', 'Right Lock: ', 'Blindside Flanker: ',
				'Openside Flanker: ', 'Number 8: ', 'Scrumhalf: ',
				'Flyhalf: ', 'Left Wing: ', 'Inside Centre: ',
				'Outside Centre: ', 'Right Wing: ', 'Fullback: ']

	choice = players('Prop')
	Loosehead_Prop = SelectField(positions[0], 
		choices=choice,
		coerce=int)

	choice = players('Hooker')
	Hooker = SelectField(positions[1], 
	 	choices=choice,
		coerce=int)

	choice = players('Prop')
	Tighthead_Prop = SelectField(positions[2], 
	 	choices=choice,
		coerce=int)

	choice = players('Locks')
	Left_Lock = SelectField(positions[3], 
		choices=choice,
		coerce=int)
	
	choice = players('Locks')
	Right_Lock = SelectField(positions[4], 
		choices=choice,
		coerce=int)
	
	choice = players('Flanker')
	Blindside_Flanker = SelectField(positions[5], 
		choices=choice,
		coerce=int)
	
	choice = players('Flanker')
	Openside_Flanker = SelectField(positions[6], 
		choices=choice,
		coerce=int)
	
	choice = players('Number 8')
	Number = SelectField(positions[7], 
		choices=choice,
		coerce=int)
	
	choice = players('Scrumhalf')
	Scrum_Half = SelectField(positions[8], 
		choices=choice,
		coerce=int)
	
	choice = players('Flyhalf')
	Fly_Half = SelectField(positions[9], 
		choices=choice,
		coerce=int)
	
	choice = players('Wings')
	Left_Wing = SelectField(positions[10], 
		choices=choice,
		coerce=int)
	
	choice = players('Centre')
	Inside_Centre = SelectField(positions[11], 
		choices=choice,
		coerce=int)
	
	choice = players('Centre')
	Outside_Centre = SelectField(positions[12], 
		choices=choice,
		coerce=int)
	
	choice = players('Wings')
	Right_Wing = SelectField(positions[13], 
		choices=choice,
		coerce=int)
	
	choice = players('Fullback')
	Fullback = SelectField(positions[14], 
		choices=choice,
		coerce=int)

	Team_Name = StringField('Team Name: ',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
			])

	submit = SubmitField('Save!')

	def validate_Loosehead_Prop(self, Loosehead_Prop):
		if self.Tighthead_Prop.data == Loosehead_Prop.data:
			raise ValidationError("Can't have two of the same Props")

	def validate_Tighthead_Prop(self, Tighthead_Prop):
		if Tighthead_Prop.data == self.Loosehead_Prop.data:
			raise ValidationError("Can't have two of the same Props")

	def validate_Left_Lock(self, Left_Lock):
		if self.Right_Lock.data == Left_Lock.data:
			raise ValidationError("Can't have two of the same Locks")

	def validate_Right_Lock(self, Right_Lock):
		if Right_Lock.data == self.Left_Lock.data:
			raise ValidationError("Can't have two of the same Locks")

	def validate_Blindside_Flanker(self, Blindside_Flanker):
		if self.Openside_Flanker.data == Blindside_Flanker.data:
			raise ValidationError("Can't have two of the same Flankers")

	def validate_Openside_Flanker(self, Openside_Flanker):
		if Openside_Flanker.data == self.Blindside_Flanker.data:
			raise ValidationError("Can't have two of the same Flankers")

	def validate_Left_Wing(self, Left_Wing):
		if self.Right_Wing.data == Left_Wing.data:
			raise ValidationError("Can't have two of the same Wings")

	def validate_Right_Wing(self, Right_Wing):
		if Right_Wing.data == self.Left_Wing.data:
			raise ValidationError("Can't have two of the same Wings")

	def validate_Inside_Centre(self, Inside_Centre):
		if self.Outside_Centre.data == Inside_Centre.data:
			raise ValidationError("Can't have two of the same Centre's")

	def validate_Outside_Centre(self, Outside_Centre):
		if Outside_Centre.data == self.Inside_Centre.data:
			raise ValidationError("Can't have two of the same Centre's")