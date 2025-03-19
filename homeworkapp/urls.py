
from django.urls import path, include
from .views import indexxx



app_name = 'homeworkapp'

urlpatterns = [
    path('', indexxx, name='indexxx'),


]