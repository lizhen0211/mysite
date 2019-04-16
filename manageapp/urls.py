from django.urls import path

from manageapp.views import index

app_name = 'manageapp'
urlpatterns = [
    path('index', index)
]