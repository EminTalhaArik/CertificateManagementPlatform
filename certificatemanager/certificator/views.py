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
                print(cert.participant_name.encode('utf-8'))

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
            return render(request, 'certificator/certificate.html')

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

    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(make_certificates(str(event.certificate_file), participant_name, code))

    asyncio.run(make_certificates(str(event.certificate_file), participant_name, code))

    print("certificates done.")

    image_data = open("media/out/"+str(str(participant_name).encode('utf-8'))+".png", "rb")
    return FileResponse(image_data)


CODE_FONT_FILE = ImageFont.truetype(r'static/font/Roboto-LightItalic.ttf', 15)
FONT_COLOR = "#000000"

async def make_certificates(event, name, code):

    fontsize = 160
    font = ImageFont.truetype(r'static/font/GreatVibes-Regular.ttf', fontsize)

    image_source = Image.open(r'media/'+event)
    WIDTH, HEIGHT = image_source.size
    draw = ImageDraw.Draw(image_source)

    code = "Sertifika Kodu: TBK2023-" + code

    if name.__len__() > 25:
        fontsize = 140
        font = ImageFont.truetype(r'static/font/GreatVibes-Regular.ttf', fontsize)


    # Finding the width and height of the text. 
    name_width, name_height = draw.textsize(name, font=font)
    code_width, code_height = draw.textsize(code, CODE_FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=font)
    draw.text(((WIDTH - code_width) / 1.05, (HEIGHT - code_height) / 1.05), code, fill=FONT_COLOR, font=CODE_FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("media/out/"+str(str(name).encode('utf-8'))+".png")
    print('Saving Certificate of:', str(str(name).encode('utf-8')))

#endregion
