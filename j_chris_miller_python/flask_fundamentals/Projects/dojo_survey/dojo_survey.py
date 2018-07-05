from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def process():
   print "Got Post Info"
   # email = request.form['email']
   comment = request.form['comment']
   if len(request.form['name']) < 1:
   	flash("Name cannot be empty!")
   if len(request.form['comment']) < 1:
   	flash("Comment cannot be empty!")
   if len(request.form['comment']) > 120:
   	flash("Comment too long!")
   else:
   	flash("Success your name is {}".format(request.form['name']))


   return redirect('/')

   # return render_template('/result.html', name = name, email = email, comment = comment)
app.run(debug=True) # run our server
