from django.contrib import admin
from .models import Event
from .models import Participant
from .models import EventType

class EventAdmin(admin.ModelAdmin):
    filter_horizontal = ['event_participants']


admin.site.register(Event, EventAdmin)
admin.site.register(Participant)
admin.site.register(EventType)

