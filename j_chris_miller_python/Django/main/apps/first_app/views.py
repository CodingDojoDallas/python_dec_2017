from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = "Hello, I am your first request"
	return HttpResponse(response)

def test(request):
	response = "This is a test"
	return HttpResponse(response)

def create(request):
	response = "This is create"
	return redirect(index)

def show(request, number):
	response = "blog " + number
	return HttpResponse(response)

def edit(request, number):
	response = "edit blog " + number
	return HttpResponse(response)

def destroy(request, number):
	return redirect(index)