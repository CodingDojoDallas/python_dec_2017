from flask import Flask, render_template, request #, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/ninja')
def ninja():
   return render_template('/ninja.html')

@app.route('/ninja/<color>')
def image(color):
	if color == "blue":
		return render_template('/ninja.html', color = "leonardo.jpg")
	if image == "red":
		return render_template('/ninja.html', color = "raphael.jpg")
	if image == "purple":
		return render_template('/ninja.html', color = "donatello.jpg")
	if image == "orange":
		return render_template('/ninja.html', color = "michelangelo.jpg")
	else: 
		return render_template('/ninja.html', color = "notapril.jpg")


app.run(debug=True) # run our server
