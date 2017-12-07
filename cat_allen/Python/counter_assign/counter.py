from flask import Flask, render_template, session, request, redirect

app = Flask (__name__)

app.secret_key = "yoyoyo"

@app.route('/')

def index():
	if 'hit' not in session:
		session['hit'] = 1
	else:
		session['hit'] += 1

	return render_template('index.html')

@app.route('/process/<action>', methods=['POST'])

def process(action):
	if request.form['action'] == 'increment':
		session['hit'] +=1
	elif request.form['action'] == 'reset':
		session['hit'] = -1
	return redirect('/')

app.run(debug=True)
