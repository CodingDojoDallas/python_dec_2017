from flask import Flask, render_template, session, request, redirect, flash
import random

app = Flask(__name__)

app.secret_key = "yoyoyo"

@app.route('/')

def number_game():
	print type(session['num'])
	# del session['num']
	if 'num' not in session:
		session['num'] = random.randint(0, 100)
		print session['num']
	return render_template('index.html')

@app.route('/guess', methods=['POST'])

def guess():
	var = int(request.form['guess'])
	if var == session['num']:
		print session['num']
		flash("You Win!")
		session['num']= random.randint(0,100)
	elif var > session['num']:
		print session['num']
		flash("Too high.")
	elif var < session['num']:
		print session['num']
		flash("Too low.")
	return redirect('/')


app.run(debug=True)
