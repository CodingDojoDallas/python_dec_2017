from django.shortcuts import render, HttpResponse, redirect
# Import required to use datetime
from datetime import datetime

def index(request):
    # If no word list is in session, create empty array to append them into
    if 'words' not in request.session:
        request.session['words'] = []

    return render(request, "main_app/index.html")

def add_word(request):
    # Set size to empty unless checkbox was selected
    size = ''
    if 'big_font' in request.POST:
        size = 'big_font'

     # Set color to empty unless a radio button was selected
    color = ''
    if 'color' in request.POST:
        color = request.POST['color']

    # Gets the current time and formats it into a string
    # See http://strftime.org/ or https://www.foragoodstrftime.com/ for more info
    # Note the datetime import at top
    date = datetime.now().strftime("%I:%M:%S%p, %B %e, %Y")
    
    # Collect data on word and enter into dictionary
    word = {
        'word': request.POST['word'],
        'color': color,
        'size': size,
        'created_at': date
    }

    # Can't append word into request.session directly
    temp = request.session['words']
    temp.append(word)
    request.session['words'] = temp

    return redirect(index)

def clear(request):
    # Clear the session of the entire word list
    del request.session['words']
    return redirect(index)