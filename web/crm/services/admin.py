# Django core
from django.contrib import admin

# Our apps
from .models import Service, StudentServiceRelation, TelegramService

admin.site.register(Service)
admin.site.register(TelegramService)
admin.site.register(StudentServiceRelation)
