from django.urls import path

from search.views import index

app_name = 'search'
urlpatterns = [
    path('index', index)
]