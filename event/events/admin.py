from django.contrib import admin

from .models import event, person

# Register your models here.

admin.site.register(person)
admin.site.register(event)
