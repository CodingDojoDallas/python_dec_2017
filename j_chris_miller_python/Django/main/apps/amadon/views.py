from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from products import items


def index(request):
	if "last_transaction" in request.session.keys():
		del request.session['last_transaction']

	context = {
		"items": items
	}

	return render(request, 'amadon/index.html', context)

def buy(request, item_id):
	#find item in our items list from the url's item_id matching the 'id' key on the item
	for item in items:
		if item['id'] == int(item_id):
			amount_charged = item['price'] * int(request.POST['quantity'])

	#exception handler for keys if they don't exist yet
	try:
		request.session['total_charged']
	except KeyError:
		request.session['total_charged'] = 0

	try:
		request.session['total_items']
	except KeyError:
		request.session['total_items'] = 0

	request.session['total_charged'] += amount_charged
	request.session['total_items'] += int(request.POST['quantity'])
	request.session['last_transaction'] = amount_charged
	return redirect('/checkout')

def checkout(request):
	return render(request, 'amadon/checkout.html')

