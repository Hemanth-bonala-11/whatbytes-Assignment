from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('login', login_page),
    path('signup', signup_page),
    path('create_user', signup_logic),
    path('logging_in', credentials_check),
    path('dashboard', dashboard),
    path('profile', profile),
    path('change_password', change_password),
    path('logout', logout_user),
    path('reset_password', reset_password)
]
