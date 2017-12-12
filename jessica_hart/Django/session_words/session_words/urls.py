from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
    # Common name in routes can be entered here
    # All routes in main_app will now start with "session_words/" (completely optional)
    url(r'^session_words/', include('apps.main_app.urls'))
]
