from django.urls import path
from .import views
from . forms import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.Registration,name='register'),
    path('accaount/login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('accaount/logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout')
]
