from django.urls import path

from . import views

urlpatterns = [
path("register",views.registerPage, name="register"),
path("registration", views.registration, name = "registration"),
path("login", views.loginPage, name="login") ,
path("logout",views.logout, name="logout"),
path("about",views.about,name="about"),
path("admin",views.admin, name="admin"),

]