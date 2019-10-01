from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Users, Players
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required


#  <img src="static/'ImageName.Format' alt="Error Text" height=?? width=??>

@app.route('/select')
def select():
	return render_template('select.html', title='Select')

@app.errorhandler(404)
def not_found(error):
	return render_template('error.html', title='No Page')

@app.route('/player/<int(min=1, max=100):player_id>')
def player(player_id):
	player_info = Players.query.filter_by(id=player_id).first()
	return render_template('player.html', title=player_info.first_name, num='1',
	 name=player_info.first_name + " " +player_info.last_name, team=player_info.team, 
	 worth=player_info.worth, position=player_info.posistion, lb=player_info.picture)

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('home'))
	return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		if current_user.is_authenticated:
			return redirect(url_for('home'))
		hashed_pw = bcrypt.generate_password_hash(form.password.data)
		user = Users(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			email=form.email.data, 
			password=hashed_pw)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('home')) #CHANGE THIS AT SOME POINT
	return render_template('register.html', title='Register', form=form)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)