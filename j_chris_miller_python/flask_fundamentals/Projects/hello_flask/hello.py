from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojos():
	return render_template('dojos.html')

# def hello_world():
    # return "Hello World" render_template('index.html')
app.run(debug=True)


