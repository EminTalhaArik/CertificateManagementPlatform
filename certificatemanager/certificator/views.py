from django.http import HttpResponse, FileResponse
from django.shortcuts import render

from .models import EventType, Event, Participant
from PIL import Image, ImageFont, ImageDraw

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


def generate_certificate(request):    
    event_name = request.GET.get('event')
    participant_name = request.GET.get('participant')

    context = {
        'event_name': event_name,
        'participant_name': participant_name
    }


    make_certificates(event_name ,participant_name)

    print("certificates done.")

    image_data = open("media/"+ participant_name +".png", "rb")
    return FileResponse(image_data)


FONT_FILE = ImageFont.truetype(r'static/font/GreatVibes-Regular.ttf', 180)
FONT_COLOR = "#FFFFFF"

def make_certificates(event, name):

    image_source = Image.open(r'media/'+event+'.png')
    WIDTH, HEIGHT = image_source.size
    draw = ImageDraw.Draw(image_source)

    # Finding the width and height of the text. 
    name_width, name_height = draw.textsize(name, font=FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("media/"+name+".png")
    print('Saving Certificate of:', name)        
