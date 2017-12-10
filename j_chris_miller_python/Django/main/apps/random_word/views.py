from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import random

def index(request):
	try:
		request.session['tries']
	except KeyError:
		request.session['tries'] = 0

	return render(request, 'random_word/index.html')

def generate(request):
	request.session['tries'] +=1
	request.session['random'] = get_random_string(length=14)
	return redirect('/')

def reset(request):
	del request.session['tries']
	del request.session['random']
	return redirect('/')

