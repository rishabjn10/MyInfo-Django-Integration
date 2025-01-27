from django.urls import path
from .views import auth_login, auth_callback

urlpatterns = [
    path('auth/login/', auth_login, name='auth-login'),
    path('auth/callback/', auth_callback, name='auth-callback'),
]
