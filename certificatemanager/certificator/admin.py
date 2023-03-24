from import_export.admin import ImportExportModelAdmin
from .resources import CertificateResource
from django.contrib import admin
from .models import Event
from .models import EventType
from .models import Certificate

class EventAdmin(admin.ModelAdmin):
    list_display = ('id','event_name','event_date')

class CertificateAdmin(ImportExportModelAdmin):
    list_display = ('id', 'participant_name', 'participant_mail')
    resource_class = CertificateResource      
 

admin.site.register(Event, EventAdmin)
admin.site.register(EventType)
admin.site.register(Certificate, CertificateAdmin)

