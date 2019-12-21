from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"


urlpatterns = [
    #user/register
    path('register/', views.register, name = "register"),
    #user/login
    path('login/', views.loginUser, name = "login"),
    #user/logout
    path('logout/', views.logoutUser, name = "logout"),
]

