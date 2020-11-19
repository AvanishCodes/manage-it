from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Event, Organization, Organizer, Participant, Speaker

# Create your views here.
def index(request):
    return render(request, "events/allEvents.html", {
        "events": Event.objects.all()
    })