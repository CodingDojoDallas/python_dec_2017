from flask import Flask, request, redirect, render_template, flash
app = Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
	if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['email'])< 1 or len(request.form['password']) < 1 or len(request.form['confirm_password']) < 1:
		flash('All fields are required', 'required')

	if request.form['password'] != request.form['confirm_password']:
		flash('Passwords must match')

	elif '@' not in request.form['email']:
		flash('Invalid email')

	elif len(request.form['password']) < 8:
		flash('Password must be at least 8 characters')

	# elif request.form['first_name']
	# can't figure out syntax for str instance
	
	else:
		flash('You were successfully logged in')
	return redirect('/')


app.run(debug=True)