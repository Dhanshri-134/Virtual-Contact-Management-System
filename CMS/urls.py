
from django.contrib import admin
from django.urls import path
from CMS import views


urlpatterns = [
    path('', views.index, name="index"),
    path('index.html',views.index, name="index"),
    path('about.html',views.about, name="about"),
    path('services.html',views.services, name="services"),
    path('contact.html',views.contact, name="contact"),
    path('signin.html',views.signin, name="signIn"),
    path('login.html',views.login, name="logIn")

]