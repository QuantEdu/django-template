# URLconf
from django.urls import path

from apps.crm.social import views


app_name = 'social'
urlpatterns = [
    path('vk/complete', views.vk_complete, name='vk_complete'),
]
