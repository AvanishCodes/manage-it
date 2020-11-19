from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Event, Organization, Organizer, Participant, Speaker

# Create your views here.
def index(request):
    return render(request, "events/index.html", {
        "events": Event.objects.all()
    })

def event(request, event_id):
    return render(request, "allEvents.html")

def register(request, event_id):
    return None