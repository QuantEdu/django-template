# Django core
from django.contrib import admin

# Our apps
from .models import UserSocialAuth

admin.site.register(UserSocialAuth)
