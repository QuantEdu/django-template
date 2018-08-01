from django.contrib import admin
from .models import User, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class CustomUserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]


admin.site.register(User, CustomUserAdmin)
