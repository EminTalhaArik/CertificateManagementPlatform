import asyncio
import string
import random

from django.http import HttpResponse, FileResponse
from django.shortcuts import render

from .models import EventType, Event, Certificate
from PIL import Image, ImageFont, ImageDraw


def main(request):
    search = request.GET.get('search')

    if search != "" and search != None:

        if '@' in search:
            certificates = Certificate.objects.filter(participant_mail=search)

            for cert in certificates:
                print(cert.participant_name)

            context = {
                "certificates": certificates,
            }

            return render(request, 'certificator/certificate.html', context)
        
        elif '-' in search:
            code = search.split('-')[1]
            certificates = Certificate.objects.filter(id=code)
            
            context = {
                "certificates": certificates
            }

            return render(request, 'certificator/certificate.html', context)

    else:

        certificates = Event.objects.all()

        context = {
            "events": Event.objects.all(),
        }

        return render(request, 'certificator/index.html', context)


#region Certificate Generator

def generate_certificate(request):    
    event_search = request.GET.get('event')
    participant_name = request.GET.get('participant')
    code = request.GET.get('code')

    event = Event.objects.get(event_name=event_search)

    asyncio.run(make_certificates(str(event.certificate_file), participant_name, code))

    print("certificates done.")

    image_data = open("media/out/"+participant_name+".png", "rb")
    return FileResponse(image_data)


NAME_FONT_FILE = ImageFont.truetype(r'static/font/GreatVibes-Regular.ttf', 180)
CODE_FONT_FILE = ImageFont.truetype(r'static/font/Roboto-LightItalic.ttf', 30)
FONT_COLOR = "#FFFFFF"

async def make_certificates(event, name, code):

    image_source = Image.open(r'media/'+event)
    WIDTH, HEIGHT = image_source.size
    draw = ImageDraw.Draw(image_source)

    letters = string.ascii_uppercase
    random_code = ''.join(random.choice(letters) for i in range(7))

    code = "Sertifika Kodu: " + random_code + "-" + code

    # Finding the width and height of the text. 
    name_width, name_height = draw.textsize(name, font=NAME_FONT_FILE)
    code_width, code_height = draw.textsize(code, CODE_FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=NAME_FONT_FILE)
    draw.text(((WIDTH - code_width) / 1.05, (HEIGHT - code_height) / 1.05), code, fill=FONT_COLOR, font=CODE_FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("media/out/"+name+".png")
    print('Saving Certificate of:', name)

#endregion
