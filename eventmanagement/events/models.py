from django.db import models

# Create your models here.

# Organization Model
class Organization(models.Model):
    # blank = True set the field as non compulsory
    # Name of the organization 
    orgName = models.CharField(max_length=200, default='', blank=True)
    # Address for the organization
    Al1 = models.CharField(max_length=100, default=orgName, blank=True)
    Al2 = models.CharField(max_length=100, default='', blank=True)
    Al3 = models.CharField(max_length=100, default='', blank=True)
    district = models.CharField(max_length=40, default='', blank=True)
    state = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='India', blank=True)
    pinCode = models.IntegerField(default=0)
    # Logo of the organization
    logo = models.ImageField(blank=True)
    

class Participant(models.Model):
    partName = models.CharField(max_length=100)                 # Name of the participant
    partOrg = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, blank=True)       # Organization of the participant
    partCountry = models.CharField(max_length=100)              # Country of the participant
    partContact = models.BigIntegerField(blank=True)            # Contact Number of the participant
    partMail = models.EmailField(blank=True)                    # Email of the participant
    partPic = models.ImageField(blank=True)                     # Profile Picture of the participant

class Organizer(models.Model):
    OrganizerName = models.CharField(max_length=100)                    # Name of the organizer
    OrganizerContactNumber = models.BigIntegerField(blank=True)         # Contact Number of the organizer
    OrganizerMail = models.EmailField(blank=True)                       # Email of the organizer
    OrganizerOrganization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, blank=True) # Organization of the organizer
    OrganizerPic = models.ImageField(blank=True)                        # Profile Picture of the organizer

class Speaker(models.Model):
    speakerName = models.CharField(max_length=100)          # Name of the speaker
    speakerPic = models.ImageField(blank=True)              # Image of the speaker
    speakerLinkedIn = models.URLField(blank=True)           # LinkedIn of the speaker
    speakerIG = models.URLField(blank=True)                 # InstaGram of the speaker
    speakerFB = models.URLField(blank=True)                 # FaceBook of the speaker
    speakerTwitter = models.URLField(blank=True)            # Twitter of the speaker
    speakerWebSite = models.URLField(blank=True)            # WebSite of the speaker


class Event(models.Model):
    eventName = models.CharField(max_length=100, default='')                            # Name of the Event
    eventDescription = models.TextField(max_length=1000, default='', blank=True)        # Description of the event
    eventSpeaker = models.ForeignKey(Speaker, on_delete=models.DO_NOTHING, blank=True)  # Speaker of the Event
    eventStartTime = models.DateTimeField(blank=True)                                   # Start Time of the event
    eventEndTime = models.DateTimeField(blank=True)                                     # End Time of the event
    eventVenue = models.CharField(max_length=200, blank=True)                           # Venue of the event
    eventURL = models.URLField(blank=True)                                              # URL of the event
    