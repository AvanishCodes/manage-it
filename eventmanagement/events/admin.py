from django.contrib import admin
from .models import Event, Organization, Organizer, Participant, Speaker

# Register your models here.
# class EventAdmin(admin.ModelAdmin):
admin.site.register(Organization)
admin.site.register(Organizer)
admin.site.register(Participant)
admin.site.register(Event)
admin.site.register(Speaker)