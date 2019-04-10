from django.urls import path

from aggregation.views import index

app_name = 'aggregation'
urlpatterns = [
    path('index', index)
]
