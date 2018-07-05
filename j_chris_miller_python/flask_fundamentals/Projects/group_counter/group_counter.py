from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def index():
	if 'hit' not in	session:
		session['hit'] = 1
	else:
		session['hit'] +=1

	return render_template('index.html')

@app.route('/process', methods = ['POST'])
def increment():
	session['hit'] +=1
	return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
	session['hit'] = 0
	return redirect('/')

app.run(debug = True)