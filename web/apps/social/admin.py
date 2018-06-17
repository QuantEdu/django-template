# Django core
from django.contrib import admin

# Our apps
from .models import VKAuth

admin.site.register(VKAuth)
