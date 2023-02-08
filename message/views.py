import json
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt

def send_message(longitude, latitude,messageType):
    print("sid",settings.TWILIO_NUMBER)
    try:
        message_to_broadcast = (f'Emmergency Message\nlive location: https://www.google.com/maps?q={latitude},{longitude}')
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
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
        print(latitude,longitude,messagetype)
        send_message(longitude, latitude, messagetype)
        return JsonResponse({'status': 'success'})
