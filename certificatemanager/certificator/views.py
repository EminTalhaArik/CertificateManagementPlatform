import types
import sys
import asyncio
import string
import random
from os import path

from django.http import HttpResponse, FileResponse
from django.shortcuts import render

from .models import EventType, Event, Certificate
from PIL import Image, ImageFont, ImageDraw

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


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


# region Certificate Generator

def generate_certificate(request, code):
    certificate_code = code

    if path.exists("media/out/"+str(certificate_code)+".png"):
        image_data = open(
            "media/out/"+str(certificate_code)+".png", "rb")
        return FileResponse(image_data)

    else:
        certificate = Certificate.objects.get(pk=certificate_code)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(make_certificates(certificate))
        finally:
            loop.close()
            asyncio.set_event_loop(None)

        image_data = open(
            "media/out/"+str(certificate_code)+".png", "rb")
        return FileResponse(image_data)


CODE_FONT_FILE = ImageFont.truetype(r'static/font/Roboto-LightItalic.ttf', 15)
BIG_FONTSIZE = 160
SMALL_FONTSIZE = 140
BIG_TEXT_FONT = ImageFont.truetype(
    r'static/font/GreatVibes-Regular.ttf', BIG_FONTSIZE)
SMALL_TEXT_FONT = ImageFont.truetype(
    r'static/font/GreatVibes-Regular.ttf', SMALL_FONTSIZE)
FONT_COLOR = "#000000"


async def make_certificates(certificate):

    participant_name = certificate.participant_name
    certificate_code = certificate.id
    certificate_file = certificate.event.certificate_file

    image_source = Image.open(
        r'media/'+str(certificate_file))
    WIDTH, HEIGHT = image_source.size
    draw = ImageDraw.Draw(image_source)

    code = "Belge Kodu: TKB2023-" + str(certificate_code)

    if participant_name.__len__() > 25:
        font = SMALL_TEXT_FONT
    else:
        font = BIG_TEXT_FONT

    name_width, name_height = draw.textsize(
        participant_name, font=font)
    code_width, code_height = draw.textsize(
        str(certificate_code), CODE_FONT_FILE)

    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) /
              2 - 30), participant_name, fill=FONT_COLOR, font=font)
    draw.text(((WIDTH - code_width) / 1.18, (HEIGHT - code_height) /
              1.05), code, fill=FONT_COLOR, font=CODE_FONT_FILE)

    image_source.save("media/out/"+str(certificate_code)+".png")
    print('Saving Certificate of:', str(
        str(participant_name).encode('utf-8')))

# endregion
