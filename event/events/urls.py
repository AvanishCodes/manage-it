from django.urls import path
from . import views

urlpatterns = [
    path('<int:eventID>/', views.eventDetail, name='event'),
    path('', views.events, name='events-page'),
]