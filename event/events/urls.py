from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.events, name='events'),
    path('<int:eventID>', views.eventDetail, name='eventDetail'), 
]