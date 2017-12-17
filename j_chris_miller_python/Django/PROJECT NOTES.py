#Step by Step instructions for creating a new project:

0. Make sure youre in your virtual enviornment:
source DjangoEnv/Scripts/activate

1. Create project: > django-admin startproject {{project_name}}
2. Create an apps folder inside main project folder
3. Create __init__.py and add to apps folder **Note it will have no code in it.
4. Create the app. You must be in your apps folder: 
> python ../manage.py startapp {{app_name}} **Note that you cannot name it the same as the project or you will get an error.
5. Create urls.py and import:

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index), 
	url(r'^add_word$', views.add_word), #this will differ depending on your method
	url(r'^clear$', views.clear) #this will differ depending on your method
]

6. In the 2nd main folder which is siblings with apps, open your urls.py file. Include the following:

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.{{app_name}}.urls')),
    url(r'^{{app_name}}/', include('apps.{{app_name}}.urls')),
]

7. Create views.py and import libraries: 

from django.shortcuts import render, HttpResponse, redirect

8. Create a templates folder and a static folder in your {{app_name}} folder.
9. Inside templates and static, create {{app_name}} folder
10. Inside templates/{{app_name}} create index.html and other templates files - Include {% csrf_token %} in html
11. Inside static/{{app_name}} create CSS folder, images folder, and javascript folder
12. When using sessions, run the following code from the terminal in your project folder:
	> python manage.py makemigrations
	> python manage.py migrate

13. In the second main folder (sibling to apps) open the settings.py file and add your app to the list of apps using the following syntax:
	'apps.{{app_name}}', **Place it at the top of the list and do not forget the comma or you will get an error
14. In the apps urls.py folder, make sure you add a url for each view in the patterns such as:
url(r'^add_word$', views.add_word) **Note, remember to use commas to separate the urls.


request.session**
**'DONT FORGET COMMAS IN SETTINGS.PY'
**'DONT FORGET TO MIGRATE'

111111. Shell Command 11111111.
NameError: name 'Ninjas' is not defined
solution: from apps.app_name.models import * 
