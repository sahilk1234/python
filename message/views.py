import json
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt


def send_message(longitude, latitude, messageType):
    print("sid", settings.TWILIO_NUMBER)
    try:
        numers = []
        message_to_broadcast = ""
        if messageType == "contact":
            numers = settings.CONTACTS_NUMBERS
            message_to_broadcast = (
                f'Emmergency Message to Contacts\nlive location: https://www.google.com/maps?q={latitude},{longitude}')
        else:
            numers = settings.POLICE_NUMBERS
            message_to_broadcast = (
                f'Emmergency Message to Police\nlive location: https://www.google.com/maps?q={latitude},{longitude}')

        client = Client(settings.TWILIO_ACCOUNT_SID,
                        settings.TWILIO_AUTH_TOKEN)
        for recipient in numers:
            if recipient:
                client.messages.create(to=recipient,
                                       from_=settings.TWILIO_NUMBER,
                                       body=message_to_broadcast)
    except ValueError:
        print(ValueError)


@csrf_exempt
def index(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        longitude = body['longitude']
        latitude = body['latitude']
        messagetype = body['messageType']
        print(latitude, longitude, messagetype)
        send_message(longitude, latitude, messagetype)
        return JsonResponse({'status': 'success'})
