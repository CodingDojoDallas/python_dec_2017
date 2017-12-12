from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime


def index(request):
	if 'words' not in request.session:
		request.session['words'] = []
	return render(request, "session_words/index.html")

def add_word(request):
	big_font = ''
	if 'big_font' in request.POST:
		big_font = 'big_font'
	word = {
		'word': request.POST['word'],
		'color': request.POST['color'],
		'big_font': big_font,
		'time': datetime.now().strftime("%H:%M %p, %B %d, %Y")
	}
	temp = request.session['words']
	temp.append(word)
	request.session['words'] = temp
	return redirect(index)

def clear(request):
	del request.session['words']
	return redirect(index)
