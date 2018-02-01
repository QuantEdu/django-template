"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django core
# from django.conf import settings
from django.contrib import admin
from django.urls import include, path

# Our own implementations
from apps.custom_admin.admin import custom_admin


urlpatterns = [
    # Core django paths
    path('super_admin/', admin.site.urls),
    path('admin/', custom_admin.urls),


    # Third party
    path('markdownx/', include('markdownx.urls')),

    # Our apps
    path('', include('apps.example.urls')),
]
