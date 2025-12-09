from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path("home/", home_page, name="home_name"),
    path("about/", about_page, name="about_name"),
    path("contact/", contact_page, name="contact_name"),   
]
