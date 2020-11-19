# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path("<int:event_id>", views.event, name="event"),
    path("<int:event_id>/register", views.register, name="register")
]
