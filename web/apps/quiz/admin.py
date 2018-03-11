# Django core
from django.contrib import admin

# Models
from .models import Quiz, QuizProgress

# Core django admin site register
admin.site.register(Quiz)
admin.site.register(QuizProgress)
