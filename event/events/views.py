from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import event, person
from django.template import loader

# Create your views here.

def index(request):
    return 

def events(request):
    allEvents = event.objects.all()
    template = loader.get_template('events/allEvents.html')
    context = {
        'allEvents': allEvents
    }
    return HttpResponse(template.render(context, request))

def eventDetail(request, eventID):
    try:
        thisEvent = event.objects.get(pk = eventID)
    except events.DoesNotExist:
        raise Http404("Event does not exist")
    template = loader.get_template('events/sampleEvent.html') 
    context = {
        'eventID': eventID
    }
    return render(request, "events/sampleEvent.html", {
        'thisEvent': thisEvent,
        'detail': thisEvent.eventDetail
    })
