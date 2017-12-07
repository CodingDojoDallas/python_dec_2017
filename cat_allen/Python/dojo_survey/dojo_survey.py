from flask import Flask, render_template, redirect, request, session, flash

app = Flask (__name__)

app.secret_key = "yoyoyo"

@app.route('/')

def dojo_survey():
	return render_template('index.html')

@app.route('/submit', methods=['POST'])

def submit():
	print "Form Success"
	name = request.form['name']
	if len(request.form['name']) < 1:
    		flash("Name cannot be empty!") 
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']



	return render_template('submitted.html', name=name, location=location, language=language, comment=comment)
	

app.run(debug=True)