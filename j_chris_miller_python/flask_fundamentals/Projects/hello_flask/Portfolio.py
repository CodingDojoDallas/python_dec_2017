from flask import Flask, render_template
app = Flask(__name__)

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')


# def hello_world():
    # return "Hello World" render_template('index.html')
app.run(debug=True)


