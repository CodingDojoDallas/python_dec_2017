from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

mysql = MySQLConnector(app,'email_valid')

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/email', methods=['POST'])
def create():
	print request.form['email']
	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
	else:
		flash("The e-mail address you entered ("+ request.form['email'] +") is a VALID email address! Thank you!")
		query = "INSERT INTO email_valid.email (email, created_at) VALUES (:email, NOW())"
		data = {
			'email': request.form['email'],
		}
		mysql.query_db(query, data)
		return redirect('/success')
	return redirect('/')

@app.route('/success')
def success():
	query = "SELECT * FROM email_valid.email"  
	email = mysql.query_db(query) 
	return render_template('success.html', all_email=email) 

app.run(debug=True)