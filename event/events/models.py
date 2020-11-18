from django.db import models

# Create your models here.

# Definition of a person who is organizing an event
class person(models.Model):
    name = models.CharField(max_length = 50)
    contactNumber = models.CharField(max_length = 15)
    def __str__(self):
        return self.name

# Definition of an event
class event(models.Model):
    eventName = models.CharField(max_length = 100)
    eventDescription = models.CharField(max_length = 500)
    eventImage = models.ImageField()
    eventKeyPerson = models.ForeignKey(person, on_delete=models.CASCADE)
    eventStartTime = models.DateTimeField()
    eventEndTime = models.DateTimeField()
    def __str__(self):
        return self.eventName