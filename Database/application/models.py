from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))

class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	password = db.Column(db.String(250), nullable=False)
	team_users = db.relationship('Teams', backref='customer', lazy=True)

	def __repr__(self):
		return ''.join(['User ID: ',str(self.id), '\r\n',
		 'Email: ', self.email, '\r\n', 'Name: ',
		 self.first_name, ' ', self.last_name])

class Players(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	team = db.Column(db.String(30), nullable=False)
	worth = db.Column(db.Integer, nullable=False)
	posistion = db.Column(db.String(30), nullable=False)
	picture = db.Column(db.LargeBinary, nullable=True)

class Teams(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	loosehead_prop = db.Column(db.Integer, nullable=False)
	hooker = db.Column(db.Integer, nullable=False)
	tighthead_prop = db.Column(db.Integer, nullable=False)
	left_lock = db.Column(db.Integer, nullable=False)
	right_lock = db.Column(db.Integer, nullable=False)
	blindside_flanker = db.Column(db.Integer, nullable=False)
	openside_flanker = db.Column(db.Integer, nullable=False)
	number_8 = db.Column(db.Integer, nullable=False)
	scrum_half = db.Column(db.Integer, nullable=False)
	fly_half = db.Column(db.Integer, nullable=False)
	left_wing = db.Column(db.Integer, nullable=False)
	inside_centre = db.Column(db.Integer, nullable=False)
	outside_centre = db.Column(db.Integer, nullable=False)
	right_wing = db.Column(db.Integer, nullable=False)
	fullback = db.Column(db.Integer, nullable=False)
	team_name = db.Column(db.String(30), nullable=False)