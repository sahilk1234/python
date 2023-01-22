from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import Client


def send_message(numbers):
    message_to_broadcast = ("Emergency Message")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in numbers:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)


def broadcast_sms(request):
    return send_message(settings.SMS_BROADCAST_TO_NUMBERS)
    
def index(request):
    if (request.GET.get('smsBtn')):
        broadcast_sms(request)
        context = {
            "sms": "true"
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')
