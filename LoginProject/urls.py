from django.contrib import admin
from django.urls import path
from appProfile import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="home"),
    path('signup/', views.SignUp, name="signup"), # ruta para registrarse
    path('logged/', views.Logged, name="logged"),  #ruta para cuando ya esta iniciada la sesion
    path('logout/', views.LogOut, name="logout"), #ruta para cuando cierra sesion
    path('login/', views.Login, name="login") #ruta para cuando va hacer login
]
