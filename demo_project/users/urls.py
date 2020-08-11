from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.Signupview, name = 'signup'),
    path('login/', views.Loginview, name = 'login'),
]