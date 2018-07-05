from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, 'survey/index.html')

def display_result(request):
	return render(request, 'survey/result.html')

def process(request):
	try:
		request.session['tries']
	except KeyError:
		request.session['tries'] = 0
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	request.session['tries'] +=1
	return redirect('/result')

