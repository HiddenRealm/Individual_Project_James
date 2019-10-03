from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Users, Players, Teams
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm, SelectionForm
from flask_login import login_user, current_user, logout_user, login_required#, LoginManager
import base64


#  <img src="static/'ImageName.Format' alt="Error Text" height=?? width=??>

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
		return redirect(url_for('login'))
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

@app.route('/select', methods=['GET', 'POST'])
def select():
	form = SelectionForm()
	extra = ''
	amount = Teams.query.filter_by(user_id=current_user.id).all()
	if amount:
		print(amount)
		amount = len(amount)
		print(amount)
	else:
		amount = 0

	if form.validate_on_submit():
		num = worth([form.Loosehead_Prop.data, form.Hooker.data,
					form.Tighthead_Prop.data, form.Left_Lock.data,
					form.Right_Lock.data, form.Blindside_Flanker.data,
					form.Openside_Flanker.data, form.Number.data,
					form.Scrum_Half.data, form.Fly_Half.data,
					form.Left_Wing.data, form.Inside_Centre.data,
					form.Outside_Centre.data, form.Right_Wing.data,
					form.Fullback.data])
		if amount < 3:
			if num <= 45000:
				team = Teams(
					user_id=current_user.id,
					loosehead_prop=form.Loosehead_Prop.data,
					hooker=form.Hooker.data,
					tighthead_prop=form.Tighthead_Prop.data, 
					left_lock=form.Left_Lock.data,
					right_lock=form.Right_Lock.data,
					blindside_flanker=form.Blindside_Flanker.data,
					openside_flanker=form.Openside_Flanker.data,
					number_8=form.Number.data,
					scrum_half=form.Scrum_Half.data,
					fly_half=form.Fly_Half.data,
					left_wing=form.Left_Wing.data,
					inside_centre=form.Inside_Centre.data,
					outside_centre=form.Outside_Centre.data,
					right_wing=form.Right_Wing.data,
					fullback=form.Fullback.data)
				db.session.add(team)
				db.session.commit()
				return redirect(url_for('home'))
			else:
				extra = 'Costs too much: ' + str(num) + ' Should be less than 30,000'
		else:
			extra = 'You can only have 3 teams at once, please delete one of you previous teams if you want to add a new one'
	return render_template('select.html', title='Select', form=form, totWorth=0, more=extra)

@app.route('/player/<int(min=1, max=100):player_id>')
def player(player_id):
	player_info = Players.query.filter_by(id=player_id).first()
	pic = base64.b64encode(player_info.picture)
	return render_template('player.html', title=player_info.first_name, num='1',
	 name=player_info.first_name + " " +player_info.last_name, team=player_info.team, 
	 worth=player_info.worth, position=player_info.posistion, lb=pic)

@app.route('/select/<int(min=1, max=10):select_id>', methods=['GET', 'POST'])
def selection(select_id):
	term = Players.query.filter_by(id=(select_id * 10)).first()
	players = Players.query.filter_by(posistion=term.posistion).all()
	num = ((select_id - 1) * 10)
	lists = []
	for i in range(10):
		temp = players[i].first_name + ' ' + players[i].last_name + ': ' + players[i].team
		lists.append(temp)

	return render_template('selection.html', title=term.posistion, num=num, player1=lists[0],
		player2=lists[1], player3=lists[2], player4=lists[3],
		player5=lists[4], player6=lists[5], player7=lists[6],
		player8=lists[7], player9=lists[8], player10=lists[9])

@app.errorhandler(404)
def not_found(error):
	return render_template('error.html', title='No Page')

def worth(lists):
	num=0
	for x in range(15):
		num+= Players.query.filter_by(id=lists[x]).first().worth
	return num