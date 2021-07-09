from sys import displayhook
from django.shortcuts import render
from .models import Random
import os
from twilio.rest import Client
from decouple import config
# Create your views here.

def home(request):
    if request.method == 'POST':
        num = request.POST['num']
        


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
        # account_sid = config('TWILIO_ACCOUNT_SID', cast=str)
        # auth_token = config('TWILIO_AUTH_TOKEN', cast=str)
        # client = Client(account_sid, auth_token)

        # message = client.messages.create(
        #                         body='Hi there',
        #                         from_=config('twilio_num'),
        #                         to='+918943755785'
        #                     )

        # print(message.sid)
    random = Random.objects.all()
    context = {'random':random,}
    return render(request,'index.html',context)