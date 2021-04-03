from django.urls import path
from movie.views import *

urlpatterns = [
    path('',home,name="home"),
    path('api/',movielist, name='api'),
    path('api/create/',MovieCreate, name="api_create"),
]
