from django.contrib import admin
from django.urls import path
from .views import AuthenticateUser
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('authenticateuser/', AuthenticateUser.as_view(), name='authenticateuser'),
]
