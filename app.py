from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy 

# init app
app = Flask(__name__)

# DB
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/database/users.db' # /// 3개 !!


# model schema
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(50))
	lastname = db.Column(db.String(50))


# Route
@app.route('/')
def index():
	return 'Hello Data Science Optimizers'

# HTML 파일 추가
@app.route('/home')
def home():
	return render_template('home.html')


# 
@app.route('/predict', methods=['GET', 'POST'])
def predict():
	if request.method == 'POST':
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		single_user = User(firstname=firstname, lastname=lastname)
		db.session.add(single_user)
		db.session.commit()

	return render_template('home.html', firstname=firstname.upper(), lastname=lastname)

@app.route('/allusers')
def allusers():
	userslist = User.query.all()
	print(userslist)
	return render_template('results.html', userslist=userslist)

@app.route('/profile/<firstname>')
def profile(firstname):
	user = User.query.filter_by(firstname=firstname).first()
	return render_template('profile.html', user=user)

# Templating , Jinja
@app.route('/about')
def about():
	mission = "Optimizing Data and ML Models with Python"
	return render_template('about.html', mission_frontend=mission)

if __name__ == '__main__':
	app.run(debug=True)
