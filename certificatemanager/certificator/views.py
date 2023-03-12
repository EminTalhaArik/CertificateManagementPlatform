from django.http import HttpResponse
from django.shortcuts import render

from .models import EventType, Event, Participant

# Create your views here.
def main(request):
    search = request.GET.get('search')

    if search != "" and search != None:
        events = Event.objects.filter(event_participants__participant_mail=search)
        participant = Participant.objects.filter(participant_mail=search)

        print(participant)

        context = {
            "events": events,
            "participant": participant
        }

        return render(request, 'certificator/certificate.html', context)

    else:

        certificates = Event.objects.all()

        context = {
            "events": Event.objects.all(),
        }

        return render(request, 'certificator/index.html', context)





