from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import datetime

def index(request):
	context = {
		"time": datetime.datetime.now()
	}
	return render(request, 'timedisplay/index.html', context)