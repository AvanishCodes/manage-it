from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Event, Organization, Organizer, Participant, Speaker

# Create your views here.
def index(request):
    return render(request, "events/index.html", {
        "events": Event.objects.all()
    })

def event(request, event_id):
    event = Event.objects.get(pk=event_id)
    # Get the event and the participants of the event
    instance = {
        'event': event,
        'participants': event.participants.all(),
        # 'non_participants': Participant.objects.exclude(events = event).all()
    }
    return render(request, "events/displayEvent.html", instance)

def register(request, event_id):
    return render(request, "events/register.html")