from flask import Flask, redirect, render_template, flash, session, request
import random
import datetime
import time

app=Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def gold():
	if 'gold' not in session:
		session['gold']=0
	return render_template('index.html')

@app.route('/process_money', methods = ["POST"])
def process():
	if request.form['building'] == 'farm':
		payout = random.randint(10,20)
		session['payout_str'] = "Earned " + str(payout) + " gold from the farm! " + str(datetime.datetime.now())
		# print session['payout_str']
		session['gold'] += payout

	if request.form['building'] == 'cave':
		payout = random.randint(5,10)
		session['payout_str'] = "Earned " + str(payout) + " gold from the cave! " + str(datetime.datetime.now())
		# print session['payout_str']
		session['gold'] += payout
		return redirect('/')

	if request.form['building'] == 'house':
		payout = random.randint(2,5)
		session['payout_str'] = "Earned " + str(payout) + " gold from the house! " + str(datetime.datetime.now())
		# print session['payout_str']
		session['gold'] += payout
		return redirect('/')	

	if request.form['building'] == 'casino':
		result = random.randint(0,1)
		payout = random.randint(0,50)
		if result == 1:			
			session['payout_str'] = "Earned " + str(payout) + " gold from the casino! " + str(datetime.datetime.now())
			# print session['payout_str']
			session['gold'] += payout
		else:
			session['loss_str'] = "Lost " + str(payout) + " gold from the casino! " + str(datetime.datetime.now())
			# print session['payout_str']
			session['gold'] -= payout
	return redirect('/')
		









app.run(debug=True)