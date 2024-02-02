from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegister, name="register"),
    path('login/', userLogin, name="login"),
    path('profiles/', profiles, name="profiles"),
    path('create/', createProfil, name="create"),
    path('logout/', userLogout, name="logout" ),
    path('hesap/', hesap, name="hesap"),
    path('delete/', userDelete, name="delete"),
]