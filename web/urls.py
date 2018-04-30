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
# Development
import debug_toolbar
import django.contrib.auth.views as auth_views
# Django core
from django.contrib import admin
from django.urls import include, path

# Our own implementations
from apps.custom_admin.admin import custom_admin

urlpatterns = [
    # Core django paths
    path('super_admin/', admin.site.urls),
    path('admin/', custom_admin.urls),

    # Login views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social/', include('apps.social.urls')),

    # Development
    path('__debug__/', include(debug_toolbar.urls)),

    # Third party
    path('markdownx/', include('markdownx.urls')),

    # Our apps
    path('bot/', include('apps.bot.urls')),
    path('', include('apps.lp.urls')),
    path('lms/', include('apps.quiz.urls')),
    path('lms/', include('apps.lms.urls')),
]
