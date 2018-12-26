# URLconf
from django.urls import path

from bot import views


app_name = 'bot'
urlpatterns = [
    path('callback', views.callback, name='callback'),
]
