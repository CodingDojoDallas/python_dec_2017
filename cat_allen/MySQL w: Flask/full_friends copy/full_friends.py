from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM full_friends.friends"  
    friends = mysql.query_db(query) 
    print friends
    return render_template('index.html', all_friends=friends) 

@app.route('/friends', methods=['POST'])
def create():

    query = "INSERT INTO full_friends.friends (name, age, friend_since, created_at) VALUES (:name, :age, NOW(), NOW())"
    data = {
             'name': request.form['name'],
             'age':  request.form['age'],
           }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)