# URLconf
from django.urls import path

from quiz import views

urlpatterns = [
    path('quizzes/', views.QuizListView.as_view(), name='quiz_list'),

    path('quiz/<int:pk>/', views.QuizDetailView.as_view(), name='quiz_detail'),
    path('quiz/<int:pk>/take', views.quiz_take, name='quiz_take'),
    path('quiz/<int:pk>/result/', views.QuizDetailView.as_view(), {'fresh': True}, name='quiz_result'),

    path('quiz/result/<int:pk>', views.QuizProgressView.as_view(), name='quiz_progress'),
]
