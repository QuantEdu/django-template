# URLconf
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('main/<int:number>/', views.NumIndexView.as_view(), name='num_index'),
]
